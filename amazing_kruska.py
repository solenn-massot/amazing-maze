import random

class Maze:
      def __init__(self, size):
        self.width = size * 2 + 1
        self.height = size * 2 + 1 
        self.brd = []
        
      
      def printMaze(self):
            i = 0
            for x in range(self.height):
                  print(x)
                  if x == 0 or (x * 2) == 0:
                      for y in range(self.width):
                            self.brd[x][y] = '#'
                  else:
                      for y in range(self.width):
                            if y == 0 or (y * 2) == 0:
                                  self.brd[x][y] = "#"
                            else:
                                  self.brd[x][y] = i
                                  i += 1
                  print(self.brd[y])



size = int(input("Please enter a number"))
maze = Maze(size)
maze.printMaze()