"""
I came across .tsv (tab separated value) files whilst trying to find a dataset for a mini-project. 
This file type was new to me and has taken a bit of time to work out how to parse them correctly.

It turns out, that you can feed "any object which supports the iterator protocol and returns a string each time its __next__() method is called" into csv_reader(). 
This includes things like lists, so in this code I have used split() on the string data saved from a web page and parsed it using csv_reader.

Hope you like the code. Any tips, comments or general feedback are welcome.

Thanks, 
Rob

+++++++++++++++++++++++++++++++++++++++++
CSV Module Documentation: https://docs.python.org/2/library/csv.html

"""

import csv
from urllib.request import urlopen, Request

link = "https://www.dropbox.com/s/shsvqzbe5c6ncbr/livermore1a.txt?dl=1"

# Download the data
req = Request(link)
res = urlopen(req)

# This dataset contains special characters not recognised by unicode so we need to decode to latin-1
data = res.read().decode('latin-1')
data = data[:500]
# We then split the string along the carriage returns to create a list that can be fed into csv_reader()
datafile = data.split('\r\n')

print("Pre-parsed data: \n")
print(datafile[:200])
print("=" * 30 + "\n")

# Create empty list to append values to
data_list = []

# Parse the list line by line to create a list of lists, with the main list representing a table, and each nested list representing a column in the table
for line in csv.reader(datafile, dialect="excel-tab", ):
    if line:
        data_list.append(line)
        
print("Parsed data: \n")    
print(data_list[:100])
