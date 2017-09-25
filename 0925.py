from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

class mic:

    x=0
    y=0
    z=0
    
    def pos(self):
        self.x,self.y,self.z = mc.player.getPos()
        print self.x
        print self.y
        print self.z

    def rfg(self):
        water = 8
        mc.setBlock(self.x,self.y,self.z, water)
        
        
        
i=mic()
i.pos()
i.rfg()
