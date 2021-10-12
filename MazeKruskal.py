import random
import numpy as np

class MazeKruskal():
    def __init__(self):                                     # --- --- CONSTRUCTEUR attribut : size maze , direction, matrice, edge, generateMaze
        
        self.size = int(input('choose a number : '))                    # --- User give Size  
        self.direction = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]           # --- Nord Sud Ouest Est
        self.grid = np.zeros((self.size, self.size), dtype=int)         # --- Creation matrice de 0
        self.maze = np.zeros((self.size*2-1, self.size*2-1), dtype=int) # --- Matrice de modelisation du maze
        self.edge =  self.setIdMatrix()                                 # --- Rentrer edge via ID
        self.path = self.generateKruskalMaze()                          # --- Generate backtracking recursive
        
    def isLimit(self, x , y):                               # --- --- FUNCTION RETURNE param (x , y) VERIFIE LIMITE MATRICE  

        if 0 <= x < self.size and 0 <= y < self.size:              # --- limite Board
            return x, y                                            # --- si les position x et y sont dans les limites de ma matrice return 
        else: return False
    
    def setIds(self, edge, edgePop):                        # --- --- FUNCTION set ID with param edge une postion edgePop position voisine
        self.grid[self.grid == self.grid[edgePop[0]][edgePop[1]]] = self.grid[edge[0]][edge[1]]                    
        # print("position one two")
        # print(edge, edgePop)
        # print("id one two")
        # print(self.grid[edge[0]][edge[1]], self.grid[edgePop[0]][edgePop[1]])
                    
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
                    # print(edge)
                    # print(neighbors[i])
                    path.append((edge, neighbors[i]))                   # STEP 4 Finally SAVE PATH
                    self.setIds(edge, neighbors[i])                     # STEP 5 UPDATE ID NEIGHBORS WITH ID CASE
                    self.mazeInString(edge, neighbors[i])
                    # print(self.grid)                                    # pour mieux comprendre print            
                    # input("continue ? ")                                # step by step regardez les differentes action de lm'algorithme
        # print(path)
        return path
    
    def mazeInString(self, edgeOne, edgeTwo):               # --- --- FUNCTION make a maze in matrice     
        if edgeOne[0] == edgeTwo[0]:
            if edgeTwo[1] == 0 or edgeOne[1] == 0:
                middleEdge = 1
                
            elif edgeOne[1] < edgeTwo[1]:
                middleEdge = (edgeTwo[1]*2) -1 
                
            else:
                middleEdge = (edgeOne[1]*2)-1
            self.maze[edgeOne[0]*2][middleEdge] = 1    
            
        else:
            if edgeTwo[0] == 0 or edgeOne[0] == 0:
                middleEdge = 1
                
            elif edgeOne[0] < edgeTwo[0]:
                middleEdge = (edgeTwo[0]*2) -1 
                
            else:
                middleEdge = (edgeOne[0]*2)-1
            self.maze[middleEdge][edgeOne[1]*2] = 1    
        self.maze[edgeOne[0]*2][edgeOne[1]*2] = 1
        self.maze[edgeTwo[0]*2][edgeTwo[1]*2] = 1

    def printMaze(self):                                    # --- --- FUNCTION make a maze in string
        maze = ''
        wall = "##"
        path = ".."
        br = "\n"
        maze += wall + path + (wall * len(self.maze)) + br
        for x in range(len(self.maze)):
            maze += wall
            for y in range(len(self.maze)):
                if self.maze[x][y] == 0:
                    maze += wall
                else:
                    maze += path
            maze += wall + br
        maze += wall * len(self.maze) + path + wall
        return maze
    
    
M1 = MazeKruskal()
maze = M1.printMaze()
print(maze)