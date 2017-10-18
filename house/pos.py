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
        



            
s=mic()
s.playerid('willpi')
s.playerpos()
