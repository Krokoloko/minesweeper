class Tile:
    def __init__(self,x, y, bomb, chars):
        self.x = x
        self.y = y
        self.bomb = bomb
        self.chars = chars
        self.display = ""
        self.hidden = True
        self.marked = False
        self.adjecent = []

    def getAdjecent(self, board):
        sides = [[-1,-1],[-1,0],[0,-1],[1,0],[0,1],[1,1],[-1,1],[1,-1]]
        adjecent = []
        
        #print("tile: ",end="")
        #print(self.x,end=",")
        #print(self.y)
        for side in sides:
            if(not side[0]+self.x >= board.width and not 0 > side[0]+self.x):
                if(not side[1]+self.y >= board.height and not 0 > side[1]+self.y):
                    adjecent.append(board.grid[self.y+side[1]][self.x+side[0]])
                    #print(self.x+side[0], end=", ")
                    #print(self.y+side[1])
                    
        self.adjecent = adjecent
        #print(len(self.adjecent))
        
    def countAdjecentBombs(self):
        bombs = 0
        for i in self.adjecent:
            if(i.bomb):
                bombs+=1
        return bombs

    def refealInnocents(self):
        if(not self.bomb):
            for i in self.adjecent:
                if(i.bomb == False and i.hidden):
                    i.hidden = False
                    i.setDisplay()
                    if(i.countAdjecentBombs()==0):
                        i.refealInnocents()

    def setDisplay(self):
        if(self.marked):
            self.display = self.chars[3]
        else:
            if(self.hidden):
                self.display = self.chars[0]
            else:
                if(self.countAdjecentBombs() == 0):
                    self.display = self.chars[1]
                else:
                    self.display = self.countAdjecentBombs()
                if(self.bomb):
                    self.display = self.chars[2]
                
    
