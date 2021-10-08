import random
import numpy as np

class MazeKruskal():
    def __init__(self):                                           # --- --- CONSTRUCTEUR
        
        self.edges = {}                                           # --- init dict
        self.path = []                                            # --- init chemin
        self.size = int(input("choose a number : "))              # --- User give Size  
        self.direction = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]     # --- Nord Sud Ouest Est
        self.grid = np.zeros((self.size, self.size), dtype=int)   # --- Creation matrice de 0
        self.gridId = self.fullMatrix()
        self.generateEdge = self.selectAllEdges()                 # --- init all edge
        self.generate = self.generateKruskalMaze()                # --- Generate backtracking recursive
        
    def isWall(self, x , y):                                       # --- --- FUNCTION RETURNE param (x , y) VERIFIE LIMITE MATRICE  
        
        if 0 <= x < self.size and 0 <= y < self.size:              # --- limite Board
            return x, y                                            # --- si les position x et y sont dans les limites de ma matrice return 
        else: return False
    
    def selectGoodNeighbors(self, x, y):                           # --- --- FUNCTION VERIFICATION DES BON VOISIN
        
        neighbors = []                                             # --- Voisin actuelle                                            
        for dir in self.direction:                                 # --- Boucle sur les directions
            if self.isWall((x + dir[0]), (y + dir[1])):            # --- Ici on appel la verification de limite de la matrice
                if self.grid[(x + dir[0])][(y + dir[1])] == 0:     # --- Si le nouveau noeud n'est pas visité 
                    if self.getIdByVal((x + dir[0], y + dir[1])):
                        neighbors.append((x + dir[0], y + dir[1]))     # --- Alors append liste voisins
        return neighbors      
        
    def selectAllEdges(self):
        i = 0       
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                # self.edges.update({i : voisin })
                self.edges.update({ i : (x, y)})
                i+=1

    def getIdByVal(self, voisinTuple):
        for edge in self.edges:
            if self.edges[edge] == (voisinTuple[0], voisinTuple[1]):       
                return edge
            else : return False
    def fullMatrix(self):
        i = 0
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                self.grid[x][y] = i
                i += 1
        print(self.grid)
            
    def randomizeEdges(self):
        l = list(self.edges.items())
        random.shuffle(l)
        edges = dict(l)
        allEdges = edges
        return allEdges
    
    def connect(self, posOne, posTwo):
        # -- save path with this
        self.path.append((posOne, posTwo))
        print("path")
        print(self.path)
        
    
    def union(self, idOne, idTwo):
        edge1 = self.edges.get(idTwo)
        edge2 = self.edges.get(idOne)
        # print(edge1)
        listPos = (edge1, edge2)
        self.edges.update({idOne : listPos})
        print("id removed")
        print(idTwo)
        self.edges.pop(idTwo)
        print(self.edges)
                            
    def generateKruskalMaze(self):
        # STEP 1 GET RANDOM CASE
        # STEP 2 TAKE A NEIGHBORS
        # STEP 3 CHECK NEIGHBORS AND RANDOM CASE id's
        # STEP 4 CHOOSE A RANDOM GOOD NEIGHBORS
        # STEP 5 SAVE PATH AND UPDATE ID NEIGHBORS WITH ID CASE
        
         
        pass
        # allEdges = self.randomizeEdges()
        # for edge in allEdges:               # boucle sur un set de chemin
        #     if edge in self.edges:
        #         print("its edges")
        #         print(edge)
        #         pos = self.edges.get(edge)
        #         voisin = self.selectGoodNeighbors(pos[0], pos[1])
        #         if voisin == []:
        #             pass
                
        #         # REVOIR LA SELECTION DU VOSIN 
        #         # LE SCRIPT NE PEUX PRENDRE UN VOISIN QUI N'AS PAS D'ID !
        #         # IDEA DIRECTION PRISE OBLIGER QUE LE VOISIN A UN ID DIFFERENT SINON ESSAYE TOUTES LES DIRECTIONS ET LA C SUR VUE QUE L'ID RASSEMBLE LES CASE ENTRES ELLES ! 
        #         # mettre id par case garder les position de tous enlever les id par rapport aux voisins un voisin ayant le meme ID ne peux pa BASTAAA
        #           BOUCLER SUR LE NOMBRE DE CASE -1 x , y 
        
        
         
        #          print("voisin via pos ")
        #         print(voisin[0])
        #         random.shuffle(voisin)
        #         idVoisin = self.getIdByVal(voisin[0])
        #         print("id voisin [0]")
        #         print(idVoisin)
        #         if len(self.edges) == 1:
        #             return
        #         if edge != idVoisin:
                
        #             self.connect(pos, voisin[0])
        #             self.union(edge, idVoisin)
            
        
        # print(s)
        
MazeKruskal()