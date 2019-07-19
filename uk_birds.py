"""
This is a mini study of UK woodland bird data I have set up to practice some of the skills I have learnt in data processing and analysis. I chose a small dataset I got in .csv format of the UK goverment website to make it more readable and manageable on Sololearn.

Hope you like the code. Any tips, comments or general feedback are welcome.

Thanks, 
Rob
"""

#Import libraries
import re
import statistics

#First open the file and save it to a variable
bird_csv = "Long term change (1970-2014),Short term change (2009-2014)|Species,Long term percentage change,Annual percentage change,Trend,Short term percentage change,Annual percentage change,Trend|Blackcap (Sylvia atricapilla),297,3.18,strong increase,40,6.93,strong increase|Chiffchaff (Phylloscopus collybita),93,1.51,weak increase,22,4.13,strong increase|Coal Tit (Periparus ater),19,0.4,no change,-10,-2.14,weak decline|Garden Warbler (Sylvia borin),-5,-0.12,no change,-9,-1.94,weak decline|Goldcrest (Regulus regulus),-21,-0.53,no change,0,0.09,no change|Great Spotted Woodpecker (Dendrocopos major),361,3.53,strong increase,-1,-0.27,no change|Green Woodpecker (Picus viridis),101,1.6,weak increase,-8,-1.7,weak decline|Jay (Garrulus glandarius),14,0.29,no change,9,1.78,weak increase|Lesser Spotted Woodpecker (Dendrocopos minor),-83,-3.98,strong decline,-44,-11.08,strong decline|Marsh Tit (Poecile palustris),-72,-2.83,strong decline,-12,-2.5,weak decline|Nightingale (Luscinia megarhynchos),(1995-2014) -40,-2.62,weak decline,28,5.04,strong increase|Nuthatch (Sitta europaea),257,2.94,strong increase,15,2.91,strong increase|Lesser Redpoll (Carduelis cabaret),-86,-4.33,strong decline,14,2.58,weak increase|Redstart (Phoenicurus phoenicurus),70,1.21,weak increase,35,6.2,strong increase|Sparrowhawk (Accipiter nisus),93,1.51,weak increase,-5,-1.11,no change|Spotted Flycatcher (Muscicapa striata),-87,-4.45,strong decline,6,1.15,weak increase|Tree Pipit (Anthus trivialis),-67,-2.5,weak decline,28,4.98,strong increase|Treecreeper (Certhia familiaris),-12,-0.29,no change,11,2.03,weak increase|Willow Tit (Poecile montana),-93,-5.73,strong decline,-7,-1.46,weak decline|Willow Warbler (Phylloscopus trochilus),-42,-1.22,weak decline,-7,-1.41,weak decline|Pied Flycatcher     (Ficedula hypoleuca),(1995-2014) -46,-3.15,strong decline,15,2.77,weak increase|Wood Warbler (Phylloscopus sibilatrix),(1995-2014) -55,-4.07,strong decline,13,2.43,weak increase|Common Crossbill (Loxia curvirostra),(1995-2014) 8,0.38,no change,-22,-4.94,strong decline|Siskin (Carduelis spinus),(1995-2014) 53,2.26,weak increase,-2,-0.49,no change|Capercaillie (Tetrao urogallus),-89,-4.94,strong decline,-11,-2.38,weak decline"

print("First we will take a quick look at the first few lines in the data.\n")

#Then split string along the "|" character to create a list of strings which each representing rows in a table
list_split = list(bird_csv.split("|"))
print("Each string is a row: ")
print(list_split[:5])
print("")

#Then remove the first row since this is just information about the dataset
info = list_split[0]
list_split = list_split[1:]

#Next iterate over each string and split along the "," to create a list of strings with each list representing a row in a table and each string representing a column
datalist = []
for item in list_split :
    i = str(item)
    split = list(i.split(","))
    datalist.append(split)

print("Each list is a row, each string is a column: ")    
print(datalist[:5])
print("")

#Then save the header and separate it from the rest of the data
header = datalist[0]
data = datalist[1:]

#This is only a tiny dataset but we should still know how many entries there are
bird_count = len(data)
print(f"Number of entries: {bird_count}\n")

print("""First we should investigate how the woodland bird species are doing in the long term by calculating the mean percentage of the long term and long term annual trends.\n """)

#First we isolate the column for Long term percentage change
longterm_chg = [row[1] for row in data]

