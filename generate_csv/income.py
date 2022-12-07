from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd

def get_data():
    # Get data from website
    page_url = 'https://fred.stlouisfed.org/release/tables?rid=110&eid=257197#snid=257202'
    req = Request(page_url)
    req.add_header('user-agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/107.0.0.0 Safari/537.36')
    rawpage = urlopen(req).read()
    bs = BeautifulSoup(rawpage, 'lxml')


    # Clean data
    # get a list of all table tags
    table_list = bs.findAll('table')

    # there is only one table, so get it
    table = table_list[0]
    # data in each row are in the tag <tr></tr>, so get it
    rows = table.findAll('tr')

    # the first 2 rows are headers
    first_headers = rows[0].findAll('th')
    second_headers = rows[1].findAll('th')

    # we only need the 2nd title in the first headers
    header = ('State', first_headers[2].contents[0])

    # use the "rec" to store the data we need extract from the remaining rows.
    df = pd.DataFrame(columns=['Incomes'])
    # the first two rows are headers, so we begin from the third one
    for row in rows[2:]:
        # use tmp to store the data extract from each row
        row_data = row.findAll('td')
        city_name = row_data[1].contents[3].contents[0].contents[0]
        per_capital_income = int((re.findall(r'\d+.\d+', row_data[2].contents[0])[0]).replace(',', ''))
        # add data from the same row to our final record
        df.loc[city_name] = per_capital_income

    # drop District of Columbia & Puerto Rico
    df = df.drop(['District of Columbia'])

    df = df.sort_values('Incomes')

    df['Incomes_ranking'] = [i + 1 for i in range(len(df))]

    return (df['Incomes'], df['Incomes_ranking'].astype(int))

if __name__ == '__main__':
    print(get_data())