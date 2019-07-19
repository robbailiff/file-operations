import csv

f = open("guns.csv", "r")

data = list(csv.reader(f))

data[:5]

[['',
  'year',
  'month',
  'intent',
  'police',
  'sex',
  'age',
  'race',
  'hispanic',
  'place',
  'education'],
 ['1',
  '2012',
  '01',
  'Suicide',
  '0',
  'M',
  '34',
  'Asian/Pacific Islander',
  '100',
  'Home',
  '4'],
 ['2', '2012', '01', 'Suicide', '0', 'F', '21', 'White', '100', 'Street', '3'],
 ['3',
  '2012',
  '01',
  'Suicide',
  '0',
  'M',
  '60',
  'White',
  '100',
  'Other specified',
  '4'],
 ['4', '2012', '02', 'Suicide', '0', 'M', '64', 'White', '100', 'Home', '4']]

headers = data[0]

headers

['',
 'year',
 'month',
 'intent',
 'police',
 'sex',
 'age',
 'race',
 'hispanic',
 'place',
 'education']

data = data[1:]

data[:5]

[['1',
  '2012',
  '01',
  'Suicide',
  '0',
  'M',
  '34',
  'Asian/Pacific Islander',
  '100',
  'Home',
  '4'],
 ['2', '2012', '01', 'Suicide', '0', 'F', '21', 'White', '100', 'Street', '3'],
 ['3',
  '2012',
  '01',
  'Suicide',
  '0',
  'M',
  '60',
  'White',
  '100',
  'Other specified',
  '4'],
 ['4', '2012', '02', 'Suicide', '0', 'M', '64', 'White', '100', 'Home', '4'],
 ['5',
  '2012',
  '02',
  'Suicide',
  '0',
  'M',
  '31',
  'White',
  '100',
  'Other specified',
  '2']]

years = [row[1] for row in data]

year_count = {}

for year in years:

    if year not in year_count:

        year_count[year] = 1

    else:

        year_count[year] += 1

​

print(year_count)

{'2014': 33599, '2013': 33636, '2012': 33563}

import datetime

dates = [datetime.datetime(year = int(row[1]), month = int(row[2]), day = 1) for row in data]

dates[:5]

[datetime.datetime(2012, 1, 1, 0, 0),
 datetime.datetime(2012, 1, 1, 0, 0),
 datetime.datetime(2012, 1, 1, 0, 0),
 datetime.datetime(2012, 2, 1, 0, 0),
 datetime.datetime(2012, 2, 1, 0, 0)]

date_count = {}

for date in dates:

    if date not in date_count:

        date_count[date] = 1

    else:

        date_count[date] += 1

        

date_count

{datetime.datetime(2012, 1, 1, 0, 0): 2758,
 datetime.datetime(2012, 2, 1, 0, 0): 2357,
 datetime.datetime(2012, 3, 1, 0, 0): 2743,
 datetime.datetime(2012, 4, 1, 0, 0): 2795,
 datetime.datetime(2012, 5, 1, 0, 0): 2999,
 datetime.datetime(2012, 6, 1, 0, 0): 2826,
 datetime.datetime(2012, 7, 1, 0, 0): 3026,
 datetime.datetime(2012, 8, 1, 0, 0): 2954,
 datetime.datetime(2012, 9, 1, 0, 0): 2852,
 datetime.datetime(2012, 10, 1, 0, 0): 2733,
 datetime.datetime(2012, 11, 1, 0, 0): 2729,
 datetime.datetime(2012, 12, 1, 0, 0): 2791,
 datetime.datetime(2013, 1, 1, 0, 0): 2864,
 datetime.datetime(2013, 2, 1, 0, 0): 2375,
 datetime.datetime(2013, 3, 1, 0, 0): 2862,
 datetime.datetime(2013, 4, 1, 0, 0): 2798,
 datetime.datetime(2013, 5, 1, 0, 0): 2806,
 datetime.datetime(2013, 6, 1, 0, 0): 2920,
 datetime.datetime(2013, 7, 1, 0, 0): 3079,
 datetime.datetime(2013, 8, 1, 0, 0): 2859,
 datetime.datetime(2013, 9, 1, 0, 0): 2742,
 datetime.datetime(2013, 10, 1, 0, 0): 2808,
 datetime.datetime(2013, 11, 1, 0, 0): 2758,
 datetime.datetime(2013, 12, 1, 0, 0): 2765,
 datetime.datetime(2014, 1, 1, 0, 0): 2651,
 datetime.datetime(2014, 2, 1, 0, 0): 2361,
 datetime.datetime(2014, 3, 1, 0, 0): 2684,
 datetime.datetime(2014, 4, 1, 0, 0): 2862,
 datetime.datetime(2014, 5, 1, 0, 0): 2864,
 datetime.datetime(2014, 6, 1, 0, 0): 2931,
 datetime.datetime(2014, 7, 1, 0, 0): 2884,
 datetime.datetime(2014, 8, 1, 0, 0): 2970,
 datetime.datetime(2014, 9, 1, 0, 0): 2914,
 datetime.datetime(2014, 10, 1, 0, 0): 2865,
 datetime.datetime(2014, 11, 1, 0, 0): 2756,
 datetime.datetime(2014, 12, 1, 0, 0): 2857}

