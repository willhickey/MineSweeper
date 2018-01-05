from msvcrt import getch
from MinesweeperClasses import GameGrid

grid = GameGrid(5,5,24)
print(grid)
grid.layMines(1,1)
print(grid)

# while True:
	# #draw the cursor border
	# print_at(2*cursorY, 2*cursorX, '===')
	# print_at(2*cursorY+2, 2*cursorX, '===')
	# print_at(2*cursorY+1, 2*cursorX, '$ $')
	# key = getch()
	# if key == b'Q' or key == b'q':
		# break
	# if key == b' ':
		# sweep(cursorX, cursorY)
	# if key == b'F':
		# markMine(cursorX, cursorY)