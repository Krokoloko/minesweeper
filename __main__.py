import os
import random
from board import board
from tile import tile
clear = lambda: os.system('cls')



""" 0:hidden 1:blank 2:Bomb(revealed) 3:Check    """
chars = ['▓','░','#','!']
states = ["app", "game", "game over",]
state = states[0]

mineField = board.Board(20,25,chars)

def HelpMe():
    for i in funcList:
        print("\n" + funcList[i][2] + " : " + funcList[i][1] + " : " + funcList[i][4])

def About():
    print("\n This is a minesweeper game I'm making. \n Type \'help me\' if you want to see the command list. \n Or type \'new game\' to start a new game.")

def NewGame():
    global state
    state = states[1]
    
    mineField.emptyBoard(tile.Tile(0,0,False,chars))
    
    for x in range(mineField.width):
        for y in range(mineField.height):
            mineField.fill(x,y,tile.Tile(x,y,False,chars))
    
    while(mineField.countBombs() < mineField.width*mineField.height/10):
        chance = [random.randint(0,mineField.width-1),random.randint(0,mineField.height-1)]
        if(not mineField.grid[chance[1]][chance[0]].bomb):
            mineField.grid[chance[1]][chance[0]].bomb = True

    for x in range(mineField.width):
        for y in range(mineField.height):
            mineField.grid[y][x].getAdjecent(mineField)
    

def OpenGame():
    global state
    state = states[1]
    pass

def Status():
    print(state)
    pass

def CloseGame():
    global state
    state = states[0]
    pass

def CloseApp():
    print("See ya next time!")
    sys.exit(0)

"""index: [function,description,functionString,object,group] """

funcList = {0:[HelpMe,"Shows all the functions and descriptions.","help me",None,"any"],
            1:[About,"About this application.","about",None,"app"],
            2:[CloseApp,"Closes the application.","close",None,"app"],
            3:[NewGame,"Starts a new game.", "new game",None,"app"],
            4:[Status,"Gives the status of your game.","status", None, "game"],
            5:[CloseGame,"Closes the game and saves the game progress.","close", None, "game"],
            6:[OpenGame,"Starts the game based on the game progress.","open", None, "app"],
            7:[mineField.Reveal,"Reveals the inputted tile.","reveal",None,"game"],
            8:[mineField.Mark,"Marks the inputted tile.","mark",None,"game"]
            }
    
def Main():
    start = True
    while True:
        clear()
        global state
        if(start):
            About()
            start = not start
        if(state == states[1]):
            mineField.update()
            if(mineField.status == "game over"):
                for x in range(mineField.width):
                    for y in range(mineField.height):
                        if(mineField.grid[y][x].bomb):
                            mineField.grid[y][x].hidden = False
                mineField.status = "new game"
                
                print("Game over type new game to retry")
            mineField.printBoard()
            
                
        
        command = input()
        try:
            for i in funcList:
                if funcList[i][2] == command:
                    if(funcList[i][4] == state or funcList[i][4] == "any"):
                        funcList[i][0]()
                        
                    else:
                        print("Can\'t use the command at this moment.")
                    
        except KeyError:
            print("No such command exists. \nBe sure to type \'helpMe\' to look for appropiate commands.")



if(__name__ == '__main__'):
    Main()
