import mcpi.minecraft as minecraft
import mcpi.block as block
import random

# connect to Minecraft
mc = minecraft.Minecraft.create()

# define village size and location
x, y, z=(76.681, 63.0, 316.756)


mc.setBlocks(x-50,y-50,z-50, x+50,y+50,z+50, block.AIR)
