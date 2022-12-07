from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


def get_ranking():
    # Get raw data from website
    page_url = 'https://www.mphonline.org/green-states/'
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

    # get a list of all header
    headers_rec = table.findAll('th')
    headers = []
    for i in range(len(headers_rec)):
        headers.append(headers_rec[i].contents[0])
    # we only need the first 2 headers 'state' and 'overall rank'
    headers = headers[:2]

    # data in each row are in the tag <tbody><tr></tr></tbody>, so get it
    rows = table.findAll('td')

    row_data = []
    for i in range(len(rows)):
        row_data.append(rows[i].contents[0])

    # We only need the first column data "state", and the second one "ranking"
    row_data = (np.array(row_data).reshape(50, 6))[:, :2]
    # print(row_data)

    df = pd.DataFrame(row_data[:, 1],
                      columns=['GreenSpace_ranking'],
                      index=row_data[:, 0])

    greenspace_ranking = df['GreenSpace_ranking'].astype(int)
    greenspace_ranking = 51 - greenspace_ranking

    return greenspace_ranking


if __name__ == '__main__':
    print(get_ranking())
