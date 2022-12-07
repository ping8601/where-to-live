import pandas as pd

# import all the data scraping modules
import personal_consumption_expenditure
import education_attainment
import green_space
import health_funding
import crime_rate
import income

# import data normolization module
import data_normolization

personal_consumption_expenditure_data, personal_consumption_expenditure_ranking = personal_consumption_expenditure.get_data()
education_attainment_data, education_attainment_ranking = education_attainment.get_data()
crime_rate_data, crime_rate_ranking = crime_rate.get_data()
health_funding_data, health_funding_ranking = health_funding.get_data()
income_data, income_ranking = income.get_data()

# put all the data in the same dataframe
all_data = pd.concat([
  personal_consumption_expenditure_data,
  education_attainment_data,
  crime_rate_data,
  health_funding_data,
  income_data
  ], axis = 1)

# put all rank data in the same dataframe
all_rank = pd.concat([
  personal_consumption_expenditure_ranking,
  education_attainment_ranking,
  green_space.get_ranking(),
  crime_rate_ranking,
  health_funding_ranking,
  income_ranking
  ], axis = 1)

# save unnormalized rank data into csv
all_rank.to_csv('all_rank.csv')

# save data into csv
all_data.to_csv('all_data.csv')

# get all the columns
columns = list(all_rank)

# create a new dataframe to store normalized data
all_rank_normal = pd.DataFrame(index=all_rank.index)

for column in columns:
  all_rank_normal[column] = data_normolization.minmax_normalization(all_rank[column])
  
# save normalized data into csv
all_rank_normal.to_csv('all_rank_normal.csv')