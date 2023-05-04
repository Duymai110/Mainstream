from mcpi.minecraft import Minecraft
from mcpi import block
import random
mc=Minecraft.create()

#house dimension
width = random.randint(10, 20)
length = random.randint(10, 20)
height = random.randint(5, 10)



x,y,z = mc.getPos


mc.setBlocks(x,y,z, x+20,y+20,z+20, block.AIR)

def divideroom():
    
    mc.setBlocks(x, y, z, x + width, y, z + length, block.WOOD_PLANKS)
    dw= random.randint(5, width - 5)
    mc.setBlocks(x+ dw ,y ,z , x + dw,y ,z+length , block.SANDSTONE)
    

divideroom()