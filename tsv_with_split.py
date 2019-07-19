"""
I came across .tsv (tab separated value) files whilst trying to find a dataset for a mini-project. 
This file type was new to me and has taken a bit of time to work out how to parse them correctly.

In this code, I have downloaded the data from a web page, saved it as a string object and manually parsed it using string methods and for loops. 
At the time I didn't realise I could use csv_reader to parse non .csv files, which is much easier it turns out.

Hope you like the code. Any tips, comments or general feedback are welcome.

Thanks, 
Rob

+++++++++++++++++++++++++++++++++++++++++
CSV Module Documentation: https://docs.python.org/2/library/csv.html

"""

import csv
from urllib.request import urlopen, Request

link = "https://www.dropbox.com/s/shsvqzbe5c6ncbr/livermore1a.txt?dl=1"

# Download the data from the link
req = Request(link)
res = urlopen(req)

# This dataset contains special characters not recognised by unicode so we need to decode to latin-1
data = res.read().decode('latin-1')

print("Raw data: \n")
print(data[:200] + '\n')
print("Data type: " + str(type(data)) + "\n")
print("=" * 30 + "\n")

# Each entry is enclosed in double quotes, which need to be removed
quote_data = data.replace('"', '')

print("Data with double quotes removed: \n")
print(quote_data[:200] + '\n')
print("Data type: " + str(type(quote_data)) + "\n")
print("=" * 30 + "\n")

# Each row ends with a carriage return so we use split() to split the one long string representing the entire table into multiple strings in a list, each representing a row
return_data = quote_data.split('\r\n')

print("Data split along carriage returns: \n")
print(str(return_data[:2]) + '\n')
print("Data type: " + str(type(return_data)) + "\n")
print("=" * 30 + "\n")

# Create empty list to append values to
data_list = []

# Iterate the list line by line and split each string at the tab character '\t' to create a list of lists, with the main list representing a table, and each nested list representing a column in the table
for row in return_data:
    i = row.split('\t')
    data_list.append(i)

print("Data split along tabs: \n")
print(str(data_list[:2]) + '\n')
print("Data type: " + str(type(data_list)) + "\n")
