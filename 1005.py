from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

class mic:

    x=0
    y=0
    z=0
    u=1

    def playerid(self):
        t=mc.getPlayerEntityIds()
        print t
    
    def playerpos(self,wkj):
        self.x,self.y,self.z = mc.entity.getPos(wkj)
        print self.x,self.y,self.z

    def wdfe(self,item):
        mc.setBlock(self.x,self.y,self.z, item)

    def setfloor(self,item,width,deep):
        for erf in range(0,width):
            for wdz in range(0,deep):
                print erf,wdz
                mc.setBlock(self.x+erf,self.y,self.z+wdz, item)
                
s=mic()
s.playerid()
s.playerpos(761732)
s.setfloor(2,12,5)

        
