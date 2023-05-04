from mcpi.minecraft import Minecraft
from mcpi import block
import random

mc = Minecraft.create()

# Define the initial room dimensions
width = random.randint(8, 12)
length = random.randint(8, 12)
height = 5


# Define the starting coordinates
def Starting_coordinates():
    
    x, y, z = mc.player.getPos()
    z = int(z + 4)
    x = int(x + 4)
    y=int(y)
    return x,y,z

def Add_roof(x, y, z, width, length, height):
    mc.setBlocks(x, y + height, z, x + width, y + height, z + length, block.WOOD_PLANKS)
    axis = random.randint(0, 1)    
    if axis == 0:
        mc.setBlocks()
    else:
        mc.setBlocks()

def Split_room_Add_door_Add_window(x, y, z, width, length, height, depth):
    
    # Stop splitting if the room has been split 3 times
    if depth == 0:
        return
    
    # Choose a random axis to split the room on (x=0, z=1)
    axis = random.randint(0, 1)
    side = random.randint(0, 1)

    if axis == 0 and width >= 8:
        # Split the room on the x axis
        split = random.randint(width // 2 - 1, width // 2 + 1)

        # Build the dividing wall
        mc.setBlocks(x + split, y, z, x + split, y + height, z + length, block.WOOD_PLANKS.withData(2))
        
        # Add a door to at ramdom to the dividing wall
        if side == 0:
            doorpos = random.randint(1,3)
        else:
            doorpos = random.randint(length - 3,length - 2)
        mc.setBlock(x + split , y + 2, z+doorpos, block.DOOR_WOOD.withData(8))
        mc.setBlock(x + split , y + 1, z+doorpos, block.DOOR_WOOD.withData(0))
        
        # Add windows to the outer walls
        window_pos = random.randint(1, 3)
        
        mc.setBlocks(x - 1, y + 2, z + window_pos, x - 1, y + 3, z + window_pos, block.STAINED_GLASS)
        mc.setBlock(x - 2, y + 1, z + window_pos, block.DIRT)
        mc.setBlock(x - 2, y + 1, z + window_pos + 1, block.SIGN_WALL.withData(3))
        mc.setBlock(x - 2, y + 1, z + window_pos - 1, block.SIGN_WALL)
        mc.setBlock(x - 3, y + 1, z + window_pos, block.SIGN_WALL.withData(4))
        mc.setBlock(x - 2, y + 2, z + window_pos, block.FLOWER_YELLOW)
        
        mc.setBlocks(x + width + 1, y + 2, z + window_pos, x + width + 1, y + 3, z + window_pos, block.STAINED_GLASS)
        mc.setBlock(x + width + 2, y + 1, z + window_pos, block.DIRT)
        mc.setBlock(x + width + 2, y + 1, z + window_pos + 1, block.SIGN_WALL.withData(3))
        mc.setBlock(x + width + 2, y + 1, z + window_pos - 1, block.SIGN_WALL)
        mc.setBlock(x + width + 3, y + 1, z + window_pos, block.SIGN_WALL.withData(4))
        mc.setBlock(x + width + 2, y + 2, z + window_pos, block.FLOWER_CYAN)
        # Recursively split the two resulting parts
        Split_room_Add_door_Add_window(x, y, z, split, length, height, depth - 1)
        Split_room_Add_door_Add_window(x + split, y, z, width - split, length, height, depth - 1)

    elif axis == 1 and length >= 8:
        # Split the room on the z axis
        split = random.randint(length // 2 - 1, length // 2 + 1)

        # Build the dividing wall
        mc.setBlocks(x, y, z + split, x + width, y + height, z + split, block.WOOD_PLANKS.withData(2))

        # Add a door to the dividing wall
        if side == 0:
            doorpos = random.randint(1,3)
        else:
            doorpos = random.randint(width - 3,width - 2)
        mc.setBlock(x+doorpos , y + 2, z + split, block.DOOR_WOOD.withData(8))
        mc.setBlock(x+doorpos , y + 1, z + split, block.DOOR_WOOD.withData(0))
        
        # Add a window to the outer wall
        window_pos = random.randint(1, 3)
        mc.setBlocks(x + window_pos, y + 2, z - 1, x + window_pos, y + 3, z - 1 , block.STAINED_GLASS)
        
        mc.setBlocks(x + window_pos, y + 2, z+ length + 1, x + window_pos, y + 3, z + length + 1 , block.STAINED_GLASS)
        # Recursively split the two resulting parts
        Split_room_Add_door_Add_window(x, y, z, width, split, height, depth - 1)
        Split_room_Add_door_Add_window(x, y, z + split, width, length - split, height, depth - 1)

def Build_house():
    global x, y, z, width, length, height
    # Build the initial room
    mc.setBlocks(x - 1, y, z - 1, x + width + 1, y + height, z + length + 1, block.STONE_BRICK)
    mc.setBlocks(x, y, z, x + width, y + height, z + length, block.AIR)  # fill up air inside room

    mc.setBlocks(x, y, z, x + width, y, z + length, block.WOOD_PLANKS)

    # Add a door to the house
    side = random.randint(0, 1)

    if side == 0:
        doorpos = random.randrange(1,2)
    else:
        doorpos = random.randrange(width - 3,width - 2)
    # back door    
    mc.setBlock(x + width + 1 , y + 2, z + doorpos-1, block.DOOR_WOOD.withData(8))
    mc.setBlock(x + width + 1 , y + 1, z + doorpos-1, block.DOOR_WOOD.withData(0))
    # front door
    mc.setBlock(x-1 , y + 2, z + doorpos-1, block.DOOR_WOOD.withData(8))
    mc.setBlock(x-1 , y + 1, z + doorpos-1, block.DOOR_WOOD.withData(0))

    # Add light
    for i in range(x, x + width, 3):
        for t in range(z, z + length, 3):
            mc.setBlock(i, y, t, block.GLOWSTONE_BLOCK)

    

    
    
def Add_bookshelf(x, y, z, width, length, height, count):
    # Add books
    while True:
        if count == 0:
            return
        x1 = random.randrange(x+1,x + width)
        if mc.getBlock(x1, y + 1, z) == 0:
            mc.setBlocks(x1, y+1, z, x1, y+2, z, block.BOOKSHELF)
            count-=1

def Add_beds(x, y, z, width, length, height, count):
    
    # Add beds
    for i in range(x+1, x + width, 4):
        for t in range(z+1, z + length, 4):
            if mc.getBlocks(i, y + 1, t) == block.AIR:
                mc.setBlocks(i, y+1, t, i, y+2, t, block.BOOKSHELF)    
    
def Add_Trees(x, y, z, width, length, height, count):
    
    # Add Trees
    for i in range(x, x + width, 3):
        for t in range(z, z + length, 3):
            mc.setBlock(i, y, t, block.DIRT)
# Add furnance
# Add chest
x,y,z= Starting_coordinates()
Build_house()

Split_room_Add_door_Add_window(x, y, z, width, length, height, 3)
Add_bookshelf(x, y, z, width, length, height, 3)