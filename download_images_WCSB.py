import requests, os, sys

mydir = 'C:/Users/rgjb/Desktop/Atlases/WSCB_Images'
os.chdir = mydir

url = 'https://ags.aer.ca/image-content/'

l = list(range(1,51))
sl = [str(i) for i in l]
slz =  ["0" + s if len(s) <= 1 else s for s in sl]

    
for num in range(15,27):
    for x in slz:
        image = "fg"+str(num)+"_"+x
        res = requests.get(url+image+".jfif")
            
        if res.status_code is not 200:
            print(res.status_code)
            #break
        elif res.status_code is 200:
            file = open(mydir + "/" + image + ".jpg", "wb")
            file.write(res.content)
            file.close()                    
            
          

    
    