sex = [row[5] for row in data]

sex_count = {}

for gender in sex:

    if gender not in sex_count:

        sex_count[gender] = 1

    else:

        sex_count[gender] += 1

​

sex_count

{'F': 14449, 'M': 86349}

races = [row[7] for row in data]

race_count = {}

for race in races:

    if race not in race_count:

        race_count[race] = 1

    else:

        race_count[race] += 1

​

race_count

{'Asian/Pacific Islander': 1326,
 'Black': 23296,
 'Hispanic': 9022,
 'Native American/Native Alaskan': 917,
 'White': 66237}

#So far I have opened and read the file, and then saved and removed the header. 
#I have also converted the the year and month columns into a datetime format using a list comprehension.
# Then counted how many times each date appears in the dataset. 
#I have done the same for the year, sex and race columns. 
#So far it seems that although the number of incidents is consistent from year to year, most of them involve men who are white. 
#The number of black people involved in gun crime seems high relative to the % of the overall population.
# So the links between % gun crime and % population should be examined further. 
#It would also be interesting to examine the 'intent' relative to race,a nd also relative to education to see if there is a link.

file = open("census.csv", "r")

census = list(csv.reader(file))

census

[['Id',
  'Year',
  'Id',
  'Sex',
  'Id',
  'Hispanic Origin',
  'Id',
  'Id2',
  'Geography',
  'Total',
  'Race Alone - White',
  'Race Alone - Hispanic',
  'Race Alone - Black or African American',
  'Race Alone - American Indian and Alaska Native',
  'Race Alone - Asian',
  'Race Alone - Native Hawaiian and Other Pacific Islander',
  'Two or More Races'],
 ['cen42010',
  'April 1, 2010 Census',
  'totsex',
  'Both Sexes',
  'tothisp',
  'Total',
  '0100000US',
  '',
  'United States',
  '308745538',
  '197318956',
  '44618105',
  '40250635',
  '3739506',
  '15159516',
  '674625',
  '6984195']]

mapping = {

    'Asian/Pacific Islander': 15159516 + 674625,

    'Black': 40250635,

    'Native American/Native Alaskan': 3739506,

    'Hispanic': 44618105,

    'White': 197318956

}

race_per_hundredk = {}

for key, value in race_count.items():

    race_per_hundredk[key] = (value / mapping[key]) * 100000

    

race_per_hundredk    

{'Asian/Pacific Islander': 8.374309664161762,
 'Black': 57.8773477735196,
 'Hispanic': 20.220491210910907,
 'Native American/Native Alaskan': 24.521955573811088,
 'White': 33.56849303419181}

#We can filter our results, and restrict them to the Homicide intent. 
#This will tell us what the gun-related murder rate per 100000 people in each racial category is. 
#In order to do this, we'll need to redo our work in generating race_counts, but only count rows where the intent was Homicide.

intents = [row[3] for row in data]

races = [row[7] for row in data]

homicide_race_counts = {}

for i, race in enumerate(races):

    if intents[i] == 'Homicide':

        if race not in homicide_race_counts:

            homicide_race_counts[race] = 1

        else:

            homicide_race_counts[race] += 1

            

homicide_race_counts

{'Asian/Pacific Islander': 559,
 'Black': 19510,
 'Hispanic': 5634,
 'Native American/Native Alaskan': 326,
 'White': 9147}

homicide_per_hundredk = {}

for key, value in homicide_race_counts.items():

    homicide_per_hundredk[key] = (value / mapping[key]) * 100000

    

homicide_per_hundredk  

{'Asian/Pacific Islander': 3.530346230970155,
 'Black': 48.471284987180944,
 'Hispanic': 12.627161104219914,
 'Native American/Native Alaskan': 8.717729026240365,
 'White': 4.6356417981453335}

#This data shows overwhelmingly that black people are responsible for the highest rates of homicide per 100000 people.
#The next step would be to find out why this is the case. 
#Investigating education, poverty, job availabilty, drug and alcohol abuse, and criminal activity may reveal why this is the case.

#Further things to investigate with current dataset:

    #Figure out the link, if any, between month and homicide rate.
    #Explore the homicide rate by gender.
    #Explore the rates of other intents, like Accidental, by gender and race.
    #Find out if gun death rates correlate to location and education.

