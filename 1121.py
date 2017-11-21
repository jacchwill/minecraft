import json,math

house=[]

s=[1,1,1,1,
   1,1,1,1,
   1,1,1,1,
   1,1,1,1]


house.append(s)

s=[1,1,1,1,
   1,0,0,1,
   1,0,0,1,
   1,1,1,1]

house.append(s) 
house.append(s) 
house.append(s) 

f=open("tower.txt","w")
json.dump(house,f)
f.close()


from mcpi.minecraft import Minecraft

import time
mc = Minecraft.create()

class mic:
    
    def setpostion(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def staeo(self,dvd):
        q=len(dvd)
        print q
        h=len(dvd[0])
        
        he=math.sqrt(h)
        print he
        he=int(he)
        for d in range(0,q):
            #print d
            #print dvd[d]
            i=0
            for s in range(0,he):
                for k in range(0,he):
                    mc.setBlock(self.x+s,self.y+d,self.z+k,dvd[d][i])
                    i=i+1
m=mic()
m.setpostion(-18,7,-20)
m.staeo(house)
