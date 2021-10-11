class Sisi:
    def __init__(self):
        self.size = int(input("choose a number : "))
        self.walls = [(x,y,x+1,y) for x in range(self.size-1) for y in range(self.size)]
        print(self.walls)
        
Sisi()