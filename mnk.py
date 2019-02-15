from pprint import pprint
X = 1
O = 2
k = 4

initial_grid_size = 20
center = (initial_grid_size/2,initial_grid_size/2)

grid = [[0 for j in range(initial_grid_size)] for i in range(initial_grid_size)]

grid[center[0]][center[1]] = X
grid[center[0]][center[1]+1] = O
grid[center[0]+1][center[1]] = X
grid[center[0]+2][center[1]] = O
grid[center[0]-1][center[1]] = X
grid[center[0]-2][center[1]] = O
#Location for first 2 moves do not matter due to rotational symmetry
#O and X should always move next to each other since not doing so will always make
#X's grid value smaller, since O will not obstruct anything

directions = [[0,4,6],
			  [1,5,7],
			  [2,4,5],
			  [3,5,6],
			  [0,2,4,5,6],
			  [1,2,4,5,7],
			  [0,3,4,6,7],
			  [1,3,5,6,7],
			  [0,1,2,3,4,5,6,7]]

def gameOver():
	pprint(grid)
	exit()

# left, right, up, down, ul, ur, dl, dr, no = 0, 1, 2, 3, 4, 5, 6, 7, 8
def getNeighbours(dir):
	return directions[dir]
	
# 0     1      2   3     4   5   6   7
# left, right, up, down, ul, ur, dl, dr	
def getPosFromDir(pos, dir):
	if dir == 0:
		return (pos[0] - 1, pos[1])
	elif dir == 1:
		return (pos[0] + 1, pos[1])
	elif dir == 2:
		return (pos[0], pos[1] + 1)
	elif dir == 3:
		return (pos[0], pos[1] - 1)
	elif dir == 4:
		return (pos[0] - 1, pos[1] + 1)
	elif dir == 5:
		return (pos[0] + 1, pos[1] + 1)
	elif dir == 6:
		return (pos[0] - 1, pos[1] - 1)
	elif dir == 7:
		return (pos[0] + 1, pos[1] - 1)
				
# left, right, up, down, ul, ur, dl, dr, no = 0, 1, 2, 3, 4, 5, 6, 7, 8			
def getAllOptions(pos, dir):
	result = set([])
	for direction in getNeighbours(dir):
		cell = getPosFromDir(pos, direction)
		if grid[cell[0]][cell[1]] == 0:
			result.add(cell)
		else:
			result.update(getAllOptions(cell, direction))
	return result
		
		
	

# In theory player O in perfect play should never get ahead. So he should only try to minimize
# the grid value of player X
# Proof: uit me duim gezogen
	
def bestMove(player):
    if (player == X):
		for x in getAllOptions((initial_grid_size/2, initial_grid_size/2), 8):
			grid[x[0]][x[1]] = 9
		pprint(grid)
		return
        #for each possible option
		#	maximize getGridValue for that option for player X
		#	if multiple options have the same getGridValue
		#		select option with minimal getGridValue for player O
		#do that move
		#check whether game is over
    else:  
		return
        #for each possible option
		#	minimize getGridValue for that option for player X
		#	if multiple options have the same getGridValue
		#		select option with maximal getGridValue for player O
		#do that move

# How to calculate grid value: idk
def getGridValue(grid, player):
	# TODO: figure out how gridvalue should be calculated
	return
	
bestMove(X)