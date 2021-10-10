import random
import numpy as np

class MazeKruskal():
    def __init__(self):                                           # --- --- CONSTRUCTEUR
        
        self.size = int(input('choose a number : '))              # --- User give Size  
        self.direction = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]     # --- Nord Sud Ouest Est
        self.grid = np.zeros((self.size, self.size), dtype=int)   # --- Creation matrice de 0
        self.edge =  self.GetIdMatrix()                           # --- get edge via ID
        self.generate = self.generateKruskalMaze()                # --- Generate backtracking recursive
        
    def isLimit(self, x , y):                                     # --- --- FUNCTION RETURNE param (x , y) VERIFIE LIMITE MATRICE  

        if 0 <= x < self.size and 0 <= y < self.size:              # --- limite Board
            return x, y                                            # --- si les position x et y sont dans les limites de ma matrice return 
        else: return False
    
    def setIds(self, edge, edgePop):                              # --- --- FUNCTION SET ID with param edge une postion edgePop position voisine
        
        # print("id edges One")
        # print(self.grid[edge[0]][edge[1]])
        # print("nombre de recurrences")
        # print(nbr)
        # print("id edges One")
        # print(self.grid[edgePop[0]][edgePop[1]])
        # print("nombre de recurrences")
        # print(nbr1)

        nbr = np.count_nonzero(self.grid == self.grid[edge[0]][edge[1]])    
        nbr1 = np.count_nonzero(self.grid == self.grid[edgePop[0]][edgePop[1]])
        
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):

                if nbr >= nbr1:
                    if self.grid[x][y] == self.grid[edgePop[0]][edgePop[1]]:
                        self.grid[x][y] = self.grid[edge[0]][edge[1]]
                        self.grid[edgePop[0]][edgePop[1]] = self.grid[edge[0]][edge[1]]

                else :
                    if self.grid[x][y] == self.grid[edge[0]][edge[1]]:
                        self.grid[x][y] = self.grid[edgePop[0]][edgePop[1]]
                        self.grid[edge[0]][edge[1]] = self.grid[edgePop[0]][edgePop[1]]

    def GetIdMatrix(self):

        i = 0
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                self.grid[x][y] = i
                i += 1
    
    def checkIdViaPos(self, edgeOne, edgeTwo):

        if self.grid[edgeOne[0]][edgeOne[1]] == self.grid[edgeTwo[0]][edgeTwo[1]]:
            return False
        else: return True
    
    def selectNeighborsViaPos(self, x, y):                          # --- --- FUNCTION VERIFICATION DES BON VOISIN
        
        neighbors = []                                                 # --- Voisin actuelle                                            
        for dir in self.direction:                                     # --- Boucle sur les directions
            if self.isLimit((x + dir[0]), (y + dir[1])):               # --- Ici on appel la verification de limite de la matrice
                    neighbors.append((x + dir[0], y + dir[1]))         # --- Alors stock liste des voisins
        return neighbors     
          
    def randomizeEdges(self):
        
        listEdgesRand = []
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                listEdgesRand.append((x, y))
        random.shuffle(listEdgesRand)
        return listEdgesRand

    def generateKruskalMaze(self):
        path = []
        # STEP 1 GET RANDOM CASE
        allEdges = self.randomizeEdges()
        for edge in allEdges:                                               # --- PROBLEM WITH LOOP BAD LOOP

            # STEP 2 TAKE A NEIGHBORS et on random
            neighbors = self.selectNeighborsViaPos(edge[0], edge[1])
            random.shuffle(neighbors)

            # STEP 3 CHECK NEIGHBORS and edge id's
            if self.checkIdViaPos(edge, neighbors[0]):
                
                # STEP 5 Finally SAVE PATH AND UPDATE ID NEIGHBORS WITH ID CASE
                path.append((edge, neighbors[0]))
                self.setIds(edge, neighbors[0])
                print(self.grid)
                input("continue ? ")

        print(path) 

MazeKruskal()