import tkinter as tk
from time import *
import cubeController as cc


class makeCube(cc.cubeController):
    def __init__(self, left, front, right, back, top, bottom):
        self.left = left
        self.front = front
        self.right = right
        self.back = back
        self.top = top
        self.bottom = bottom
        self.frames = [[],[],[],[],[],[]]
        self.popUpWindow = tk.Tk()
        self.movesExecuted = []
        self.skippedRows = 5
        self.skippedColumns = 3
        self.fillFrames(self.left, self.front, self.right, self.back, self.top, self.bottom)
        self.moveFunctions = cc.cubeController(self.left, self.front, self.right, self.back, self.top, self.bottom, self.frames, self.popUpWindow)

        self.makePopUpWindow()

    def fillFrames(self, leftColors, frontColors, rightColors, backColors, topColors, bottomColors):
        horizontalSides = [leftColors, frontColors, rightColors, backColors]

        for i, face in enumerate(horizontalSides, start=1):       # horizontal rubiks cube faces
            for j, cellColor in enumerate(face, start=1):   
                frame = tk.Frame(self.popUpWindow, width=50, height=50, bg=cellColor, relief=tk.RAISED, borderwidth=2)
                if ((j-1)%3+1) == 1:    # first column
                    frame.grid(row=(j-1)//3+self.skippedRows, column=(((j-1)%3+1) + ((i-1)*4)) + self.skippedColumns, padx=(1, 0), pady=0)
                elif ((j-1)%3+1) == 3:  # third column
                    frame.grid(row=(j-1)//3+self.skippedRows, column=(((j-1)%3+1) + ((i-1)*4)) + self.skippedColumns, padx=(0, 1), pady=0)
                else:                   # second column
                    frame.grid(row=(j-1)//3+self.skippedRows, column=(((j-1)%3+1) + ((i-1)*4)) + self.skippedColumns, padx=(0, 0), pady=0)
                self.frames[i-1].append(frame)
  
        verticalSides = [topColors, bottomColors]

        for i,  face in enumerate(verticalSides, start=1):       # vertical rubiks cube faces
            for j, cellColor in enumerate(face, start=1):
                frame = tk.Frame(self.popUpWindow, width=50, height=50, bg=cellColor, relief=tk.RAISED, borderwidth=2)
                if ((j-1)//3) == 0:     # first row
                    if ((j-1)%3+1) == 1:    # first column
                        frame.grid(row=((j-1)//3) + (i-1)*7 + 1, column=(j-1)%3+5 + self.skippedColumns, padx= (1, 0), pady= (2,0))
                    else:
                        frame.grid(row=((j-1)//3) + (i-1)*7 + 1, column=(j-1)%3+5 + self.skippedColumns, padx= (0, 0), pady= (2,0))
                
                elif ((j-1)//3) == 1:   # second row
                    if ((j-1)%3+1) == 1:    # first column
                        frame.grid(row=((j-1)//3) + (i-1)*7 + 1, column=(j-1)%3+5 + self.skippedColumns, padx= (1, 0), pady= (0,0))
                    else:
                        frame.grid(row=((j-1)//3) + (i-1)*7 + 1, column=(j-1)%3+5 + self.skippedColumns, padx= (0, 0), pady= (0,0))
                    
                else:                   # third row
                    if ((j-1)%3+1) == 1:    # first column
                        frame.grid(row=((j-1)//3) + (i-1)*7 + 1, column=(j-1)%3+5 + self.skippedColumns, padx= (1, 0), pady= (0,2))
                    else: 
                        frame.grid(row=((j-1)//3) + (i-1)*7 + 1, column=(j-1)%3+5 + self.skippedColumns, padx= (0, 0), pady= (0,2))
                    
                self.frames[i+3].append(frame)

    def makePopUpWindow(self):  # make pop up window
        
        self.popUpWindow.title('Rubiks Cube')
        self.popUpWindow.geometry('1380x650')
        
        moveLabels = ['R', 'R\'', 'L', 'L\'', 'U', 'U\'', 'F', 'F\'', 'B', 'B\'', 'D', 'D\'', '   Scramble  ', '    Reset   ', 
                      'Solve Cross ', 'Solve F2L',
                      '  Solve OLL  ', 'Solve PLL', ' Solve Cube ']
        
        functions = [self.moveFunctions.R, self.moveFunctions.RPrime, 
                     self.moveFunctions.L, self.moveFunctions.LPrime, 
                     self.moveFunctions.U, self.moveFunctions.UPrime, 
                     self.moveFunctions.F, self.moveFunctions.FPrime, 
                     self.moveFunctions.B, self.moveFunctions.BPrime, 
                     self.moveFunctions.D, self.moveFunctions.DPrime, 
                     self.moveFunctions.randomScramble, self.moveFunctions.resetCube,
                     self.moveFunctions.solveCross, self.moveFunctions.solveF2L,
                     self.moveFunctions.solveOLL, self.moveFunctions.solvePLL,
                     self.moveFunctions.solveCube]
        
        for i, buttonCommand in enumerate(functions):
            actualButton = tk.Button(self.popUpWindow, text=moveLabels[i], command=buttonCommand)
            actualButton.grid(row=i//2+5, column=i%2)

        self.popUpWindow.mainloop()
        
if __name__ == '__main__':

    edges = [['white', 'green'], ['white', 'orange'], ['white', 'blue'], ['white', 'red'], 
             ['yellow', 'green'], ['yellow', 'red'], ['yellow', 'blue'], ['yellow', 'orange'], 
             ['orange', 'green'], ['orange', 'blue'], ['red', 'green'], ['red', 'blue']]
    
    corners = [['white', 'orange', 'blue'], ['white', 'orange', 'green'], 
               ['white', 'red', 'blue'], ['white', 'red', 'green'], 
               ['yellow', 'red', 'blue'], ['yellow', 'red', 'green'], 
               ['yellow', 'orange', 'blue'], ['yellow', 'orange', 'green']]


    frontSide = ['orange']*9
    rightSide = ['blue']*9
    backSide = ['red']*9
    leftSide = ['green']*9
    topSide = ['yellow']*9
    bottomSide = ['white']*9
    
    cube = makeCube(leftSide, frontSide, rightSide, backSide, topSide, bottomSide)