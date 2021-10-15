import random
import numpy as np

"""
Class MazeBacktracking
genere un labyrinthe avec l'algorithme backtracking
"""
class MazeBacktracking():
    def __init__(self):                                            # --- --- CONSTRUCTEUR ATTR(size) : maze (direction) : NORD SUD OEUST EST (grid): matrice 
        self.size = int(input("choose a number : "))                    # --- user give Size  
        self.direction = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]           # --- Nord Sud Ouest Est 
        self.grid = np.zeros((self.size, self.size), dtype=int)         # --- Creation matrice de 0
        self.ver = [["#."] * self.size + ['#'] for _ in range(self.size)] + [[]]
        self.hor = [["##"] * self.size + ['#'] for _ in range(self.size + 1)]
        self.hor[0][0] = '#.'
        self.hor[-1][-2] = '#.'
        self.generate = self.backtrackingRecursive(0, 0)                # --- Generate backtracking recursive
        self.print = self.printMaze()

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
            if pos[0] == x: self.hor[max(y, pos[1])][x] = "#."
            if pos[1] == y: self.ver[y][max(x, pos[0])] = ".."                                                      
            self.backtrackingRecursive(pos[0],pos[1])              # --- Rappel recursiv avec un voisins a chaques fois
            
            #print(pos)                                            # --- En dépillant il retourne des nouvelles cellules inconnues 
        return x , y                                               # --- RETURNE POSITION DÉPART
         
    def printMaze(self):                                           # --- --- FUNCTION DRAW THE  MAZE IN A STRING
        maze = ""
        for (a, b) in zip(self.hor, self.ver):
            maze += ''.join(a + ['\n'] + b + ['\n'])
        print("Labyrinthe génerée ")
        print("\n")
        print(maze)
        return maze

"""
Class SolveMazeBacktracking
herite de la Class MazeBacktracking
resoud un labyrinthe avec l'algorithme backtracking o pour le chemin
et * pour les impasses
"""    
class SolveMazeBacktracking(MazeBacktracking):
    def __init__(self):                         # --- --- CONSTRUCTEUR ATTR(size) : maze (direction) : NORD SUD OEUST EST (grid): matrice               
        super().__init__()
        self.maze = np.zeros((self.size*2+1, self.size*2+1), dtype=int)
        self.start = (0, 1)
        self.end = (-1, -2)
        self.fillMaze = self.solveMazeRecusrive(self.start[0], self.start[1])
               
    def isLimit(self, x , y):                                       # --- --- FUNCTION RETURNE param (x , y) VERIFIE LIMITE MATRICE  
        
        if 0 <= x < self.size*2+1 and 0 <= y < self.size*2+1:              # --- limite Board
            return x, y                                            # --- si les position x et y sont dans les limites de ma matrice return 
        else: return False

    def fillMatrice(self):
        listChar = []
        for char in self.print:
            if char == "\n": continue
            listChar.append(char)
        
        i = 0
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if listChar[i] == '#': self.maze[x][y] = 1
                i += 1

    def selectNeighbors(self, x, y):                                # --- --- FUNCTION VERIFICATION DES BON VOISIN
        
        neighbors = []                                             # --- Voisin actuelle                                            
        for dir in self.direction:                                 # --- Boucle sur les directions
            if self.isLimit((x + dir[0]), (y + dir[1])):            # --- Ici on appel la verification de limite de la matrice
                if self.maze[(x + dir[0])][(y + dir[1])] == 0:     # --- Si le nouveau noeud n'est pas visité 
                    neighbors.append((x + dir[0], y + dir[1]))     # --- Alors append liste voisins
        return neighbors     

    def selectOldNeighbors(self, x, y):                             # --- --- FUNCTION VERIFICATION DES BON VOISIN
        
        Oldneighbors = []                                             # --- Voisin actuelle                                            
        for dir in self.direction:                                 # --- Boucle sur les directions
            if self.isLimit((x + dir[0]), (y + dir[1])):            # --- Ici on appel la verification de limite de la matrice
                if self.maze[(x + dir[0])][(y + dir[1])] != 0 and self.maze[(x + dir[0])][(y + dir[1])] != 1:     # --- Si le nouveau noeud n'est pas visité 
                    Oldneighbors.append((x + dir[0], y + dir[1]))     # --- Alors append liste voisins
        return Oldneighbors     

    def setPath(self, x, y):
        old = self.selectOldNeighbors(x, y)
        if not old:
            self.maze[x][y] = 2
        else:
            self.maze[x][y] = self.maze[old[0][0]][old[0][1]] + 1

    def findGoodPathRecursive(self, x, y):
        old = self.selectOldNeighbors(x, y)
        for ney in old:
            if (self.maze[x][y] -1) == self.maze[ney[0]][ney[1]]:
                if self.maze[ney[0]][ney[1]] == 2:
                    self.maze[ney[0]][ney[1]] = -7
                self.maze[x][y] = -7
                # print(self.maze)
                # input(" continue ? ")
                self.findGoodPathRecursive(ney[0], ney[1])
        
    def solveMazeRecusrive(self, x, y):
        self.fillMatrice()
        self.setPath(x, y)
        if self.maze[x][y] == self.maze[self.end[0]][self.end[1]]:
            self.end = (x, y)
            self.findGoodPathRecursive(self.end[0], self.end[1])
            return 
        neighbors = self.selectNeighbors(x, y)
        random.shuffle(neighbors)
        # print(self.maze)
        # input("continue ? ")
        for ney in neighbors:
            self.solveMazeRecusrive(ney[0], ney[1])
        
    def beautifulPrint(self):
        mazeString = ''
        for x in range(self.size*2+1):
            for y in range(self.size*2+1):
                if self.maze[x][y] == -7:
                    mazeString += "o"
                elif self.maze[x][y] == 1:
                    mazeString += "#"
                else:
                    mazeString += "*"
            mazeString += "\n"
        return mazeString


        # step 1 ON A LE VOISIN MTN NOTE COMME VUE C AUTRE CHOSEN AHHHAH marque comme vue si il y en a c tout et si il arrive a la bonne case voila

S1 = SolveMazeBacktracking()
maze = S1.beautifulPrint()
print("\n")
print("Labyrinthe résolue : ")
print("\n")
print("Chemin representée par des (oo) impasse par des (**) mur par des (##) ")
print(maze)