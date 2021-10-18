import random


class Cell:
    # Créer une cellule avec une position (= sa place dans l'array du maze) + des murs
    def __init__(self, position):
        self.position = position
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}
    # Vérifie si tous les murs sont là
    def check_walls(self):
        if False not in self.walls.values():
            return True
        else:
            return False
    #casse les murs
    def break_walls(self, next_cell, wall):
        wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
        self.walls[wall] = False
        next_cell.walls[wall_pairs[wall]] = False



class Maze(Cell):
    # Créer un labyrinthe avec la taille donnée
    def __init__(self, size):
        self.size = size
        self.entrance = 0
        self.cells = [[Cell((i,j)) for j in range(0, self.size)] for i in range(0, self.size)]
        self.stack = []
    
    #récupère la cellule
    def get_cell(self, position):
        return self.maze[position[0]][position[1]]
    #récupère les voisins
    def get_neighbours(self, cell):
        #direction disponible et comment s'y rendre
        direction = [('W', (-1, 0)),
                  ('E', (1, 0)),
                  ('S', (0, 1)),
                  ('N', (0, -1))]
        neighbours = []
        for wall, (tx, ty) in direction:
            n_x, n_y = cell.position[0] + tx, cell.position[1] + ty
            if (n_x >= 0 and n_x < self.size) and (n_y >= 0 and n_y < self.size):
                neighbour = self.get_cell((n_x, n_y))
                if neighbour.check_walls():
                    neighbours.append((wall, neighbour))
        return neighbours

    #creuse le chemin
    def carve_passage(self, position):
        current_cell = self.get_cell(position)
        neighbours = self.get_neighbours(current_cell)
        if not neighbours:
            current_cell = self.stack.pop()
        wall, next_cell = random.choice(neighbours)
        current_cell.break_walls(next_cell, wall)
        position = next_cell.position
        
        self.carve_passage(self, position)

        # current_cell = self.get_cell(self.entrance)
        # stack = []
        # visited = 1
        # while visited < self.size*self.size:
        #     #je récupère mes voisins
        #     neighbours = self.get_neighbours(current_cell)
        #     #si je n'ai pas de voisins, je pop ma cellule hors de ma stack
        #     if not neighbours:
        #         current_cell = stack.pop()
        #         continue
        #     wall, next_cell = random.choice(neighbours)
        #     current_cell.break_walls(next_cell, wall)
        #     stack.append(current_cell)
        #     current_cell = next_cell
        #     visited += 1
        




