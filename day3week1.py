from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

land_height = 100


if True:
    plot_x = 10

    plot_z = -10

    size_x = 20

    size_z = 30




    # Create the land

    mc.setBlocks(plot_x, 0, plot_z, plot_x + size_x, land_height, plot_z + size_z, block.GRASS)




 # Destroy everything above

    mc.setBlocks(plot_x, land_height + 1, plot_z, plot_x + size_x, 255, plot_z + size_z, block.AIR)



    mc.player.setPos(plot_x, land_height + 1, plot_z)


house_x = 12

house_z = -5

house_size_x = 10

house_size_z = 16

house_height = 5


# Build four walls

mc.setBlocks(house_x, land_height + 1, house_z, house_x + house_size_x - 1, land_height + house_height, house_z, block.WOOD)

mc.setBlocks(house_x, land_height + 1, house_z, house_x, land_height + house_height, house_z + house_size_z - 1, block.WOOD)

mc.setBlocks(house_x, land_height + 1, house_z + house_size_z - 1, house_x + house_size_x - 1, land_height + house_height, house_z + house_size_z - 1, block.WOOD)

mc.setBlocks(house_x + house_size_x - 1, land_height + 1, house_z, house_x + house_size_x - 1, land_height + house_height, house_z + house_size_z - 1, block.WOOD)
