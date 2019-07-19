"""
A simple code made whilst playing around around with the file and urllib modules. 
It simply downloads data from a webpage and writes it to a text file.
"""

from urllib.request import urlopen, Request

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

req = Request('https://www.w3.org/TR/PNG/iso_8859-1.txt', headers = headers)

res = urlopen(req)

data = res.read() 

myfile = open('sample.txt', 'wb+')
myfile.write(data)
myfile.seek(0)
print(myfile.read(100))
myfile.close()
