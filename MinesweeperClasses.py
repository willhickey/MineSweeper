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
		#for rowIndex in range(0, self.gridHeight):
		#	for colIndex in range(0, self.gridWidth):
		#		stringRepresentation = stringRepresentation + self.grid[rowIndex][colIndex].__str__()
		#	stringRepresentation = stringRepresentation + '\n'
		for y in range(0,self.gridHeight):
			stringRepresentation = stringRepresentation + '-'*self.gridWidth*2 + '-' + '\n' 
			for x in range(0,self.gridWidth):
				stringRepresentation = stringRepresentation + '|' + self.grid[y][x].__str__()
			stringRepresentation = stringRepresentation + '|\n'
		stringRepresentation = stringRepresentation + '-'*self.gridWidth*2 + '-' + '\n' 
		return stringRepresentation
	
	def revealSquare(self, clickedY, clickedX):
		if self.grid[clickedY][clickedX].isFlagged == 1:
			return 0
		self.grid[clickedY][clickedX].isRevealed = 1
		if self.grid[clickedY][clickedX].isMine == 1:
			return 1
		
		if self.grid[clickedY][clickedX].adjacentMineCount == 0:
			for i in range(-1, 2):
				for j in range(-1, 2):
					if clickedY+i >=0 and clickedY+i < self.gridHeight and clickedX+j>=0 and clickedX+j < self.gridWidth:
						self.grid[clickedY+i][clickedX+j].isRevealed = 1
		return 0

		
	def markMine(self, clickedY, clickedX):
		self.grid[clickedY][clickedX].isFlagged = 1
	
	def checkGrid(self):
		for y in range(0,self.gridHeight):
			for x in range(0,self.gridWidth):
				if not self.grid[y][x].isRevealed and not self.grid[y][x].isMine:
					return 0
		return 1	#if we get here, the entire grid is either revealed or mines
	
class GameSquare:
	isMine = 0
	isFlagged = 0
	isRevealed = 0
	adjacentMineCount = 0
	
	def __str__(self):
		if self.isFlagged == 1:
				return 'F'
		if self.isRevealed == 1:
			if self.isMine == 1:
				return 'X'
			else:
				return str(self.adjacentMineCount)
		else:
			return ' '