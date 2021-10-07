import random
import numpy as np

class MazeGenerate():
    def __init__(self):
        self.size = int(input("choose a number : "))              # ----- user give Size  
        self.direction = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]     # ----- Nord Sud Ouest Est 
        self.grid = np.zeros((self.size, self.size), dtype=int)   # ----- Creation matrice de 0  
        self.generate = self.backtrackingRecursive(0, 0)          # ----- Generate backtracking recursive
        
    def setPath(self, x, y):
        # ici on dit set x, y a visité
        self.grid[x][y] = 1
        

    def isWall(self, x , y):
        if 0 <= x < self.size and 0 <= y < self.size:          # --- limite Board
            return x, y                                        # --- si les position x et y sont dans les limites de ma matrice return 
        else: return False

    def selectGoodNeighbors(self, x, y):
        neighbors = []                                         # --- Voisin actuelle                                            
        for dir in self.direction:                             # --- Boucle sur les directions
            if self.isWall((x + dir[0]), (y + dir[1])):        # --- Ici on appel la verification de limite de la matrice
                if self.grid[(x + dir[0])][(y + dir[1])] == 0: # --- Si le nouveau noeud n'est pas visité 
                    neighbors.append((x + dir[0], y + dir[1])) # --- Alors append liste voisins
        return neighbors                                       # --- Retourné list voisins verfiée
    
    def shuffleDirection(self, x, y):                          # --- Func randomize Direction
        liNeighbors = self.selectGoodNeighbors(x, y)           # --- on apelle les voisins avec x , y verifier
        if liNeighbors == False:                               # --- Si les voisins ne sont null
            return False                                       # --- Return False
        random.shuffle(liNeighbors)                            # --- Function de melange de list
        return liNeighbors                                     # --- liste melangée retourné

    def backtrackingRecursive(self, x ,y):                     # --- FUNCTION RECURSIVE
        # --- zone de test --- # 
        # print(self.grid) 
        # input("continue")
        
        self.setPath(x, y)                                     # --- Cellule x , y a visitée
        posRandom = self.shuffleDirection(x, y)                # --- appel de ma fonction de melange de mes voisins veriffiée
        
        for pos in posRandom:                                  # --- Boucle sur mes voisins verifiée
                        
            self.backtrackingRecursive(pos[0],pos[1])          # --- Rappel recursiv avec un voisins a chaques fois
                                                            
            #print(pos)                                        # ---  EN Dépillant il retourne des nouveaux noeud inconnue
        return
            

MazeGenerate()
        