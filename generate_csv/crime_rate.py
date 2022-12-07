#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 20:19:50 2022

@author: Kaia
"""

#https://www.wikiwand.com/en/List_of_U.S._states_and_territories_by_violent_crime_rate
import pandas as pd

#%% save raw data
def get_data():
    pd.set_option('display.max_columns', None)
    url = 'https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_violent_crime_rate'
    tables = pd.read_html(url)[0]
#rawdata = open('raw_crime_rate.txt', 'wt', encoding='utf-8')
#if __name__ == '__main__':
#rawdata.write(str(tables))
#rawdata.close()

#%% clean data in csv
    temp = tables.drop(0)
    temp.columns=['states','Incidence Count','2020','2019','2018',\
              '2017','2016','2015','2014','2013','2012','2011']

#change datatype
    states = temp['states'].astype(str)
    temp = temp.loc[:,temp.columns != 'states'].apply(pd.to_numeric)
    temp.index= states

# calculate crime rate (cases per 10000 inhabitants)
    temp. drop(index='United States',inplace=True)
    temp['crime rate(per 10000)']= (temp['2020']+temp['2019']+temp['2018']+temp['2017']+temp['2016']\
                                    +temp['2015']+temp['2014']+temp['2013']+temp['2012']+temp['2011'])/10/10
    temp['crime rate(per 10000)']=temp['crime rate(per 10000)'].round(2)

# drop District of Columbia & Puerto Rico
    temp = temp.drop(['District of Columbia', 'Puerto Rico'])

# sort by crime rate (descending)
    temp.sort_values(by='crime rate(per 10000)', ascending=False, inplace= True)
    temp['Crime_ranking']=[i for i in range (1,51)]
    crime_rank= temp['Crime_ranking'].astype(int)

# output
    return (temp['crime rate(per 10000)'], crime_rank)

if __name__ == '__main__':
   print(get_data())