#Before we calculate the mean we need to remove '(1995-2014)' from the column if it is different from the rest of the data to leave only the % values. We will use regular expression to remove it but we must combine the list into a string first
s_join = ", ".join(longterm_chg)
reg = re.sub('\(1995-2014\) ', '', s_join)

#Then split the string into a list of strings and convert them into floats
longterm_re = list(reg.split(","))
longterm_re = [float(i) for i in longterm_re]
print("After year data removed from column: ")
print(longterm_re)
print("")

#Now use sum() on the list of floats to calculate the mean
longterm_mean = int(sum(longterm_re)) / bird_count 
print(f"The mean long term percentage change is {longterm_mean}%\n")

print("""Looking at the data, there seem to be some very high positive values which may give a misleading result. We will check the median to see what results we get back.\n""")

#We will sort this list into numerical order and use the statistics.median() method to easily calculate the median
longterm_sort = sorted(longterm_re)
longterm_median = statistics.median(longterm_sort)
print(f"The median long term percentage change is {longterm_median}%\n")

print("""These two 'average' calculations give quite different results so we could check what percentage of birds surveyed in the data are increasing versus those that are in decline.\n""")

#Now check the number the longterm trends for each bird and count how many times each entry appears
longtrend = [row[3] for row in data]
longtrend_count = {}
for trend in longtrend:
    if trend not in longtrend_count:
        longtrend_count[trend] = 1
    else:
        longtrend_count[trend] += 1

#We can then iterate over the dictionary and turn the values into a percentage
longtrend_pct = {}
for key, value in longtrend_count.items():
    longtrend_pct[key] = str(round((value / bird_count) * 100, 2)) + "%"

print(f"Long term trend percentage of UK woodland birds: \n{longtrend_pct}\n")

print("""Overall this shows that in the long term, 32% of woodland birds have increased, whilst 44% have declined. It would be interesting to see how this compares to the long term annual data or the short term data.\n
We shall first compare the long term annual percentage change.\n""")

#First we isolate the column for (Long term)  Annual percentage change, convert from strings to floats and use sum() on the list to calculate the mean
long_annual = [row[2] for row in data] 
long_annual = [float(i) for i in long_annual]
longannual_mean = int(sum(long_annual)) / bird_count 
print(f"The mean long term annual percentage change is {longannual_mean}%\n")

#Then sort the list and use the statistics.median() method
longannual_sort = sorted(long_annual)
longannual_median = statistics.median(longannual_sort)
print(f"The median long term annual percentage change is {longannual_median}%\n")

print("""These results show that overall woodland bird species declined by an average <1% every year between 1970-2014, backing up the results from the long term trends.\n
We will do the same analysis for the short term percentage change, short term annual percentage change, and the short term trend percentage.\n""")

#Repeat for the short term percentage change
short_chg = [row[4] for row in data] 
short_chg = [float(i) for i in short_chg]
short_mean = int(sum(short_chg)) / bird_count 
print(f"The mean short term percentage change is {short_mean}%\n")

short_sort = sorted(short_chg)
short_median = statistics.median(short_sort)
print(f"The median short term percentage change is {short_median}%\n")

#Now repeat for the short term annual percentage change
short_annual = [row[5] for row in data] 
short_annual = [float(i) for i in short_annual]
shortannual_mean = int(sum(short_annual)) / bird_count 
print(f"The mean short term annual percentage change is {shortannual_mean}%\n")

shortannual_sort = sorted(short_annual)
shortannual_median = statistics.median(shortannual_sort)
print(f"The median short term annual percentage change is {shortannual_median}%\n")


#Now check the number the short term trends for each bird and count how many times each entry appears
short_trend = [row[6] for row in data]
short_count = {}
for trend in short_trend:
    if trend not in short_count:
        short_count[trend] = 1
    else:
        short_count[trend] += 1

#We can then iterate over the dictionary and turn the values into a percentage
short_trend_pct = {}
for key, value in short_count.items():
    short_trend_pct[key] = str(round((value / bird_count) * 100, 2)) + "%"

print(f"Short term trend percentage of UK woodland birds: \n{short_trend_pct}\n")

print("""The short term percentage change on average shows positive or no change, the short term annual change shows <1% increase on average, whilst the short term trends show 48% of species are increasing versus 36% in decline.\n
Together these data indicate that overall between 1995-2014 there has been a signicant recovery in populations of woodland bird species in the UK. From here would could get more data on the bird species in this study, birds from other habitats, the birds food sources, climate, conservation projects, and more to get more insights into how and why these changes have occurred.\n
+++++ END +++++
If you have read down this far, thanks for reading :)""")
