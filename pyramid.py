
height = 0
blocks = int(input ("How many blocks do you want?: "))
layerblocks = 1

while layerblocks <= blocks:
    height += 1
    blocks -= layerblocks
    layerblocks += 1

print ("The height is", height)
