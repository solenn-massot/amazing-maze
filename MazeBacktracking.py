import random
import numpy as np

class MazeBacktracking():
    def __init__(self):                                                 # --- --- CONSTRUCTEUR ATTR(size) : maze (direction) : NORD SUD OEUST EST (grid): matrice 
        self.size = int(input("choose a number : "))                    # --- user give Size  
        self.direction = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]           # --- Nord Sud Ouest Est 
        self.grid = np.zeros((self.size, self.size), dtype=int)         # --- Creation matrice de 0
        self.mazeSize = self.size // 2 *2 +1                            # --- Matrice de modelisation du maze
        self.ver = [["#.."] * self.size + ['#'] for _ in range(self.size)] + [[]]
        self.hor = [["###"] * self.size + ['#'] for _ in range(self.size + 1)]
        self.generate = self.backtrackingRecursive(0, 0)                # --- Generate backtracking recursive

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
        return neighbors                                           # --- Retourné list voisins verfiée
    
    def shuffleDirection(self, x, y):                              # --- --- FUNCTION MELANGE LES DIRECTION
        
        liNeighbors = self.selectGoodNeighbors(x, y)               # --- on apelle les voisins avec x , y verifier
        if liNeighbors == False:                                   # --- Si les voisins ne sont null
            return False                                           # --- Return False
        random.shuffle(liNeighbors)                                # --- Function de melange de list
        return liNeighbors                                         # --- liste melangée retourné
        
    def backtrackingRecursive(self, x ,y):                         # --- --- FUNCTION RECURSIVE
        
        # print(self.grid)                                           # --- ZONE DE TEST --- #
        #                                                            # --- pour voir l'avancée de l'algo dans la matrice                                            
        # input("continue")                                          # --- ZONE DE TEST --- #
        posRandom = self.shuffleDirection(x, y)                    # --- appel de ma fonction de melange de mes voisins veriffiée
        self.grid[x][y] = 1                                        # --- change x , y par 1 pour dire qu'il a était visitée
        for pos in posRandom:                                      # --- Boucle sur mes voisins verifiée
            if self.grid[pos[0]][pos[1]]: continue
            if pos[0] == x: self.hor[max(y, pos[1])][x] = "#.."
            if pos[1] == y: self.ver[y][max(x, pos[0])] = "..."                                                      
            self.backtrackingRecursive(pos[0],pos[1])              # --- Rappel recursiv avec un voisins a chaques fois
            
            #print(pos)                                            # --- En dépillant il retourne des nouvelles cellules inconnues 
        return x , y                                               # --- RETURNE POSITION DÉPART
         
    def checkFill(self, x, y):
        if self.grid[x][y] ==0:
            return True
        else: return False
        
    
    def printMaze(self):
        s = ""
        for (a, b) in zip(self.hor, self.ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        return s
    
    
M1 = MazeBacktracking()
s = M1.printMaze()
print(s)