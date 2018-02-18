#Chapter 4 Challenge - Character Picture Grid

#Technically this works to create the heart image from the grid list but it's ugly
def picgrid(grid):
	y=0
	while y<=5:
		print(grid[0][y], grid[1][y], grid[2][y], grid[3][y], grid[4][y], grid[5][y], grid[6][y], grid[7][y], grid[8][y])
		y+=1

#Grid answer, so good. Could also use for loops
def picgrid2(grid):
	y=0
	while y<=5:
		x=0
		while x<=8:
			print(grid[x][y], end='')
			x+=1
		y+=1
		print(' ')
