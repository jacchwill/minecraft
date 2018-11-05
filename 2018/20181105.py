
# coding: utf-8

# In[2]:

from mcpi.minecraft import Minecraft
import time

#ip
ip="192.168.1.12"

#name of player
name='chocolatepowder'

#連線ip
mc = Minecraft.create(ip)

#跑5次
for w in range(0,5):
    #說Hello
    mc.postToChat('Hello')
    #停1秒
    time.sleep(1)


# In[ ]:



