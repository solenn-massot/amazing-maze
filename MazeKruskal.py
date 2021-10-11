import random
import numpy as np

class MazeKruskal():
    def __init__(self):                                     # --- --- CONSTRUCTEUR attribut : size maze , direction, matrice, edge, generateMaze
        
        self.size = int(input('choose a number : '))              # --- User give Size  
        self.direction = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]     # --- Nord Sud Ouest Est
        self.grid = np.zeros((self.size, self.size), dtype=int)   # --- Creation matrice de 0
        self.edge =  self.setIdMatrix()                           # --- get edge via ID
        self.maze = self.generateKruskalMaze()                    # --- Generate backtracking recursive
        
    def isLimit(self, x , y):                               # --- --- FUNCTION RETURNE param (x , y) VERIFIE LIMITE MATRICE  

        if 0 <= x < self.size and 0 <= y < self.size:              # --- limite Board
            return x, y                                            # --- si les position x et y sont dans les limites de ma matrice return 
        else: return False
    
    def setIds(self, edge, edgePop):                        # --- --- FUNCTION set ID with param edge une postion edgePop position voisine
        self.grid[self.grid == self.grid[edgePop[0]][edgePop[1]]] = self.grid[edge[0]][edge[1]]                    
                    
    def setIdMatrix(self):                                  # --- --- FUNCTION set ID on all grid 

        i = 0
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                self.grid[x][y] = i
                i += 1
    
    def checkIdViaPos(self, edgeOne, edgeTwo):              # --- --- FUNCTION verifie id edgeOne edgeTwo 

        if self.grid[edgeOne[0]][edgeOne[1]] == self.grid[edgeTwo[0]][edgeTwo[1]]:
            return False
        else: return True
    
    def selectNeighborsViaPos(self, x, y):                  # --- --- FUNCTION verifie des bon vosins
        
        neighbors = []                                                 # --- Voisin actuelle                                            
        for dir in self.direction:                                     # --- Boucle sur les directions
            if self.isLimit((x + dir[0]), (y + dir[1])):               # --- Ici on appel la verification de limite de la matrice
                    neighbors.append((x + dir[0], y + dir[1]))         # --- Alors stock liste des voisins
        return neighbors     
          
    def randomizeEdges(self):                               # --- --- FUNCTION randomise all edges
        
        listEdgesRand = []
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                listEdgesRand.append((x, y))
        random.shuffle(listEdgesRand)
        return listEdgesRand

    def generateKruskalMaze(self):                          # --- --- FUNCTION generate maze avec l'algorithme de kruska
        path = []
        allEdges = self.randomizeEdges()
        
        while len(allEdges) > 0:                                        # loop on all edges
            edge = allEdges.pop()                                       # STEP 1 GET RANDOM CASE
            neighbors = self.selectNeighborsViaPos(edge[0], edge[1])
            random.shuffle(neighbors)                                   # STEP 2 TAKE A NEIGHBORS random

            for i in range(len(neighbors)):                             # loop sur les voisins justfier par des vosins avec 
                if i == 2:                                              # si plus de 2 voisins break et reprend a prendre edge
                    break

                if self.checkIdViaPos(edge, neighbors[i]):              # STEP 3 CHECK NEIGHBORS and edge id's
                
                    path.append(edge)                                   # STEP 4 Finally SAVE PATH
                    path.append(neighbors[i])                           # STEP 4 Finally SAVE PATH
                    self.setIds(edge, neighbors[i])                     # STEP 5 UPDATE ID NEIGHBORS WITH ID CASE
                     
                    print(self.grid)                                    # pour mieux comprendre print
                    input("continue ? ")                                # step by step regardez les differentes action de lm'algorithme
        print(path)
        return path
    
    def mazeInString(self):                                 # --- --- FUNCTION print a maze in string
        i = 0
        Maze = ''
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                for i in range(len(self.maze)):
                
                    if x == self.maze[i][0] and y == self.maze[i][1]:
                        Maze += "."    
                    else:
                        Maze += "#"
                    i += 1
            Maze += "\n"
        return Maze

    
M1 = MazeKruskal()
maze = M1.mazeInString()
print(maze)