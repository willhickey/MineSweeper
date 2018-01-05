from msvcrt import getch
from MinesweeperClasses import GameGrid
import os
import sys
from ctypes import *
STD_OUTPUT_HANDLE = -11
class COORD(Structure):
	pass
 
COORD._fields_ = [("X", c_short), ("Y", c_short)]
 
def print_at(r, c, s):
	h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
	windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
	c = s.encode("windows-1252")
	windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)
os.system('cls')

gridHeight = 10
gridWidth = 10
grid = GameGrid(gridHeight,gridWidth,10)
#print(grid)
#grid.layMines(1,1)
print(grid)

cursorX = 0
cursorY = 5
minesPositioned = 0
while True:
	#draw the cursor border
	os.system('cls')
	print(grid)
	print_at(2*cursorY, 2*cursorX, '===')
	print_at(2*cursorY+2, 2*cursorX, '===')
	print_at(2*cursorY+1, 2*cursorX+2, '$')
	print_at(2*cursorY+1, 2*cursorX, '$')
	key = getch()
	if key == b'Q' or key == b'q':
		break
	if key == b' ':
		if minesPositioned ==0:
			minesPositioned = 1
			grid.layMines(cursorY,cursorX)
			
		detonatedMine = grid.revealSquare(cursorY, cursorX)
		if detonatedMine == 1:
			os.system('cls')
			print(grid)
			print_at(2*gridHeight+3, 1, 'Detonated a mine\n')
			sys.exit()
		gameWon = grid.checkGrid()
		if gameWon == 1:
			os.system('cls')
			print(grid)
			print_at(2*gridHeight+3, 1, 'You win!\n')
			sys.exit()
			
	if key == b'F' or key == b'f':
		grid.markMine(cursorY, cursorX)
		
	#move the cursor if an arrow key was pressed
	if key == b'K' and cursorX > 0:
		cursorX = cursorX - 1
	if key == b'M' and cursorX < gridWidth-1:
		cursorX = cursorX + 1
	if key == b'H' and cursorY > 0:
		cursorY = cursorY - 1
	if key == b'P' and cursorY < gridHeight-1:
		cursorY = cursorY + 1		
	