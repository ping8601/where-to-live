import pandas as pd
import requests
import numpy as np    

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

    linecodes_file = open('raw data/line_code.csv', 'r', encoding='utf-8')
    linecodes = []

    # import line codes
    for line in linecodes_file:
        linecodes.append(line[:-1].split(',')[1])
        
    linecodes_file.close()

    # get PCE data from BEA API
    key = '7FF96A0A-ECF1-40D8-A002-2EF594D46991'
    year = '2021'
    table = 'SAPCE3'
    df = pd.DataFrame()

    for index in range(len(linecodes)):
        PCE_url = 'https://apps.bea.gov/api/data/?UserID={0}&'\
        'method=GetData&datasetname=Regional&TableName={1}'\
        '&LineCode={2}&Year={3}&GeoFips=STATE&ResultFormat=json'\
        .format(key, table, index + 1, year)
        
        response = requests.request('GET', PCE_url)
        raw_data = response.json()
        # raw_data_f.write(str(response.json()))
        if index == 0:
            geoName = [x['GeoName'] for x in raw_data['BEAAPI']['Results']['Data']]
            df['State'] = geoName
            df = df.set_index('State')
        data = [float(x['DataValue'].replace(',', '')) for x in raw_data['BEAAPI']['Results']['Data']]
        df[linecodes[index]] = data
        
    # only get the state data
    df = df[df.index.isin(US_state_list)]

    # get population data from Census
    # the PCE info is for all the population and we need per person data for comparison purpose
    census_key = '9d18ed9ae62b66a8458cbe6710738ac9b207464b'
    variable = 'group(NST_EST2021_POP)'

    pop_url = 'https://api.census.gov/data/2021/pep/population?get=NAME,POP_{0}&for=state:*&key={1}' \
        .format(year, census_key)
        
    pop_response = requests.request('GET', pop_url)
    # turn data into DataFrame
    pop_df = pd.DataFrame(pop_response.json()[1:], columns=pop_response.json()[0])
    # drop unnecessary info
    pop_df = pop_df.drop('state', axis = 1)
    # change the data type
    NAME = pop_df['NAME']
    pop_df = pop_df.loc[:, pop_df.columns == 'POP_2021'].astype(int)
    pop_df['NAME'] = NAME
    # rename the column
    pop_df = pop_df.rename({'NAME' : 'State','POP_2021': 'Population'}, axis='columns')
    pop_df = pop_df.set_index('State')

    # only get the state data
    pop_df = pop_df[pop_df.index.isin(US_state_list)]

    # create per_capita_df to record per capita PCE
    per_capita_df = pd.DataFrame(index=df.index)
    per_capita_df['Personal consumption expenditures'] = df['Personal consumption expenditures'] * 1000000 / pop_df['Population']

    per_capita_df['Personal consumption expenditures'] = per_capita_df['Personal consumption expenditures'].round(0).astype(int)

    # rank per person PCE from highest cost to lowest cost
    per_capita_df = per_capita_df.sort_values(by=['Personal consumption expenditures'], ascending=False)

    per_capita_df['Expense_ranking'] = [i for i in range(1, 51)]
    PCE_rank = per_capita_df['Expense_ranking']

    return (per_capita_df['Personal consumption expenditures'], PCE_rank)

if __name__ == '__main__':
    print(get_data())
    
# linecode
# https://apps.bea.gov/iTable/?reqid=70&step=1&isuri=1&acrdn=7#eyJhcHBpZCI6NzAsInN0ZXBzIjpbMSwyNCwyOSwyNSwzMSwyNiwyNywzMF0sImRhdGEiOltbIlRhYmxlSWQiLCI1MjQiXSxbIkNsYXNzaWZpY2F0aW9uIiwiTkFJQ1MiXSxbIk1ham9yX0FyZWEiLCIwIl0sWyJTdGF0ZSIsWyIwIl1dLFsiQXJlYSIsWyJYWCJdXSxbIlN0YXRpc3RpYyIsWyItMSJdXSxbIlVuaXRfb2ZfbWVhc3VyZSIsIkxldmVscyJdLFsiWWVhciIsWyIyMDIxIl1dLFsiWWVhckJlZ2luIiwiLTEiXSxbIlllYXJfRW5kIiwiLTEiXV19