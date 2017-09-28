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
        water = 11
        mc.setBlock(self.x,self.y,self.z, water)

    def wdfe(self,item):
        mc.setBlock(self.x,self.y,self.z, item)
        
    def wdfe_x(self,item,wdsx):
        for erd in range(0,wdsx):
            mc.setBlock(self.x+erd,self.y,self.z, item)

    def wdfe_y(self,item,wsdz):
        for eru in range(0,wdsz):
            mc.setBlock(self.x,self.y+eru,self.z, item)
        
    def wdfe_z(self,item,wda):
        for sru in range(0,wda):
            mc.setBlock(self.x,self.y,self.z-wda, item)
        
        
i=mic()
i.pos()
i.wdfe(11)
i.wdfe_z(0,10)

