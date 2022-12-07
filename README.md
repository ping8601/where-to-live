# where-to-live
WHERE TO LIVE is an app that helps users to find the most suitable US state to live in based on a simple survey and provides living environment information about the state. The app offers a recommendation state after users rank the environment feature according to their preference. Besides, information that home seekers care about most like climate, education rates, crime rates, health funding, income and living cost from the most recent database of each state can also be found on the recommendation page.

* Survey pages

![image](https://user-images.githubusercontent.com/107028314/206202044-88570aef-4d68-4fdc-8b0a-8c3c97d5693b.png)
![image](https://user-images.githubusercontent.com/107028314/206202266-40d43845-a5cd-4941-ba22-048d87c835de.png)

* Result pages

![image](https://user-images.githubusercontent.com/107028314/206202560-b6ce9f06-7e91-45ae-9dc8-e2d47ebf0182.png)
![image](https://user-images.githubusercontent.com/107028314/206202601-464bf845-0a0a-4e9b-975e-77afb4e7d1c2.png)

## Installation
Here are the modules used in the code. Please install if you do not have them.
* tkinter
* PIL
* requests
* matplotlib
* pandas
* numpy
* re
* beautifulsoup
* urlopen

## Usage
1. Open the main.py file in Anaconda and run it.
2. Rank the importance of each feature and click the `Next Step` (1 for the most Important). Please do not select duplicated numbers on the same page, or an error message will pop out.
3. Select the climate preference.
4. Click the `Click to View Climate Data` to view the yearly temperature trend and monthly precipitation trend.
5. Click `restart` to retake the survey.
6. Click `exit` to exit the program.

## Data Source
1. Climate: https://www.ncei.noaa.gov/pub/data/normals/1981-2010/source-datasets/
2. Education attainment: https://data.census.gov/cedsci/table?q=S1501&g=0100000US%240400000&tid=ACSST1Y2021.S1501&moe=false
3. Income: https://fred.stlouisfed.org/release/tables?rid=110&eid=257197#snid=257202
4. Consumer spending: https://www.bea.gov/data/consumer-spending/state
5. Living environment: https://www.mphonline.org/green-states/
6. Crime rate: https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_violent_crime_rate

## Author
* Elena Hung: wanpingh 
* Xingyao Xie: xingyaox 
* Selina Tseng: johsuant
* Kaia Chen: wangyuac 
* Chenghao Huang: chuang5

## Video
https://www.youtube.com/watch?v=r0XzIsJ7ASY
