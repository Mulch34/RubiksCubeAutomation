from time import *

class cubeRotationMoves():
    def __init__(self, left, front, right, back, top, bottom, frames, popUpWindow):
        self.left = left
        self.front = front
        self.right = right
        self.back = back
        self.top = top
        self.bottom = bottom

        self.frames = frames
        self.popUpWindowFromOtherFile = popUpWindow

        # set the time between moves (in seconds)
        self.timeBetweenMoves = 0.1
        self.printMoves = False

        self.numOfMoves = 0

    # All Moves Are When Orange Is On The Front Side Of The Cube
              
    def R(self):    # turn right side of cube clockwise
        newFront = self.front[:2]+[self.bottom[2]]+self.front[3:5]+[self.bottom[5]]+self.front[6:8]+[self.bottom[8]]
        newTop = self.top[:2]+[self.front[2]]+self.top[3:5]+[self.front[5]]+self.top[6:8]+[self.front[8]]
        newBack = [self.top[8]]+self.back[1:3]+[self.top[5]]+self.back[4:6]+[self.top[2]]+self.back[7:9]
        newBottom = self.bottom[:2]+[self.back[6]]+self.bottom[3:5]+[self.back[3]]+self.bottom[6:8]+[self.back[0]]
        newRight = [self.right[6]]+[self.right[3]]+[self.right[0]]+[self.right[7]]+[self.right[4]]+[self.right[1]]+[self.right[8]]+[self.right[5]]+[self.right[2]]
        newLeft = self.left
        newSides = [newLeft, newFront, newRight, newBack, newTop, newBottom]
        
        self.assignNewColors(newFront, newTop, newBack, newBottom, newRight, newLeft, newSides)
        if self.printMoves:
            print('R')
        self.popUpWindowFromOtherFile.update()
        sleep(self.timeBetweenMoves)

        self.numOfMoves += 1

        return newFront, newTop, newBack, newBottom, newRight, newLeft

    def RPrime(self):    # turn right side of cube counter clockwise
        newFront = self.front[:2]+[self.top[2]]+self.front[3:5]+[self.top[5]]+self.front[6:8]+[self.top[8]]
        newTop = self.top[:2]+[self.back[6]]+self.top[3:5]+[self.back[3]]+self.top[6:8]+[self.back[0]]
        newBack = [self.bottom[8]]+self.back[1:3]+[self.bottom[5]]+self.back[4:6]+[self.bottom[2]]+self.back[7:9]
        newBottom = self.bottom[:2]+[self.front[2]]+self.bottom[3:5]+[self.front[5]]+self.bottom[6:8]+[self.front[8]]
        newRight = [self.right[2]]+[self.right[5]]+[self.right[8]]+[self.right[1]]+[self.right[4]]+[self.right[7]]+[self.right[0]]+[self.right[3]]+[self.right[6]]
        newLeft = self.left
        newSides = [newLeft, newFront, newRight, newBack, newTop, newBottom]
        
        self.assignNewColors(newFront, newTop, newBack, newBottom, newRight, newLeft, newSides)
        if self.printMoves:
            print('R\'')
        self.popUpWindowFromOtherFile.update()
        sleep(self.timeBetweenMoves)

        self.numOfMoves += 1

        return newFront, newTop, newBack, newBottom, newRight, newLeft

    def L(self):    # turn left side of cube clockwise
        newFront = [self.top[0]]+self.front[1:3]+[self.top[3]]+self.front[4:6]+[self.top[6]]+self.front[7:9]
        newTop = [self.back[8]]+self.top[1:3]+[self.back[5]]+self.top[4:6]+[self.back[2]]+self.top[7:9]
        newBack = self.back[0:2]+[self.bottom[6]]+self.back[3:5]+[self.bottom[3]]+self.back[6:8]+[self.bottom[0]]
        newBottom = [self.front[0]]+self.bottom[1:3]+[self.front[3]]+self.bottom[4:6]+[self.front[6]]+self.bottom[7:9]
        newRight = self.right
        newLeft = [self.left[6]]+[self.left[3]]+[self.left[0]]+[self.left[7]]+[self.left[4]]+[self.left[1]]+[self.left[8]]+[self.left[5]]+[self.left[2]]
        newSides = [newLeft, newFront, newRight, newBack, newTop, newBottom]
        
        self.assignNewColors(newFront, newTop, newBack, newBottom, newRight, newLeft, newSides)
        if self.printMoves:
            print('L')
        self.popUpWindowFromOtherFile.update()
        sleep(self.timeBetweenMoves)

        self.numOfMoves += 1

        return newFront, newTop, newBack, newBottom, newRight, newLeft

    def LPrime(self):    # turn left side of cube clockwise
        newFront = [self.bottom[0]]+self.front[1:3]+[self.bottom[3]]+self.front[4:6]+[self.bottom[6]]+self.front[7:9]
        newTop = [self.front[0]]+self.top[1:3]+[self.front[3]]+self.top[4:6]+[self.front[6]]+self.top[7:9]
        newBack = self.back[0:2]+[self.top[6]]+self.back[3:5]+[self.top[3]]+self.back[6:8]+[self.top[0]]
        newBottom = [self.back[8]]+self.bottom[1:3]+[self.back[5]]+self.bottom[4:6]+[self.back[2]]+self.bottom[7:9]
        newRight = self.right
        newLeft = [self.left[2]]+[self.left[5]]+[self.left[8]]+[self.left[1]]+[self.left[4]]+[self.left[7]]+[self.left[0]]+[self.left[3]]+[self.left[6]]
        newSides = [newLeft, newFront, newRight, newBack, newTop, newBottom]
        
        self.assignNewColors(newFront, newTop, newBack, newBottom, newRight, newLeft, newSides)
        if self.printMoves:
            print('L\'')
        self.popUpWindowFromOtherFile.update()
        sleep(self.timeBetweenMoves)

        self.numOfMoves += 1

        return newFront, newTop, newBack, newBottom, newRight, newLeft

    def U(self):    # turn top side of cube clockwise
        newFront = self.right[0:3]+self.front[3:9]
        newTop = [self.top[6]]+[self.top[3]]+[self.top[0]]+[self.top[7]]+[self.top[4]]+[self.top[1]]+[self.top[8]]+[self.top[5]]+[self.top[2]]
        newBack = self.left[0:3]+self.back[3:9]
        newBottom = self.bottom
        newRight = self.back[0:3]+self.right[3:9]
        newLeft = self.front[0:3]+self.left[3:9]
        newSides = [newLeft, newFront, newRight, newBack, newTop, newBottom]
        
        self.assignNewColors(newFront, newTop, newBack, newBottom, newRight, newLeft, newSides)
        if self.printMoves:
            print('U')
        self.popUpWindowFromOtherFile.update()
        sleep(self.timeBetweenMoves)

        self.numOfMoves += 1

        return newFront, newTop, newBack, newBottom, newRight, newLeft

    def UPrime(self):    # turn top side of cube counter clockwise
        newFront = self.left[0:3]+self.front[3:9]
        newTop = [self.top[2]]+[self.top[5]]+[self.top[8]]+[self.top[1]]+[self.top[4]]+[self.top[7]]+[self.top[0]]+[self.top[3]]+[self.top[6]]
        newBack = self.right[0:3]+self.back[3:9]
        newBottom = self.bottom
        newRight = self.front[0:3]+self.right[3:9]
        newLeft = self.back[0:3]+self.left[3:9]
        newSides = [newLeft, newFront, newRight, newBack, newTop, newBottom]

        self.assignNewColors(newFront, newTop, newBack, newBottom, newRight, newLeft, newSides)
        if self.printMoves:
            print('U\'')
        self.popUpWindowFromOtherFile.update()
        sleep(self.timeBetweenMoves)

        self.numOfMoves += 1

        return newFront, newTop, newBack, newBottom, newRight, newLeft

    def F(self):    # turn front side of cube clockwise
        newFront = [self.front[6]]+[self.front[3]]+[self.front[0]]+[self.front[7]]+[self.front[4]]+[self.front[1]]+[self.front[8]]+[self.front[5]]+[self.front[2]]
        newTop = self.top[0:6]+[self.left[8]]+[self.left[5]]+[self.left[2]]
        newBack = self.back
        newBottom = [self.right[6]]+[self.right[3]]+[self.right[0]]+self.bottom[3:9]
        newRight = [self.top[6]]+self.right[1:3]+[self.top[7]]+self.right[4:6]+[self.top[8]]+self.right[7:9]
        newLeft = self.left[0:2]+[self.bottom[0]]+self.left[3:5]+[self.bottom[1]]+self.left[6:8]+[self.bottom[2]]
        newSides = [newLeft, newFront, newRight, newBack, newTop, newBottom]
        
        self.assignNewColors(newFront, newTop, newBack, newBottom, newRight, newLeft, newSides)
        if self.printMoves:
            print('F')
        self.popUpWindowFromOtherFile.update()
        sleep(self.timeBetweenMoves)

        self.numOfMoves += 1

        return newFront, newTop, newBack, newBottom, newRight, newLeft
    
    def FPrime(self):    # turn front side of cube counter clockwise
        newFront = [self.front[2]]+[self.front[5]]+[self.front[8]]+[self.front[1]]+[self.front[4]]+[self.front[7]]+[self.front[0]]+[self.front[3]]+[self.front[6]]
        newTop = self.top[0:6]+[self.right[0]]+[self.right[3]]+[self.right[6]]
        newBack = self.back
        newBottom = [self.left[2]]+[self.left[5]]+[self.left[8]]+self.bottom[3:9]
        newRight = [self.bottom[2]]+self.right[1:3]+[self.bottom[1]]+self.right[4:6]+[self.bottom[0]]+self.right[7:9]
        newLeft = self.left[0:2]+[self.top[8]]+self.left[3:5]+[self.top[7]]+self.left[6:8]+[self.top[6]]
        newSides = [newLeft, newFront, newRight, newBack, newTop, newBottom]
        
        self.assignNewColors(newFront, newTop, newBack, newBottom, newRight, newLeft, newSides)
        if self.printMoves:
            print('F\'')
        self.popUpWindowFromOtherFile.update()
        sleep(self.timeBetweenMoves)

        self.numOfMoves += 1

        return newFront, newTop, newBack, newBottom, newRight, newLeft

    def B(self):    # turn back side of cube clockwise
        newFront = self.front
        newTop = [self.right[2]]+[self.right[5]]+[self.right[8]]+self.top[3:9]
        newBack = [self.back[6]]+[self.back[3]]+[self.back[0]]+[self.back[7]]+[self.back[4]]+[self.back[1]]+[self.back[8]]+[self.back[5]]+[self.back[2]]
        newBottom = self.bottom[0:6]+[self.left[0]]+[self.left[3]]+[self.left[6]]
        newRight = self.right[0:2]+[self.bottom[8]]+self.right[3:5]+[self.bottom[7]]+self.right[6:8]+[self.bottom[6]]
        newLeft = [self.top[2]]+self.left[1:3]+[self.top[1]]+self.left[4:6]+[self.top[0]]+self.left[7:9]
        newSides = [newLeft, newFront, newRight, newBack, newTop, newBottom]
        
        self.assignNewColors(newFront, newTop, newBack, newBottom, newRight, newLeft, newSides)
        if self.printMoves:
            print('B')
        self.popUpWindowFromOtherFile.update()
        sleep(self.timeBetweenMoves)

        self.numOfMoves += 1

        return newFront, newTop, newBack, newBottom, newRight, newLeft

    def BPrime(self):    # turn back side of cube counter clockwise
        newFront = self.front
        newTop = [self.left[6]]+[self.left[3]]+[self.left[0]]+self.top[3:9]
        newBack = [self.back[2]]+[self.back[5]]+[self.back[8]]+[self.back[1]]+[self.back[4]]+[self.back[7]]+[self.back[0]]+[self.back[3]]+[self.back[6]]
        newBottom = self.bottom[0:6]+[self.right[8]]+[self.right[5]]+[self.right[2]]
        newRight = self.right[0:2]+[self.top[0]]+self.right[3:5]+[self.top[1]]+self.right[6:8]+[self.top[2]]
        newLeft = [self.bottom[6]]+self.left[1:3]+[self.bottom[7]]+self.left[4:6]+[self.bottom[8]]+self.left[7:9]
        newSides = [newLeft, newFront, newRight, newBack, newTop, newBottom]
        
        self.assignNewColors(newFront, newTop, newBack, newBottom, newRight, newLeft, newSides)
        if self.printMoves:
            print('B\'')
        self.popUpWindowFromOtherFile.update()
        sleep(self.timeBetweenMoves)

        self.numOfMoves += 1

        return newFront, newTop, newBack, newBottom, newRight, newLeft

    def D(self):    # turn bottom side of cube clockwise
        newFront = self.front[0:6]+self.left[6:9]
        newTop = self.top
        newBack = self.back[0:6]+self.right[6:9]
        newBottom = [self.bottom[6]]+[self.bottom[3]]+[self.bottom[0]]+[self.bottom[7]]+[self.bottom[4]]+[self.bottom[1]]+[self.bottom[8]]+[self.bottom[5]]+[self.bottom[2]]
        newRight = self.right[0:6]+self.front[6:9]
        newLeft = self.left[0:6]+self.back[6:9]
        newSides = [newLeft, newFront, newRight, newBack, newTop, newBottom]
        
        self.assignNewColors(newFront, newTop, newBack, newBottom, newRight, newLeft, newSides)
        if self.printMoves:
            print('D')
        self.popUpWindowFromOtherFile.update()
        sleep(self.timeBetweenMoves)

        self.numOfMoves += 1

        return newFront, newTop, newBack, newBottom, newRight, newLeft
    
    def DPrime(self):    # turn bottom side of cube counter clockwise
        newFront = self.front[0:6]+self.right[6:9]
        newTop = self.top
        newBack = self.back[0:6]+self.left[6:9]
        newBottom = [self.bottom[2]]+[self.bottom[5]]+[self.bottom[8]]+[self.bottom[1]]+[self.bottom[4]]+[self.bottom[7]]+[self.bottom[0]]+[self.bottom[3]]+[self.bottom[6]]
        newRight = self.right[0:6]+self.back[6:9]
        newLeft = self.left[0:6]+self.front[6:9]
        newSides = [newLeft, newFront, newRight, newBack, newTop, newBottom]
        
        self.assignNewColors(newFront, newTop, newBack, newBottom, newRight, newLeft, newSides)
        if self.printMoves:
            print('D\'')
        self.popUpWindowFromOtherFile.update()
        sleep(self.timeBetweenMoves)

        self.numOfMoves += 1

        return newFront, newTop, newBack, newBottom, newRight, newLeft


    def assignNewColors(self, newFront, newTop, newBack, newBottom, newRight, newLeft, newSides):
        for i, oldFaceFrameArray in enumerate(self.frames):
                for j, oldColorFrame in enumerate(oldFaceFrameArray):
                    oldColorFrame.configure(bg=newSides[i][j])

        self.front = newFront
        self.top = newTop
        self.back = newBack
        self.bottom = newBottom
        self.right = newRight
        self.left = newLeft
