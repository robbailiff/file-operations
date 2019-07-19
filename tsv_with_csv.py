"""
I came across .tsv (tab separated value) files whilst trying to find a dataset for a mini-project. 
This file type was new to me and has taken a bit of time to work out how to parse them correctly.

In this code, I have downloaded the data from a web page, saved it as a file object and parsed it using csv_reader.

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
data = data[:400]

print("Pre-parsed data: \n")
print(data[:200])
print("=" * 30 + "\n")

# Create a new file in write+ mode and write the data to it. Then return the file pointer to position zero ready to by read by the csv reader
tsvfile = open('data.tsv', 'w+')
tsvfile.write(data)
tsvfile.seek(0)

# Create empty list to append values to
data_list = []

# Parse the file object line by line to create a list of lists, with the main list representing a table, and each nested list representing a column in the table
for line in csv.reader(tsvfile, dialect="excel-tab"):
    if line:
        data_list.append(line)

print("Parsed data: \n") 
print(data_list[:100])

# Remember to close the file
tsvfile.close()
