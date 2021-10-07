import random
import numpy as np

class MazeKruskal():
    def __init__(self):                                           # --- --- CONSTRUCTEUR
        self.edges = {}                                           #
        self.size = int(input("choose a number : "))              # --- User give Size  
        self.direction = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]     # --- Nord Sud Ouest Est
        self.grid = np.zeros((self.size, self.size), dtype=int)   # --- Creation matrice de 0  
        self.generate = self.generateKruskalMaze()                     # --- Generate backtracking recursive
        
    def isWall(self, x , y):                                       # --- --- FUNCTION RETURNE param (x , y) VERIFIE LIMITE MATRICE  
        
        if 0 <= x < self.size and 0 <= y < self.size:              # --- limite Board
            return x, y                                            # --- si les position x et y sont dans les limites de ma matrice return 
        else: return False
    
    def selectGoodNeighbors(self, x, y):                           # --- --- FUNCTION VERIFICATION DES BON VOISIN
        
        neighbors = []                                             # --- Voisin actuelle                                            
        for dir in self.direction:                                 # --- Boucle sur les directions
            if self.isWall((x + dir[0]), (y + dir[1])):            # --- Ici on appel la verification de limite de la matrice
                if self.grid[(x + dir[0])][(y + dir[1])] == 0:     # --- Si le nouveau noeud n'est pas visité 
                    neighbors.append((x + dir[0], y + dir[1]))     # --- Alors append liste voisins
        return neighbors      
        
    def selectAllEdges(self):
        i = 0        
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                voisin = self.selectGoodNeighbors(x, y)
                randVoisin = random.shuffle(voisin)
                # self.edges.update({i : voisin })
                self.edges.update({(x, y) : { i : voisin}})
                i+=1
        return self.edges
        
                
    def generateKruskalMaze(self):
        allEdges = self.selectAllEdges()
        # print(allEdges)
        l = list(allEdges.items())
        random.shuffle(l)
        edges = dict(l)
        s = edges
        print(s)
        
MazeKruskal()