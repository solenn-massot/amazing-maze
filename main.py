import random

size = int(input("choose a number : "))
class MazeGenerate():
    def __init__(self, size):
        self.neighbors = []
        self.direction = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]
        self.size = size//2*2+1
        self.limitGrid = self.size-1
        self.grid = [[1 for x in range(self.size) ] for y in range(self.size)]
        self.generate = self.AmazingMazeBacktrackingRecurse(0, 0)
        # for x in range(len(self.grid)):
        #     for y in range(len(self.grid)):
        #         print(self.grid[x][y])
        # print("\n")
        self.walls = [True, True, True, True]
        self.visited = 0
    
    def setPath(self, x, y):
        self.grid[x][y] = 0

    def isWall(self, x , y):
        if 0 <= x < self.limitGrid and 0 <= y < self.limitGrid:
            return x, y
        else: return False

    def setGoodNeighbors(self, x, y):
        directions = self.direction
        while (len(directions) > 0):

            tryDir = directions.pop()
            
            if self.isWall(x + tryDir[0], y + tryDir[1]):
                self.neighbors.append([x + tryDir[0], y + tryDir[1]])
            # RAJOUTER UN SI IL NY A RIEN EN BAS
        return self.neighbors

    def selectDirection(self, x, y):
        liNeighbors = self.setGoodNeighbors(x, y)
        random.shuffle(liNeighbors)
        # get direction randomisé

        return liNeighbors[0]
    
    def PrintState(self):
        print(self.grid)
        

    def AmazingMazeBacktrackingRecurse(self, x ,y):
        self.setPath(x, y)
        self.PrintState()
        posRandom = self.selectDirection(x, y)
        nodeX = posRandom[0]
        nodeY = posRandom[1]
        self.setPath(nodeX, nodeY)
        self.AmazingMazeBacktrackingRecurse(nodeX, nodeX)

# TUTORIEL PART 3 REVOIR LA MATRICE si elle s'aditionne ou i dont know
MazeGenerate(size)
        