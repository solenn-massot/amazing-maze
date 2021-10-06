import numpy as np
import random

size = int(input("choose a number : "))
class MazeGenerate():
    def __init__(self, size):
        self.direction = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]
        self.size = size//2*2+1
        self.grid = np.zeros((self.size, self.size), dtype=int)
        self.generate = self.AmazingMazeBacktrackingRecurse(0, 0)
    
    def setPath(self, x, y):
        self.grid[x][y] = 1

    def isWall(self, x , y):
        if 0 <= x < self.size and 0 <= y < self.size:
            return x, y
        else: return False

    def setGoodNeighbors(self, x, y):
        directions = self.direction
        neighbors = []
        while (len(directions) > 0):

            tryDir = directions.pop()
            
            if self.isWall(x + tryDir[0], y + tryDir[1]):
                if self.grid[x + tryDir[0]][y + tryDir[1]] == 0:
                    neighbors.append((x + tryDir[0], y + tryDir[1]))
        return neighbors

    def shuffleDirection(self, x, y):
        liNeighbors = self.setGoodNeighbors(x, y)
        random.shuffle(liNeighbors)
        return liNeighbors
    
        

    def AmazingMazeBacktrackingRecurse(self, x ,y):

        self.setPath(x, y)

        print("")
        print(self.grid)
        print("")

        availableNodes = self.shuffleDirection(x, y)
        print(availableNodes)
        for (xx, yy) in availableNodes: 
            
            self.AmazingMazeBacktrackingRecurse(xx, yy)
        # nodeX = posRandom[0]
        # nodeY = posRandom[1]

# TUTORIEL PART 3 REVOIR LA MATRICE si elle s'aditionne ou i dont know
MazeGenerate(size)
        