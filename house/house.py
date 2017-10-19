from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create("192.168.1.113")

class mic:

    x=0
    y=0
    z=0
    u=1

    def playerid(self,n):
        self.u=mc.getPlayerEntityId(n)
        print self.u 
    
    def playerpos(self):
        x,y,z = mc.entity.getPos(self.u)
        print x,y,z
        
    def pos(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def setfloor(self,item,width,deep):
        for erf in range(0,width):
            for wdz in range(0,deep):
                print erf,wdz
                mc.setBlock(self.x+erf,self.y,self.z+wdz, item)

    def cube(self,item):
        mc.setBlock(self.x,self.y,self.z, item)

    def build(self,item,f):
        for s in range(0,10):
            for a in range(0,10):
                mc.setBlock(self.x+a,self.y+f,self.z+s, item)
                sleep(0.1)
        
    def build1(self,item,f):
        n=0
        for q in range(0,10):
            for s in range(0,10):
                print item[n]
                mc.setBlock(self.x+s,self.y+f,self.z+q, item[n])
                n=n+1
                #for a in range(0,10):
                #mc.setBlock(self.x+a,self.y+f,self.z+s, item)
                #sleep(0.1)
       


            
s=mic()
s.playerid('willpi')
s.playerpos()
s.pos(-7.66340642264,5.0,136.334840483) 
s.build(155,-1)

f=[
    155,155,0,0,155,155,155,155,155,155,
    102,0,0,0,0,0,0,0,0,155,
    165,0,0,0,0,0,0,0,0,155,
    157,0,0,0,0,0,0,0,0,155,
    155,0,0,0,0,0,0,0,0,155,
    155,0,0,0,0,0,0,0,0,155,
    155,0,0,0,0,0,0,0,0,155,
    33,0,0,0,0,0,0,0,0,155,
    155,0,0,0,0,0,0,0,0,155,
    29,155,155,155,155,155,155,155,155,155
    
   ]
s.build1(f,0)
s.build1(f,1)
s.build1(f,2)
s.build1(f,3)
s.build1(f,4)
s.build1(f,5)
       
f=[
    155,155,0,0,155,155,155,155,155,155,
    29,155,155,155,155,155,155,155,155,155,
    29,155,155,155,155,155,155,155,155,155,
    29,155,155,155,155,155,155,155,155,155,
    29,155,155,155,155,155,155,155,155,155,
    29,155,155,155,155,155,155,155,155,155,
    29,155,155,155,155,155,155,155,155,155,
    29,155,155,155,155,155,155,155,155,155,
    29,155,155,155,155,155,155,155,155,155,
    29,155,155,155,155,155,155,155,155,155 
   ]
s.build1(f,6)
