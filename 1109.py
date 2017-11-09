import json

house=[]

s=[1,1,1,1,
   1,1,1,1,
   1,1,1,1,
   1,1,1,1]


house.append(s) 
house.append(s) 
house.append(s) 
house.append(s) 

f=open("tower.txt","w")
json.dump(house,f)
f.close()

