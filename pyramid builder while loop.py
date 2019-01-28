blocks = int(input("Enter the number of blocks: 5"))
height = 0
inlayer = 1
while inlayer <= blocks:
	height += 1
	blocks -= inlayer
	inlayer += 1

print("Height of the pyramid:",height)
