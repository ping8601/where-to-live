import csv
import pandas as pd

def clean(type):
    if type == 'prcp':
        input_name = 'prcp-inventory'
    else:
        input_name = 'all_stations'

    input = open("source/{0}.txt".format(input_name), "rt", encoding="utf-8")

    state_station_dict = {line.split()[0]: line.split()[4] for line in input}

    input.close()

    inputf = open("source/mly-{0}-filled.txt".format(type), "rt", encoding="utf-8")
    # outputf = open("{0}_result.txt", "wt", encoding="utf-8")

    res_list = []
    for line in inputf:
        exit_flag = False
        line_data = line.split()
        if int(line_data[1]) > 2004 and int(line_data[1]) < 2011:
            i  = 2
            while i < len(line_data):
                try:
                    line_data[i] = int(line_data[i]) / 100
                except:
                    exit_flag = True
                    break
                i += 1
            if exit_flag == True: continue
            try:
                line_data[0] = state_station_dict[line_data[0]]
            except:
                continue
            res_list.append(line_data)

    inputf.close()
    state_set =  {li[0] for li in res_list}

    with open('cleaned/state_{0}.csv'.format(type), 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(['State Name', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

        for i in state_set:
            temp_res = [i, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            count = 0
            for j in res_list:
                if j[0] == i:
                    k = 1
                    while k < len(temp_res):
                        temp_res[k] += j[k+1]
                        k += 1
                    count += 1
            m = 1
            while m < len(temp_res):
                temp_res[m] = round(temp_res[m] / count, 2)
                m += 1
            wr.writerow(temp_res)
    
clean('tmax')
clean('tmin')
clean('prcp')

# summer: Jun ~ Aug
# winter: Dec ~ Feb

# Hot Summer(0) - Cool Summer(1)
# Dry Summer(0) - Rainy Summer(1)
# Warm Winter(0) - Cold Winter(1)
# Dry Winter(0) - Rainy / Snowy Winter(1)

df_result = pd.DataFrame(columns=["State Name","Cool Summer","Rainy Summer","Cold Winter","Rainy / Snowy Winter"], index = range(58))

df = pd.read_csv(r'cleaned/state_tmax.csv')
summer_avg_max_temp = (df['Jun'].mean()+  df['Jul'].mean() + df['Aug'].mean())/3

i = 0

while i <= 57:
    df_result.iloc[i,0] = df.iloc[i,0]
    if (df.iloc[i,6]+df.iloc[i,7]+df.iloc[i,8])/3 > summer_avg_max_temp:
        df_result.iloc[i,1] = 0
    else:
        df_result.iloc[i,1] = 1
    i += 1

df = pd.read_csv(r'cleaned/state_tmin.csv')
winter_avg_min_temp = (df['Dec'].mean()+  df['Jan'].mean() + df['Feb'].mean())/3

i = 0

while i <= 57:
    if (df.iloc[i,12]+df.iloc[i,1]+df.iloc[i,2])/3 > winter_avg_min_temp:
        df_result.iloc[i,3] = 0
    else:
        df_result.iloc[i,3] = 1
    i += 1

df = pd.read_csv(r'cleaned/state_prcp.csv')
summer_avg_prcp = (df['Jun'].mean()+  df['Jul'].mean() + df['Aug'].mean())/3

i = 0

while i <= 57:
    if (df.iloc[i,6]+df.iloc[i,7]+df.iloc[i,8])/3 < summer_avg_prcp:
        df_result.iloc[i,2] = 0
    else:
        df_result.iloc[i,2] = 1
    i += 1

df = pd.read_csv(r'cleaned/state_prcp.csv')
winter_avg_prcp = (df['Dec'].mean()+  df['Jan'].mean() + df['Feb'].mean())/3

i = 0

while i <= 57:
    if (df.iloc[i,12]+df.iloc[i,1]+df.iloc[i,2])/3 < winter_avg_prcp:
        df_result.iloc[i,4] = 0
    else:
        df_result.iloc[i,4] = 1
    i += 1

df_result.to_csv("climate_classification.csv",index=False)