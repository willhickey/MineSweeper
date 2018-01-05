from random import randint

class GameGrid:
	gridHeight = 0
	gridWidth = 0
	mineCount = 0
	
	#current position
	def __init__(self, gridHeight, gridWidth, mineCount):
		self.gridHeight = gridHeight
		self.gridWidth = gridWidth
		self.mineCount = mineCount
		self.grid = [None] * gridHeight
		for y in range(0, gridHeight):
			self.grid[y] = [None] * gridWidth
			for x in range(0, gridWidth):
				self.grid[y][x] = GameSquare()
		
	def layMines(self, clickedY, clickedX):
		minesLaid = 0
		while minesLaid < self.mineCount:
			y = randint(0, self.gridHeight-1)
			x = randint(0, self.gridWidth-1)
			if (y != clickedY or x!= clickedX) and self.grid[y][x].isMine == 0:
				self.grid[y][x].isMine = 1
				minesLaid = minesLaid + 1
		for y in range(0, self.gridHeight):
			for x in range(0, self.gridWidth):
				for i in range(-1, 2):
					for j in range(-1, 2):
						if y+i >=0 and y+i < self.gridHeight and x+j>=0 and x+j < self.gridWidth and self.grid[y+i][x+j].isMine:
							self.grid[y][x].adjacentMineCount = self.grid[y][x].adjacentMineCount + 1
	
	def __str__(self):
		stringRepresentation = ''
		for rowIndex in range(0, self.gridHeight):
			for colIndex in range(0, self.gridWidth):
				stringRepresentation = stringRepresentation + self.grid[rowIndex][colIndex].__str__()
			stringRepresentation = stringRepresentation + '\n'
		return stringRepresentation
	
	#def revealSquare(self, clickedCol, clickedRow):
		
	#def flagSquare(self)
	#move position
	#reveal square
	#populate grid
	
class GameSquare:
	isMine = 0
	isFlagged = 0
	isRevealed = 1
	adjacentMineCount = 0
	
	def __str__(self):
		if self.isRevealed == 1:
			if self.isMine == 1:
				return 'X'
			else:
				return str(self.adjacentMineCount)
		else:
			return ' '