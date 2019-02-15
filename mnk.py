from pprint import pprint
X = 1
O = 2
k = 4

initial_grid_size = 20

grid = [[0 for j in range(initial_grid_size)] for i in range(initial_grid_size)]

grid[initial_grid_size/2][initial_grid_size/2] = X
grid[initial_grid_size/2 + 1][initial_grid_size/2] = O
#Location for first 2 moves do not matter due to rotational symmetry
#O and X should always move next to each other since not doing so will always make
#X's grid value smaller, since O will not obstruct anything

def gameOver():
	pprint(grid)
    exit()

# In theory player O in perfect play should never get ahead. So he should only try to minimize
# the grid value of player X
# Proof: uit me duim gezogen
	
def bestMove(player):
    if (player == X):
        #for each possible option
		#	maximize getGridValue for that option for player X
		#	if multiple options have the same getGridValue
		#		select option with minimal getGridValue for player O
		#do that move
		#check whether game is over
    else:  
        #for each possible option
		#	minimize getGridValue for that option for player X
		#	if multiple options have the same getGridValue
		#		select option with maximal getGridValue for player O
		#do that move

# How to calculate grid value: idk
def getGridValue(grid, player):
	# TODO: figure out how gridvalue should be calculated
	return
	