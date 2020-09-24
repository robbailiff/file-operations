import requests, os, sys

mydir = 'C:/Users/rgjb/Desktop/Atlases/GS_Aus_Images'
os.chdir = mydir

url = 'http://www.ga.gov.au/static/palaeo/timeslice/images/'

l = list(range(1,12))
sl = [str(i) for i in l]
#slz =  ["0" + s if len(s) <= 1 else s for s in sl]
periods = ['permian','triassic','jurassic','cretaceous','cenozoic']

    
for p in periods:
    for x in sl:
        image = p + "_" + x
        res = requests.get(url+image+".gif")
            
        if res.status_code is not 200:
            print(res.status_code)
            #break
        elif res.status_code is 200:
            file = open(mydir + "/" + image + ".jpg", "wb")
            file.write(res.content)
            file.close()                    
            
          

    
    