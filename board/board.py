class Board:

    def __init__(self,width,height,charArr):
        self.width = width
        self.height = height
        self.grid = [[]]
        self.displayGrid = [[]]
        self.chars = charArr
        self.status = "not started"

    def emptyBoard(self, obj):
        self.grid = [[obj for x in range(self.width)]for y in range(self.height)]
        self.displayGrid = [[obj for x in range(self.width)]for y in range(self.height)]
    
    def fill(self,x,y, obj):
        """print("x", end =" ")
        print(x, end= " ")
        print(", y", end =" ")
        print(y)"""
        self.grid[y][x] = obj

    def countBombs(self):
        bombs = 0
        for x in range(self.width):
            for y in range(self.height):
                if(self.grid[y][x].bomb):
                    bombs+=1
        return bombs
    
    def update(self):
        for x in range(self.width):
            for y in range(self.height):
                tile = self.grid[y][x]
                tile.setDisplay()
                if(tile.bomb and not tile.hidden):
                    self.status = "game over"
        
    def Reveal(self):
        bombs = 0
        pos = self.getPos()
        tile = self.grid[pos[1]-1][pos[0]]
        if(tile.hidden):
            tile.hidden = False
            if(tile.countAdjecentBombs() == 0):
                tile.refealInnocents()

    def Mark(self):
        pos = self.getPos()
        tile = self.grid[pos[1]-1][pos[0]]
        if(tile.hidden):
            tile.marked = not tile.marked
            
    def getPos(self):
        print("fill coordinate x ", end="")
        x = input()
        print("fill coordinate y ", end="")
        y = input()
        print(ord(x.upper())-65)
        pos = [ord(x.upper())-65,int(y)]
        return pos
    
    def printBoard(self):
        print("   ", end="")
        for i in range(self.width):
            print(chr(65+i),end="")
        
        print("\n  ╔", end="")
        for val in range(self.width):
            print("═",end="")
        print("╗")

        # And here it prints the rows per row index.
    
        for y in range(self.height):
            addedSpace = ""    
            if(y+1 < 10):
                addedSpace = " "
            print(y+1, end= addedSpace+"║")

            for x in range(self.width):
                self.grid[y][x].setDisplay()
                print(self.grid[y][x].display, end="")
            print("║")   
        
        print("  ╚", end="")
        for val in range(self.width):
            print("═",end="")
        print("╝")
           
