import pandas as pd
import requests

def get_data():
    US_state_list = ["Alabama", "Alaska", "Arizona", "Arkansas",
                    "California", "Colorado", "Connecticut",
                    "Delaware", "Florida", "Georgia", "Hawaii",
                    "Idaho", "Illinois", "Indiana", "Iowa",
                    "Kansas", "Kentucky", "Louisiana", "Maine",
                    "Maryland", "Massachusetts", "Michigan",
                    "Minnesota", "Mississippi", "Missouri",
                    "Montana", "Nebraska", "Nevada", "New Hampshire",
                    "New Jersey", "New Mexico", "New York",
                    "North Carolina", "North Dakota", "Ohio",
                    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
                    "South Carolina", "South Dakota", "Tennessee",
                    "Texas", "Utah", "Vermont", "Virginia", "Washington",
                    "West Virginia", "Wisconsin", "Wyoming"]

    # census_api_key = '9d18ed9ae62b66a8458cbe6710738ac9b207464b'
    year = '2021'
    variable = 'group(S1501)'

    url = 'https://api.census.gov/data/{0}/acs/acs1/subject?get={1}&for=state:*' \
        .format(year, variable)
        
    response = requests.request('GET', url)

    # save raw data in a txt file
    # raw_data = response.json()
    # raw_data_f = open('raw_education_attainment.txt', 'w', encoding='utf-8')
    # raw_data_f.write(str(raw_data))
    # raw_data_f.close()

    df = pd.DataFrame(response.json()[1:], columns=response.json()[0])

    code_dict = {
        'NAME': 'State',
        'S1501_C01_006E': 'Total Population 25 years and over',
        'S1501_C01_009E': 'High school graduate (includes equivalency)' ,
        'S1501_C01_012E': "Bachelor's degree" ,
        'S1501_C01_013E': 'Graduate or professional degree'
        }

    # only get the data we want
    df = df.loc[:,['NAME', 'S1501_C01_006E', 'S1501_C01_009E', 'S1501_C01_012E', 'S1501_C01_013E']]

    # change the data type
    NAME = df['NAME']
    df = df.loc[:, df.columns != 'NAME'].astype(int)
    df['NAME'] = NAME

    # add less than high school column
    df['Less than high school'] = df['S1501_C01_006E'] - df['S1501_C01_009E'] - df['S1501_C01_012E'] - df['S1501_C01_013E']

    # change column name
    df = df.rename(code_dict, axis='columns')

    # set state as index
    df = df.set_index('State')

    # rearrange the data
    df = df.reindex(columns=['Total Population 25 years and over',
                            'Less than high school',
                            'High school graduate (includes equivalency)',
                            "Bachelor's degree",
                            'Graduate or professional degree'
                            ])

    df['Higher education %'] = (df["Bachelor's degree"] + df['Graduate or professional degree']) / df['Total Population 25 years and over'] * 100
    
    df['Higher education %'] = df['Higher education %'].round(2)

    # only get the state data
    df = df[df.index.isin(US_state_list)]

    # rank from lowest higher education % to highest higher education %
    df = df.sort_values(by=['Higher education %'])

    df['Education_ranking'] = [i for i in range(1, 51)]
    education_rank = df['Education_ranking']
    return (df['Higher education %'], education_rank)

if __name__ == '__main__':
    print(get_data())
    
# variables: https://data.census.gov/cedsci/table?q=S1501&g=0100000US%240400000&tid=ACSST1Y2021.S1501
# tutorial: https://levelup.gitconnected.com/how-to-get-total-population-from-the-census-api-using-python-bbf23758bfa7