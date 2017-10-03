from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

class mic:

    x=0
    y=0
    z=0
    u=1

    def usid(self):
        t=mc.getPlayerEntityIds()
        print t
    
    def uspos(self,wkj):
        self.x,self.y,self.z = mc.entity.getPos(wkj)
        print self.x,self.y,self.z

    def wdfe(self,item):
        mc.setBlock(self.x,self.y,self.z, item)
    
    def tnt(self,item):
        mc.setBlock(self.x,self.y,self.z, item,1)
     
s=mic()
s.usid()

#s.uspos(57369)

s.uspos(1)
s.wdfe(46)
#s.uspos(20514)

