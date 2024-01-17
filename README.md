# Rubik's Cube Automation

## A fully functional Rubik's Cube simulation tool that displays a 2D Rubik's Cube and allows the user to make any rotation of choice or to have the program automatically solve the cube.

## This is the Rubik's Cube that you are most likely familiar with

![Program Interface](/Images/exampleRubiksCube.jpg)

## This what the 2D representation looks like on the interface

![Program Interface](/Images/openingRubiksCubeScreen.png)

The buttons with with one letter represent each of the 12 possible cube rotations. A lone letter represents a clockwise turn when you are facing that respective side and a letter with an apostrophe next to it represents a counter clockwise turn.

![Program Interface](/Images/openingRubiksCubeScreenEdited.png)

### The letters correspond to the following sides:

U - Top

L - Left

F - Front

R - Right

B - Back

D - Bottom

## An example F' turn would look like

![Program Interface](/Images/displayAfterFPrimeMove.png)



### The algorithms behind solving the Rubik's Cube in this program are inspired by the popular CFOP solving method.

## Scramble
### To show an example solve we will randomly scramble the cube

![Program Interface](/Images/openingRubiksCubeScreenPointingToScramble.png)

### You can follow along with the example by manually scrambling the cube by executing the same moves shown below.

![Program Interface](/Images/showRandomScramble.png)

# Solving The Cube
## 1️⃣ Cross
### The first step in solving the cube using CFOP is to solve the cross

![Program Interface](/Images/crossSolved.png)

### A solved cross will result in the bottom face having all four edge pieces being white, along with their respective secondary colors matching with the middle piece of the face they are on.

![Program Interface](/Images/crossSolvedEdited.png)

## 2️⃣ F2L (First Two Layers)
### The second step is to solve the first two layers of the cube by combining a white corner piece with their corresponding edge piece.

![Program Interface](/Images/F2LSolved.png)

### This step is the bulk of the total solution and is completed when every piece in the first two layers are in their final position.

![Program Interface](/Images/F2LSolvedEdited.png)

## 3️⃣ OLL (orientation of the last layer)
### The third step is to solve the top face of the cube, which in this case is yellow.

![Program Interface](/Images/OLLSolved.png)

### After solving the top, the only pieces out of place are the ones in the top layer

![Program Interface](/Images/OLLSolvedEdited.png)

## 4️⃣ PLL (permutation of the last layer)
### The fourth and final step is to place each piece in the top layer into their final position, resulting in a solved cube.

![Program Interface](/Images/PLLSolved.png)

# The Cube Has Been Solved!