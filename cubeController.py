import tkinter as tk
import random
from time import *
from cubeMoves import cubeRotationMoves

class cubeController():  
    def __init__(self, left, front, right, back, top, bottom, frames, popUpWindow):
        self.left = left
        self.front = front
        self.right = right
        self.back = back
        self.top = top
        self.bottom = bottom

        self.initialLeft = left
        self.initialFront = front
        self.initialRight = right
        self.initialBack = back
        self.initialTop = top
        self.initialBottom = bottom

        self.moves = cubeRotationMoves(left, front, right, back, top, bottom, frames, popUpWindow)


        self.assignNewColors = self.moves.assignNewColors

        self.currentOtherEdgeFace = None
        self.currentPrimaryEdgePiecePosition = None

        self.firstEdgePiecePositionF2L = None
        self.secondEdgePiecePositionF2L = None

        self.firstEdgePieceSideF2L = None
        self.secondEdgePieceSideF2L = None

        self.secondEdgePieceColorF2L = None

        self.comparisonEdgePieceColorF2L = None
        self.secondEdgePieceColorF2L = None

        self.comparisonEdgePieceFaceF2L = None

        self.crossSolved = False
        self.F2LSolved = False
        self.OLLSolved = False
        self.PLLSolved = False

        self.cornerSpot = None
        self.cornerPieceFace = None
        self.horizontalColors = ['red', 'green', 'orange', 'blue']
        self.edgeLocations = ['1', '3', '7', '5']
        self.yellowToWhiteMoves = {'1': self.B, '3': self.L, '7': self.FPrime, '5': self.RPrime}
        self.solvingCube = False
        self.yellowToWhite = 0
        self.otherEdge = None
        self.frames = frames
        self.numberOfRandomMoves = 20
        self.cubeCorners = []
        self.numOfTests = 10

        self.turnCounterClockWiseOnce = [self.UPrime]
        self.turnCounterClockWiseTwice = [self.UPrime, self.UPrime]
        self.turnClockWiseOnce = [self.U]

        self.shiftingEdgesToTheRightPLLAlgorithm = [self.R, self.UPrime, self.R, self.U, self.R,
                                                   self.U, self.R, self.UPrime, self.RPrime,
                                                   self.UPrime, self.R, self.R]
        
        self.shiftingEdgesToTheLeftPLLAlgorithm = [self.LPrime, self.U, self.LPrime, self.UPrime,
                                                   self.LPrime, self.UPrime, self.LPrime, self.U,
                                                   self.L, self.U, self.LPrime, self.LPrime]

        self.movesForfirstPLLAlgorithm = {
            0: 'orientation is correct',
            1: 'turnClockwiseOnce',
            2: 'turnCounterClockwiseTwice',
            3: 'turnCounterClockwiseOnce'
        }

        self.rotationToMatchTopLayer = {
            'red': 'orientation is correct',
            'green': 'turnCounterClockwiseOnce',
            'orange': 'turnCounterClockwiseTwice',
            'blue': 'turnClockwiseOnce',
        }

        self.rotations = {
            'orientation is correct': [],
            'turnCounterClockwiseOnce': self.turnCounterClockWiseOnce,
            'turnCounterClockwiseTwice': self.turnCounterClockWiseTwice,
            'turnClockwiseOnce': self.turnClockWiseOnce,
        }

        self.movesForOLLPermutations = {
            'headlightsAndOuterOLL': [self.R, self.UPrime, self.UPrime, self.RPrime, self.RPrime, self.UPrime,
                                      self.R, self.R, self.UPrime, self.R, self.R, self.UPrime, self.UPrime, self.R],
            'arrowNotNormalOLL': [self.R, self.UPrime, self.UPrime, self.RPrime, self.UPrime, self.R, self.UPrime, self.RPrime],
            'arrowNormalOLL': [self.R, self.U, self.RPrime, self.U, self.R, self.UPrime, self.UPrime, self.RPrime],
            'onlyOuterOLL': [self.L, self.F, self.RPrime, self.FPrime, self.LPrime, self.F, self.R, self.FPrime],
            'headlightsOLL': [self.R, self.UPrime, self.UPrime, self.RPrime, self.UPrime, self.R, self.U, self.RPrime, self.UPrime, self.R, self.UPrime, self.RPrime],
            'oneHeadlightsOLL': [self.R, self.R, self.D, self.RPrime, self.UPrime, self.UPrime, self.R, self.DPrime, self.RPrime, self.UPrime, self.UPrime, self.RPrime],
            'diagonalOLL': [self.FPrime, self.L, self.F, self.RPrime, self.FPrime, self.LPrime, self.F, self.R],

            'straightLineOLL': [self.F, self.R, self.U, self.RPrime, self.UPrime, self.FPrime],
            'lShapedOLL': [self.F, self.U, self.R, self.UPrime, self.RPrime, self.FPrime],
            'dotOLL': [self.F, self.R, self.U, self.RPrime, self.UPrime, self.FPrime]
        }

        self.headlightsAndOuterOLL = [[['''0,0,1,
                                         1,0,1,0,0,
                                         0,1,1,1,0,
                                         1,0,1,0,0,
                                           0,0,1''', 'orientation is correct'],
                                       ['''0,0,0, 
                                         1,0,1,0,1,
                                         0,1,1,1,0,
                                         0,0,1,0,0,
                                           1,0,1''', 'turnClockwiseOnce'],
                                       ['''1,0,0,
                                         0,0,1,0,1,
                                         0,1,1,1,0,
                                         0,0,1,0,1,
                                           1,0,0''', 'turnCounterClockwiseTwice'],
                                       ['''1,0,1,
                                         0,0,1,0,0,
                                         0,1,1,1,0,
                                         1,0,1,0,1,
                                           0,0,0''', 'turnCounterClockwiseOnce']], 'headlightsAndOuterOLL']

        self.arrowNotNormalOLL = [[['''0,0,0,
                                     1,0,1,1,0,
                                     0,1,1,1,0,
                                     0,0,1,0,1,
                                       1,0,0''', 'orientation is correct'],
                                   ['''0,0,1,
                                     0,1,1,0,0,
                                     0,1,1,1,0,
                                     0,0,1,0,1,
                                       1,0,0''', 'turnClockwiseOnce'],
                                   ['''0,0,1, 
                                     1,0,1,0,0,
                                     0,1,1,1,0,
                                     0,1,1,0,1,
                                       0,0,0''', 'turnCounterClockwiseTwice'],
                                   ['''0,0,1,
                                     1,0,1,0,0,
                                     0,1,1,1,0,
                                     0,0,1,1,0,
                                       1,0,0''', 'turnCounterClockwiseOnce']], 'arrowNotNormalOLL']
        
        self.arrowNormalOLL =    [[['''1,0,0, 
                                     0,0,1,0,1,
                                     0,1,1,1,0,
                                     0,1,1,0,0,
                                       0,0,1''', 'orientation is correct'],
                                   ['''1,0,0,
                                     0,0,1,0,1,
                                     0,1,1,1,0,
                                     1,0,1,1,0,
                                       0,0,0''', 'turnClockwiseOnce'],
                                   ['''1,0,0,
                                     0,0,1,1,0,
                                     0,1,1,1,0,
                                     1,0,1,0,0,
                                       0,0,1''', 'turnCounterClockwiseTwice'],
                                   ['''0,0,0,
                                     0,1,1,0,1,
                                     0,1,1,1,0,
                                     1,0,1,0,0,
                                       0,0,1''', 'turnCounterClockwiseOnce']], 'arrowNormalOLL']

        self.onlyOuterOLL =      [[['''1,0,0, 
                                     0,0,1,1,0,
                                     0,1,1,1,0,
                                     0,0,1,1,0,
                                       1,0,0''', 'orientation is correct'],
                                   ['''0,0,0,
                                     0,1,1,1,0,
                                     0,1,1,1,0,
                                     1,0,1,0,1,
                                       0,0,0''', 'turnClockwiseOnce'],
                                   ['''0,0,1,
                                     0,1,1,0,0,
                                     0,1,1,1,0,
                                     0,1,1,0,0,
                                       0,0,1''', 'turnCounterClockwiseTwice'],
                                   ['''0,0,0,
                                     1,0,1,0,1,
                                     0,1,1,1,0,
                                     0,1,1,1,0,
                                       0,0,0''', 'turnCounterClockwiseOnce']], 'onlyOuterOLL']

        self.headlightsOLL =     [[['''1,0,1, 
                                     0,0,1,0,0,
                                     0,1,1,1,0,
                                     0,0,1,0,0,
                                       1,0,1''', 'orientation is correct'],
                                   ['''0,0,0,
                                     1,0,1,0,1,
                                     0,1,1,1,0,
                                     1,0,1,0,1,
                                       0,0,0''', 'turnCounterClockwiseOnce']], 'headlightsOLL']

        self.oneHeadlightsOLL =  [[['''0,0,0, 
                                     0,1,1,1,0,
                                     0,1,1,1,0,
                                     0,0,1,0,0,
                                       1,0,1''', 'orientation is correct'],
                                   ['''0,0,0,
                                     0,1,1,0,1,
                                     0,1,1,1,0,
                                     0,1,1,0,1,
                                       0,0,0''', 'turnClockwiseOnce'],
                                   ['''1,0,1,
                                     0,0,1,0,0,
                                     0,1,1,1,0,
                                     0,1,1,1,0,
                                       0,0,0''', 'turnCounterClockwiseTwice'],
                                   ['''0,0,0,
                                     1,0,1,1,0,
                                     0,1,1,1,0,
                                     1,0,1,1,0,
                                       0,0,0''', 'turnCounterClockwiseOnce']], 'oneHeadlightsOLL']

        self.diagonalOLL =       [[['''0,0,0, 
                                     1,0,1,1,0,
                                     0,1,1,1,0,
                                     0,1,1,0,0,
                                       0,0,1''', 'orientation is correct'],
                                   ['''0,0,0,
                                     0,1,1,0,1,
                                     0,1,1,1,0,
                                     0,0,1,1,0,
                                       1,0,0''', 'turnClockwiseOnce'],
                                   ['''1,0,0,
                                     0,0,1,1,0,
                                     0,1,1,1,0,
                                     0,1,1,0,1,
                                       0,0,0''', 'turnCounterClockwiseTwice'],
                                   ['''0,0,1,
                                     0,1,1,0,0,
                                     0,1,1,1,0,
                                     1,0,1,1,0,
                                       0,0,0''', 'turnCounterClockwiseOnce']], 'diagonalOLL']


        self.straightLineOLL =   [[['''0,0,0, 
                                     0,0,0,0,0,
                                     0,1,1,1,0,
                                     0,0,0,0,0,
                                       0,0,0''', 'orientation is correct'],
                                   ['''0,0,0,
                                     0,0,1,0,0,
                                     0,0,1,0,0,
                                     0,0,1,0,0,
                                       0,0,0''', 'turnCounterClockwiseOnce']], 'straightLineOLL']

        self.lShapedOLL =        [[['''0,0,0, 
                                     0,0,1,0,0,
                                     0,1,1,0,0,
                                     0,0,0,0,0,
                                       0,0,0''', 'orientation is correct'],
                                   ['''0,0,0,
                                     0,0,0,0,0,
                                     0,1,1,0,0,
                                     0,0,1,0,0,
                                       0,0,0''', 'turnClockwiseOnce'],
                                   ['''0,0,0,
                                     0,0,0,0,0,
                                     0,0,1,1,0,
                                     0,0,1,0,0,
                                       0,0,0''', 'turnCounterClockwiseTwice'],
                                   ['''0,0,0,
                                     0,0,1,0,0,
                                     0,0,1,1,0,
                                     0,0,0,0,0,
                                       0,0,0''', 'turnCounterClockwiseOnce']], 'lShapedOLL']

        self.dotOLL =            [[['''0,0,0, 
                                     0,0,0,0,0,
                                     0,0,1,0,0,
                                     0,0,0,0,0,
                                       0,0,0''', 'orientation is correct']], 'dotOLL']

        self.nonFinalYellowPermutations = [self.straightLineOLL, self.lShapedOLL, self.dotOLL]

        self.possibleOLLPerumtations = {
            # headlights and outer
            self.headlightsAndOuterOLL[0][0][0].replace(' ','').replace("\n", ""): [self.headlightsAndOuterOLL[1], self.headlightsAndOuterOLL[0][0][1]],
            self.headlightsAndOuterOLL[0][1][0].replace(' ','').replace("\n", ""): [self.headlightsAndOuterOLL[1], self.headlightsAndOuterOLL[0][1][1]],
            self.headlightsAndOuterOLL[0][2][0].replace(' ','').replace("\n", ""): [self.headlightsAndOuterOLL[1], self.headlightsAndOuterOLL[0][2][1]],
            self.headlightsAndOuterOLL[0][3][0].replace(' ','').replace("\n", ""): [self.headlightsAndOuterOLL[1], self.headlightsAndOuterOLL[0][3][1]],
            # arrow not normal
            self.arrowNotNormalOLL[0][0][0].replace(' ','').replace("\n", ""): [self.arrowNotNormalOLL[1], self.arrowNotNormalOLL[0][0][1]],
            self.arrowNotNormalOLL[0][1][0].replace(' ','').replace("\n", ""): [self.arrowNotNormalOLL[1], self.arrowNotNormalOLL[0][1][1]],
            self.arrowNotNormalOLL[0][2][0].replace(' ','').replace("\n", ""): [self.arrowNotNormalOLL[1], self.arrowNotNormalOLL[0][2][1]],
            self.arrowNotNormalOLL[0][3][0].replace(' ','').replace("\n", ""): [self.arrowNotNormalOLL[1], self.arrowNotNormalOLL[0][3][1]],
            # arrow normal
            self.arrowNormalOLL[0][0][0].replace(' ','').replace("\n", ""): [self.arrowNormalOLL[1], self.arrowNormalOLL[0][0][1]],
            self.arrowNormalOLL[0][1][0].replace(' ','').replace("\n", ""): [self.arrowNormalOLL[1], self.arrowNormalOLL[0][1][1]],
            self.arrowNormalOLL[0][2][0].replace(' ','').replace("\n", ""): [self.arrowNormalOLL[1], self.arrowNormalOLL[0][2][1]],
            self.arrowNormalOLL[0][3][0].replace(' ','').replace("\n", ""): [self.arrowNormalOLL[1], self.arrowNormalOLL[0][3][1]],
            # only outer
            self.onlyOuterOLL[0][0][0].replace(' ','').replace("\n", ""): [self.onlyOuterOLL[1], self.onlyOuterOLL[0][0][1]],
            self.onlyOuterOLL[0][1][0].replace(' ','').replace("\n", ""): [self.onlyOuterOLL[1], self.onlyOuterOLL[0][1][1]],
            self.onlyOuterOLL[0][2][0].replace(' ','').replace("\n", ""): [self.onlyOuterOLL[1], self.onlyOuterOLL[0][2][1]],
            self.onlyOuterOLL[0][3][0].replace(' ','').replace("\n", ""): [self.onlyOuterOLL[1], self.onlyOuterOLL[0][3][1]],
            # headlights
            self.headlightsOLL[0][0][0].replace(' ','').replace("\n", ""): [self.headlightsOLL[1], self.headlightsOLL[0][0][1]],
            self.headlightsOLL[0][1][0].replace(' ','').replace("\n", ""): [self.headlightsOLL[1], self.headlightsOLL[0][1][1]],
            # one headlight
            self.oneHeadlightsOLL[0][0][0].replace(' ','').replace("\n", ""): [self.oneHeadlightsOLL[1], self.oneHeadlightsOLL[0][0][1]],
            self.oneHeadlightsOLL[0][1][0].replace(' ','').replace("\n", ""): [self.oneHeadlightsOLL[1], self.oneHeadlightsOLL[0][1][1]],
            self.oneHeadlightsOLL[0][2][0].replace(' ','').replace("\n", ""): [self.oneHeadlightsOLL[1], self.oneHeadlightsOLL[0][2][1]],
            self.oneHeadlightsOLL[0][3][0].replace(' ','').replace("\n", ""): [self.oneHeadlightsOLL[1], self.oneHeadlightsOLL[0][3][1]],
            # diagonal
            self.diagonalOLL[0][0][0].replace(' ','').replace("\n", ""): [self.diagonalOLL[1], self.diagonalOLL[0][0][1]],
            self.diagonalOLL[0][1][0].replace(' ','').replace("\n", ""): [self.diagonalOLL[1], self.diagonalOLL[0][1][1]],
            self.diagonalOLL[0][2][0].replace(' ','').replace("\n", ""): [self.diagonalOLL[1], self.diagonalOLL[0][2][1]],
            self.diagonalOLL[0][3][0].replace(' ','').replace("\n", ""): [self.diagonalOLL[1], self.diagonalOLL[0][3][1]]
        }

        self.edgeColorsBasedOffOfCornerSpot = {
            '1': {
                'self.back': 5,
                'self.left': 3
            },
            '2': {
                'self.right': 5,
                'self.back': 3
            },
            '3': {
                'self.front': 3,
                'self.left': 5
            },
            '4': {
                'self.front': 5,
                'self.right': 3
            },
            '5': {
                'self.front': 3,
                'self.left': 5
            },
            '6': {
                'self.front': 5,
                'self.right': 3
            },
            '7': {
                'self.back': 5,
                'self.left': 3
            },
            '8': {
                'self.right': 5,
                'self.back': 3
            }
        }

        self.gettingCornerfromBottomLayerToTopLayer = {
            '5': [self.LPrime, self.UPrime, self.L],
            '6': [self.R, self.U, self.RPrime],
            '7': [self.L, self.UPrime, self.LPrime],
            '8': [self.RPrime, self.UPrime, self.R]
        }

        self.twoEdgePiecePositionsToEdgePiece = {
            'self.top': {
                '1': '1',
                '3': '2',
                '5': '3',
                '7': '4'
            },
            'self.front': {
                '3': '5',
                '5': '6'
            },
            'self.right': {
                '5': '7'
            },
            'self.left': {
                '3': '8'
            }
        }

        self.connectingOppositeF2LPiecesEdgeOnLeft = {
            'blue': [self.RPrime, self.UPrime, self.R],
            'red': [self.BPrime, self.UPrime, self.B],
            'orange': [self.FPrime, self.UPrime, self.F],
            'green': [self.LPrime, self.UPrime, self.L]
        }

        self.connectingOppositeF2LPiecesEdgeOnRight = {
            'blue': [self.R, self.U, self.RPrime],
            'red': [self.B, self.U, self.BPrime],
            'orange': [self.F, self.U, self.FPrime],
            'green': [self.L, self.U, self.LPrime]
        }

        self.movesToSeparateOnGarbageCornerWhiteOnRightF2L = {
            'top left': [[self.BPrime, self.U, self.U, self.B], 'self.left', 'self.front'],
            'top right': [[self.RPrime, self.U, self.U, self.R], 'self.back', 'self.left'],
            'bottom left': [[self.LPrime, self.U, self.U, self.L], 'self.front', 'self.right'],
            'bottom right': [[self.FPrime, self.U, self.U, self.F], 'self.right', 'self.back']        
            }
        
        self.movesToSeparateOnGarbageCornerWhiteOnLeftF2L = {
            'top left': [[self.L, self.UPrime, self.UPrime, self.LPrime], 'self.back', 'self.right'],
            'top right': [[self.B, self.UPrime, self.UPrime, self.BPrime], 'self.right', 'self.front'],
            'bottom left': [[self.F, self.UPrime, self.UPrime, self.FPrime], 'self.left', 'self.back'],
            'bottom right': [[self.R, self.UPrime, self.UPrime, self.RPrime], 'self.front', 'self.left']        
            }

        self.faceToTurnToDependingOnWhichCornerIsGarbageEdgeOnLeft = {
            'top left': 'self.right',
            'top right': 'self.front',
            'bottom left': 'self.back',
            'bottom right': 'self.left'
        }

        self.faceToTurnToDependingOnWhichCornerIsGarbageEdgeOnRight = {
            'top left': 'self.front',
            'top right': 'self.left',
            'bottom left': 'self.right',
            'bottom right': 'self.back'
        }
        
        self.faceToTurnToDependingOnWhichCornerIsGarbageScrunchedEdgeOnRight = {
            'top left': 'self.left',
            'top right': 'self.back',
            'bottom left': 'self.front',
            'bottom right': 'self.right'
        }

        self.faceToTurnToDependingOnWhichCornerIsGarbageScrunchedEdgeOnLeft = {
            'top left': 'self.back',
            'top right': 'self.right',
            'bottom left': 'self.left',
            'bottom right': 'self.front'
        }

        self.faceToTurnToDependingOnWhichCornerIsGarbageOneTurnEdgeOnLeft = {
            'top left': 'self.right',
            'top right': 'self.front',
            'bottom left': 'self.back',
            'bottom right': 'self.left'
        }

        self.faceToTurnToDependingOnWhichCornerIsGarbageOneTurnEdgeOnRight = {
            'top left': 'self.front',
            'top right': 'self.left',
            'bottom left': 'self.right',
            'bottom right': 'self.back'
        }

        self.movesToConnectSeparateScrunchedPiecesEdgeOnRightF2L = {
            'top left': [[self.BPrime, self.UPrime, self.UPrime, self.B], 'self.right'],
            'top right': [[self.RPrime, self.UPrime, self.UPrime, self.R], 'self.front'],
            'bottom left': [[self.LPrime, self.UPrime, self.UPrime, self.L], 'self.back'],
            'bottom right': [[self.FPrime, self.UPrime, self.UPrime, self.F], 'self.left']
        }

        self.movesToConnectSeparateScrunchedPiecesEdgeOnLeftF2L = {
            'top left': [[self.L, self.U, self.U, self.LPrime], 'self.front'],
            'top right': [[self.B, self.U, self.U, self.BPrime], 'self.left'],
            'bottom left': [[self.F, self.U, self.U, self.FPrime], 'self.right'],
            'bottom right': [[self.R, self.U, self.U, self.RPrime], 'self.back']
        }

        self.insertingConstructedF2LPairWhitePieceOnTheLeft = {
            'red': [self.B, self.UPrime, self.BPrime],
            'orange': [self.F, self.UPrime, self.FPrime],
            'green': [self.L, self.UPrime, self.LPrime],
            'blue': [self.R, self.UPrime, self.RPrime]
        }

        self.movesConnectingSeparateF2LPiecesWhiteOnTop = {
            'green': {
                     # moves to connect pieces, comparison face, is white on left when pieces are connected
                'red': [[self.L, self.U, self.LPrime], 'self.left', True],
                'orange': [[self.LPrime, self.UPrime, self.UPrime, self.L], 'self.left', False]
            },
            'orange': {
                'green': [[self.F, self.U, self.FPrime], 'self.front', True],
                'blue': [[self.FPrime, self.UPrime, self.UPrime, self.F], 'self.front', False]
            },
            'red': {
                'blue': [[self.B, self.U, self.BPrime], 'self.back', True],
                'green': [[self.BPrime, self.UPrime, self.UPrime, self.B], 'self.back', False]
            },
            'blue': {
                'orange': [[self.R, self.U, self.RPrime], 'self.right', True],
                'red': [[self.RPrime, self.UPrime, self.UPrime, self.R], 'self.right', False]
            }
        }

        self.goingFromVerticalToHorizontalPairF2L = {
            'top left': [[self.L, self.UPrime, self.LPrime], 'self.front', 'Right', 'Left'],
            'top right': [[self.RPrime, self.U, self.R], 'self.front', 'Left', 'Right'],
            'bottom left': [[self.LPrime, self.U, self.L], 'self.back', 'Left', 'Right'],
            'bottom right': [[self.R, self.UPrime, self.RPrime], 'self.back', 'Right', 'Left']
        }

        self.whichWayToTurnWhiteOnTopEdgeToTheRightF2L = {
            'green': {
                'orange': [[self.LPrime, self.U, self.U, self.L, self.UPrime], 'Right'],
                'red': [[self.L, self.U, self.LPrime, self.U], 'Left']
            },
            'blue': {
                'red': [[self.RPrime, self.UPrime, self.UPrime, self.R, self.UPrime], 'Right'],
                'orange': [[self.R, self.U, self.RPrime, self.U], 'Left']
            },
            'red': {
                'green': [[self.BPrime, self.UPrime, self.UPrime, self.B, self.UPrime], 'Right'],
                'blue': [[self.B, self.U, self.BPrime, self.U], 'Left']
            },
            'orange': {
                'green': [[self.F, self.U, self.FPrime, self.U], 'Left'],
                'blue': [[self.FPrime, self.UPrime, self.UPrime, self.F, self.UPrime], 'Right']
            }
        }

        self.onePlusEdgeColorFaceWhiteOnTheRight = {
            'orange': 'self.right',
            'blue': 'self.back',
            'red': 'self.left',
            'green': 'self.front'
        }

        self.onePlusEdgeColorFaceWhiteOnTheLeft = {
            'orange': 'self.left',
            'blue': 'self.front',
            'red': 'self.right',
            'green': 'self.back'
        }

        self.topRotationsToMakeVerticalPairF2L = {
            '1': {
                '5': self.turnCounterClockWiseOnce,
                '6': self.turnCounterClockWiseTwice,
                '7': self.turnClockWiseOnce
            },
            '2': {
                '8': self.turnCounterClockWiseOnce,
                '5': self.turnCounterClockWiseTwice,
                '6': self.turnClockWiseOnce
            },
            '3': {
                '6': self.turnCounterClockWiseOnce,
                '7': self.turnCounterClockWiseTwice,
                '8': self.turnClockWiseOnce
            },
            '4': {
                '7': self.turnCounterClockWiseOnce,
                '8': self.turnCounterClockWiseTwice,
                '5': self.turnClockWiseOnce
            }

        }

        self.cornerRelationMoves = {
            'white on top piece': {
                'top left': {
                    'edge below z': {
                                  # (function, which corner)
                        'matching': (self.verticalPairWhiteOnTop, 'top left'),
                                  # (function, which corner)
                        'reversed': (self.reversedVerticalPairWhiteTop, 'top left')
                    },
                    'edge below': {
                                  # (function, edge piece left or right, comparison face, separated edge to the right or bottom)
                        'matching': (self.whiteOnTopEdgeAdjacent, 'Right', 'self.left', 'Right'),
                        'reversed': (self.whiteOnTopEdgeAdjacent, 'Right', 'self.left', 'Right')
                    },
                    'edge to the right': {
                                  # (function, edge piece left or right, comparison face, separated edge to the right or bottom)
                        'matching': (self.whiteOnTopEdgeAdjacent, 'Left', 'self.back', 'Bottom'),
                        'reversed': (self.whiteOnTopEdgeAdjacent, 'Left', 'self.back', 'Bottom')
                    }  
                },
                'top right': {
                    'edge below z': {
                        'matching': (self.verticalPairWhiteOnTop, 'top right'),
                        'reversed': (self.reversedVerticalPairWhiteTop, 'top right')
                    },
                    'edge below': {
                                  # (function, edge piece left or right, comparison face, separated edge to the right or bottom)
                        'matching': (self.whiteOnTopEdgeAdjacent, 'Left', 'self.right', 'Bottom'),
                        'reversed': (self.whiteOnTopEdgeAdjacent, 'Left', 'self.right', 'Bottom')
                    },
                    'edge to the left': {
                                  # (function, edge piece left or right, comparison face, separated edge to the right or bottom)
                        'matching': (self.whiteOnTopEdgeAdjacent, 'Right', 'self.back', 'Right'),
                        'reversed': (self.whiteOnTopEdgeAdjacent, 'Right', 'self.back', 'Right')
                    }
                },
                'bottom left': {
                    'edge below z': {
                        'matching': (self.verticalPairWhiteOnTop, 'bottom left'),
                        'reversed': (self.reversedVerticalPairWhiteTop, 'bottom left')
                    },
                    'edge above': {
                                  # (function, edge piece left or right, comparison face, separated edge to the right or bottom)
                        'matching': (self.whiteOnTopEdgeAdjacent, 'Left', 'self.left', 'Bottom'),
                        'reversed': (self.whiteOnTopEdgeAdjacent, 'Left', 'self.left', 'Bottom')
                    },
                    'edge to the right': {
                                  # (function, edge piece left or right, comparison face, separated edge to the right or bottom)
                        'matching': (self.whiteOnTopEdgeAdjacent, 'Right', 'self.front', 'Right'),
                        'reversed': (self.whiteOnTopEdgeAdjacent, 'Right', 'self.front', 'Right')
                    }
                },
                'bottom right': {
                    'edge below z': {
                        'matching': (self.verticalPairWhiteOnTop, 'bottom right'),
                        'reversed': (self.reversedVerticalPairWhiteTop, 'bottom right')
                    },
                    'edge above': {
                                  # (function, edge piece left or right, comparison face, separated edge to the right or bottom)
                        'matching': (self.whiteOnTopEdgeAdjacent, 'Right', 'self.right', 'Right'),
                        'reversed': (self.whiteOnTopEdgeAdjacent, 'Right', 'self.right', 'Right')
                    },
                    'edge to the left': {
                                  # (function, edge piece left or right, comparison face, separated edge to the right or bottom)
                        'matching': (self.whiteOnTopEdgeAdjacent, 'Left', 'self.front', 'Bottom'),
                        'reversed': (self.whiteOnTopEdgeAdjacent, 'Left', 'self.front', 'Bottom')
                    }
                }
            },
            'white on outer piece': {
                'top left': {
                    'edge to the right': {
                                  # (function, comparison Face, is white on left, is white on top)
                        'matching': (self.whiteOnOuterF2L, 'self.back', False, False),

                                  # (function, edgePieceLeftOrRight, comparisonFace, straightOrScrunched, splitOrTogether)
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.back', 'Straight', 'Together', False)
                    },
                    'edge below': {
                                  # (function, edgePieceLeftOrRight, comparisonFace, doubleOrSingleRotation)
                        'matching': (self.scrunchedMatchingTopF2L, 'Right', 'self.left', 'Connected', 'Double'),

                                  # (function, edgePieceLeftOrRight, comparisonFace, straightOrScrunched, splitOrTogether)
                        'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.left', 'Scrunched', 'Together', False)
                    },
                    'edge below z': {
                        'matching': (self.verticalWhiteNotOnTopF2L, 'top left', False, True, 'Right'),
                        'reversed': (self.verticalWhiteNotOnTopF2L, 'top left', False, False, 'Right')
                    }
                },
                'top right': {
                    'edge to the left': {
                        'matching': (self.whiteOnOuterF2L, 'self.back', True, False),
                        'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.back', 'Straight', 'Together', False)
                    },
                    'edge below': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Left', 'self.right', 'Connected', 'Double'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.right', 'Scrunched', 'Together', False)
                    },
                    'edge below z': {
                        'matching': (self.verticalWhiteNotOnTopF2L, 'top right', False, True, 'Right'),
                        'reversed': (self.verticalWhiteNotOnTopF2L, 'top right', False, False, 'Right')
                    }
                },
                'bottom left': {
                    'edge to the right': {
                        'matching': (self.whiteOnOuterF2L, 'self.front', True, False),
                        'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.front', 'Straight', 'Together', False)
                    },
                    'edge above': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Left', 'self.left', 'Connected', 'Double'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.left', 'Scrunched', 'Together', False)
                    },
                    'edge below z': {
                        'matching': (self.verticalWhiteNotOnTopF2L, 'bottom left', False, True, 'Right'),
                        'reversed': (self.verticalWhiteNotOnTopF2L, 'bottom left', False, False, 'Right')
                    }
                },
                'bottom right': {
                    'edge to the left': {
                        'matching': (self.whiteOnOuterF2L, 'self.front', False, False),
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.front', 'Straight', 'Together', False)
                    },
                    'edge above': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Right', 'self.right', 'Connected', 'Double'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.right', 'Scrunched', 'Together', False)
                    },
                    'edge below z': {
                        'matching': (self.verticalWhiteNotOnTopF2L, 'bottom right', False, True, 'Right'),
                        'reversed': (self.verticalWhiteNotOnTopF2L, 'bottom right', False, False, 'Right')
                    }
                }
            },
            'white on headlight piece': {
                'top left': {
                    'edge below': {
                                  # (function, comparison Face, is white on left, is white on top)
                        'matching': (self.whiteOnOuterF2L, 'self.left', True, False),

                                  # (self.reversedHorizontalPair, edgePieceLeftOrRight, comparisonFace, splitOrTogether)
                        'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.left', 'Straight', 'Together', False)
                    },
                    'edge to the right': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Left', 'self.back', 'Connected', 'Double'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.back', 'Scrunched', 'Together', False)
                    },
                    'edge below z': {
                        'matching': (self.verticalWhiteNotOnTopF2L, 'top left', True, False, 'Bottom'),
                        'reversed': (self.verticalWhiteNotOnTopF2L, 'top left', True, False, 'Bottom')
                    }
                    
                },
                'top right': {
                    'edge below': {
                        'matching': (self.whiteOnOuterF2L, 'self.right', False, False),
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.right','Straight', 'Together', False)
                    },
                    'edge to the left': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Right', 'self.back', 'Connected', 'Double'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.back', 'Scrunched', 'Together', False)
                    },
                    'edge below z': {
                        'matching': (self.verticalWhiteNotOnTopF2L, 'top right', True, False, 'Right'),
                                  # (function, whichCorner, whiteOnTopAfterMoving, matchedScrunchedAfterMoving, rightOrBottomEdgeIfWhiteOnTop)
                        'reversed': (self.verticalWhiteNotOnTopF2L, 'top right', True, False, 'Right')
                    }
                },
                'bottom left': {
                    'edge above': {
                        'matching': (self.whiteOnOuterF2L, 'self.left', False, False),
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.left', 'Straight', 'Together', False)
                    },
                    'edge to the right': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Right', 'self.front', 'Connected', 'Double'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.front', 'Scrunched', 'Together', False)
                    },
                    'edge below z': {
                        'matching': (self.verticalWhiteNotOnTopF2L, 'bottom left', True, False, 'Right'),
                        'reversed': (self.verticalWhiteNotOnTopF2L, 'bottom left', True, False, 'Right')
                    }
                },
                'bottom right': {
                    'edge above': {
                        'matching': (self.whiteOnOuterF2L, 'self.right', True, False),
                        'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.right', 'Straight', 'Together', False)
                    },
                    'edge to the left': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Left', 'self.front', 'Connected', 'Double'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.front', 'Scrunched', 'Together', False)
                    },
                    'edge below z': {
                        'matching': (self.verticalWhiteNotOnTopF2L, 'bottom right', True, False, 'Bottom'),
                        'reversed': (self.verticalWhiteNotOnTopF2L, 'bottom right', True, False, 'Bottom')
                    }
                }
            }

        }

        self.cornerRelationMovesWhenPiecesAreSeparated = {
            # corner number
            '1': {
                'self.top': {
                    # edge number
                       # (function, comparisonFace, edgeToTheRightOrBottom)
                    '3': {
                        'matching': (self.whiteOnTopEdgeSeparated, 'self.right', 'Right')
                    },
                    '4': {
                        'matching': (self.whiteOnTopEdgeSeparated, 'self.front', 'Bottom')
                    },
                    '5': self.cornerRelationMoves['white on top piece']['bottom left']['edge below z'],
                    '6': self.cornerRelationMoves['white on top piece']['bottom right']['edge below z'],
                    '7': self.cornerRelationMoves['white on top piece']['top right']['edge below z']
                },
                'self.back': {
                    '3': {
                                # (function, edgePieceLeftOrRight, comparisonFace, separateOrConnected, doubleOrSingleRotation)
                        'matching': (self.scrunchedMatchingTopF2L, 'Left', 'self.right', 'Separate', 'Double'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.right', 'Straight', 'Split', False)
                    },
                    '4': {
                                # (function, edgePieceLeftOrRight, comparisonFace, separateOrConnected, doubleOrSingleRotation)
                        'matching': (self.scrunchedMatchingTopF2L, 'Left', 'self.front', 'Separate', 'Single'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.front', 'Straight', 'Split', True)
                    },
                    '5': self.cornerRelationMoves['white on outer piece']['bottom left']['edge below z'],
                    '6': self.cornerRelationMoves['white on headlight piece']['bottom right']['edge below z'],
                    '7': self.cornerRelationMoves['white on outer piece']['top right']['edge below z'],
                },
                'self.left': {
                    '4': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Right', 'self.front', 'Separate', 'Double'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.front', 'Straight', 'Split', False)
                    },
                    '3': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Right', 'self.right', 'Separate', 'Single'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.right', 'Straight', 'Split', True)
                    },
                    '5': self.cornerRelationMoves['white on headlight piece']['bottom left']['edge below z'],
                    '6': self.cornerRelationMoves['white on outer piece']['bottom right']['edge below z'],
                    '7': self.cornerRelationMoves['white on headlight piece']['top right']['edge below z']
                }
            },
            '2': {
                'self.top': {
                    '4': {
                        'matching': (self.whiteOnTopEdgeSeparated, 'self.front', 'Right')
                    },
                    '2': {
                        'matching': (self.whiteOnTopEdgeSeparated, 'self.left', 'Bottom')
                    },
                    '5': self.cornerRelationMoves['white on top piece']['bottom left']['edge below z'],
                    '6': self.cornerRelationMoves['white on top piece']['bottom right']['edge below z'],
                    '8': self.cornerRelationMoves['white on top piece']['top left']['edge below z']
                },
                'self.right': {
                    '4': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Left', 'self.front', 'Separate', 'Double'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.front', 'Straight', 'Split', False)
                    },
                    '2': {
                                    # (function, edgePieceLeftOrRight, comparisonFace, separateOrConnected, doubleOrSingleRotation)
                          'matching': (self.scrunchedMatchingTopF2L, 'Left', 'self.left', 'Separate', 'Single'),
                          'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.left', 'Straight', 'Split', True)
                    },
                    '5': self.cornerRelationMoves['white on outer piece']['bottom left']['edge below z'],
                    '6': self.cornerRelationMoves['white on headlight piece']['bottom right']['edge below z'],
                    '8': self.cornerRelationMoves['white on headlight piece']['top left']['edge below z'] 
                },
                'self.back': {
                    '2': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Right', 'self.left', 'Separate', 'Double'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.left', 'Straight', 'Split', False)
                    },
                    '4': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Right', 'self.front', 'Separate', 'Single'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.front', 'Straight', 'Split', True)
                    },
                    '5': self.cornerRelationMoves['white on headlight piece']['bottom left']['edge below z'],
                    '6': self.cornerRelationMoves['white on outer piece']['bottom right']['edge below z'],
                    '8': self.cornerRelationMoves['white on outer piece']['top left']['edge below z']
                  },
                },
            '3': {
                'self.top': {
                    '1': {
                        'matching': (self.whiteOnTopEdgeSeparated, 'self.back', 'Right')
                    },
                    '3': {
                        'matching': (self.whiteOnTopEdgeSeparated, 'self.right', 'Bottom')
                    },
                    '6': self.cornerRelationMoves['white on top piece']['bottom right']['edge below z'],
                    '7': self.cornerRelationMoves['white on top piece']['top right']['edge below z'],
                    '8': self.cornerRelationMoves['white on top piece']['top left']['edge below z']
                },
                'self.left': {
                    '1': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Left', 'self.back', 'Separate', 'Double'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.back', 'Straight', 'Split', False)
                    },
                    '3': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Left', 'self.right', 'Separate', 'Single'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.right', 'Straight', 'Split', True)
                    },
                    '6': self.cornerRelationMoves['white on headlight piece']['bottom right']['edge below z'],
                    '7': self.cornerRelationMoves['white on outer piece']['top right']['edge below z'],
                    '8': self.cornerRelationMoves['white on headlight piece']['top left']['edge below z']
                  },
                'self.front': {
                    '3': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Right', 'self.right', 'Separate', 'Double'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.right', 'Straight', 'Split', False)
                    },
                    '1': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Right', 'self.back', 'Separate', 'Single'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.back', 'Straight', 'Split', True)
                    },
                    '6': self.cornerRelationMoves['white on outer piece']['bottom right']['edge below z'],
                    '7': self.cornerRelationMoves['white on headlight piece']['top right']['edge below z'],
                    '8': self.cornerRelationMoves['white on outer piece']['top left']['edge below z']
                }
            },
            '4': {
                'self.top': {
                    '2': {
                        'matching': (self.whiteOnTopEdgeSeparated, 'self.left', 'Right')
                    },
                    '1': {
                        'matching': (self.whiteOnTopEdgeSeparated, 'self.back', 'Bottom')
                    },
                    '5': self.cornerRelationMoves['white on top piece']['bottom left']['edge below z'],
                    '7': self.cornerRelationMoves['white on top piece']['top right']['edge below z'],
                    '8': self.cornerRelationMoves['white on top piece']['top left']['edge below z']
                },
                'self.front': {
                    '2': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Left', 'self.left', 'Separate', 'Double'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.left', 'Straight', 'Split', False)
                    },
                    '1': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Left', 'self.back', 'Separate', 'Single'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Right', 'self.back', 'Straight', 'Split', True)
                    },
                    '5': self.cornerRelationMoves['white on outer piece']['bottom left']['edge below z'],
                    '7': self.cornerRelationMoves['white on outer piece']['top right']['edge below z'],
                    '8': self.cornerRelationMoves['white on headlight piece']['top left']['edge below z']
                },
                'self.right': {
                    '1': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Right', 'self.back', 'Separate', 'Double'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.back', 'Straight', 'Split', False)
                    },
                    '2': {
                        'matching': (self.scrunchedMatchingTopF2L, 'Right', 'self.left', 'Separate', 'Single'),
                        'reversed': (self.reversedHorizontalPairF2L, 'Left', 'self.left', 'Straight', 'Split', True)
                    },
                    '5': self.cornerRelationMoves['white on headlight piece']['bottom left']['edge below z'],
                    '7': self.cornerRelationMoves['white on headlight piece']['top right']['edge below z'],
                    '8': self.cornerRelationMoves['white on outer piece']['top left']['edge below z']          
                }
            }
        }

        self.gettingOtherEdgePositionFromFirstColorPosition = {
            'self.front': {
                '1': ['7', 'self.top'],
                '3': ['5', 'self.left'],
                '5': ['3', 'self.right'],
                '7': ['1', 'self.bottom']
            },
            'self.left': {
                '1': ['3', 'self.top'],
                '3': ['5', 'self.back'],
                '5': ['3', 'self.front'],
                '7': ['3', 'self.bottom']
            },
            'self.right': {
                '1': ['5', 'self.top'],
                '3': ['5', 'self.front'],
                '5': ['3', 'self.back'],
                '7': ['5', 'self.bottom']
            },
            'self.back': {
                '1': ['1', 'self.top'],
                '3': ['5', 'self.right'],
                '5': ['3', 'self.left'],
                '7': ['7', 'self.bottom']
            },
            'self.top': {
                '1': ['1', 'self.back'],
                '3': ['1', 'self.left'],
                '5': ['1', 'self.right'],
                '7': ['1', 'self.front']
            },
            'self.bottom': {
                '1': ['7', 'self.front'],
                '3': ['7', 'self.left'],
                '5': ['7', 'self.right'],
                '7': ['7', 'self.back']
            }
        }

        self.separatedCornerCheckF2L = {
            '1': self.topLeftSeparatedCornerCheck,
            '2': self.topRightSeparatedCornerCheck,
            '3': self.bottomLeftSeparatedCornerCheck,
            '4': self.bottomRightSeparatedCornerCheck
        }

        self.movingCornerToYellowFaceUpdate = {
            '5': {'self.left': 'self.front',
                  'self.front': 'self.top',
                  'self.bottom': 'self.right'},

            '6': {'self.right': 'self.front',
                  'self.front': 'self.top',
                  'self.bottom': 'self.left'},

            '7': {'self.left': 'self.back',
                  'self.back': 'self.top',
                  'self.bottom': 'self.right'},

            '8': {'self.right': 'self.back',
                  'self.back': 'self.top',
                  'self.bottom': 'self.left'}
        }

        self.topLayerCornerAndEdgePieceRelation = {
            '1': {'self.top': self.topLeftZCornerCheck,
                  'self.back': self.topLeftVerticalCornerCheck,
                  'self.left': self.topLeftHorizontalCornerCheck,
                  },
            '2': {'self.top': self.topRightZCornerCheck,
                  'self.back': self.topRightVerticalCornerCheck,
                  'self.right': self.topRightHorizontalCornerCheck,
                  },
            '3': {'self.top': self.bottomLeftZCornerCheck,
                  'self.front': self.bottomLeftVerticalCornerCheck,
                  'self.left': self.bottomLeftHorizontalCornerCheck,
                  },
            '4': {'self.top': self.bottomRightZCornerCheck,
                  'self.front': self.bottomRightVerticalCornerCheck,
                  'self.right': self.bottomRightHorizontalCornerCheck,
                  }
        }

        self.colorsRelationToAnother = {'orange': {'left': 'green', 'right': 'blue', 'top': 'yellow', 'bottom': 'white'},
                                    'green': {'left': 'red', 'right': 'orange', 'top': 'yellow', 'bottom': 'white'},
                                    'blue': {'left': 'orange', 'right': 'red', 'top': 'yellow', 'bottom': 'white'},
                                    'red': {'left': 'blue', 'right': 'green', 'top': 'yellow', 'bottom': 'white'},
                                    'white': {'left': 'green', 'right': 'blue', 'top': 'orange', 'bottom': 'red'},
                                    'yellow': {'left': 'green', 'right': 'blue', 'top': 'red', 'bottom': 'orange'}
                                    }

        self.sidesToColors = {'self.front': 'orange', 'self.left': 'green',
                        'self.right': 'blue', 'self.back': 'red',
                        'self.top': 'yellow', 'self.bottom': 'white'}
        
        self.colorsToSides = {'orange': 'self.front', 'blue': 'self.right',
                              'red': 'self.back', 'green': 'self.left'    
                              }

        self.colorsToRealSides = {'orange': self.front, 'green': self.left,
                        'blue': self.right, 'red': self.back,
                        'yellow': self.top, 'white': self.bottom}

        self.colorsToFrames = {'green': self.frames[0], 'orange': self.frames[1],
                        'blue': self.frames[2], 'red': self.frames[3],
                        'yellow': self.frames[4], 'white': self.frames[5]}
        
        self.gettingPrimaryEdgeToYellow = {
                                    'orange': {'1': [self.F, '5', 'orange', 'blue'],
                                                '3': [self.LPrime, '3', 'yellow', 'green'],
                                                '5': [self.R, '5', 'yellow', 'blue'],
                                                '7': [self.FPrime, '5', 'orange', 'blue']},

                                    'green': {'1': [self.L, '5', 'green', 'orange'],
                                                '3': [self.BPrime, '1', 'yellow', 'red'],
                                                '5': [self.F, '7', 'yellow', 'orange'],
                                                '7': [self.LPrime, '5', 'green', 'orange']},

                                    'blue': {'1': [self.RPrime, '3', 'blue', 'orange'],
                                                '3': [self.FPrime, '7', 'yellow', 'orange'],
                                                '5': [self.B, '1', 'yellow', 'red'],
                                                '7': [self.R, '3', 'blue', 'orange']},

                                    'red': {'1': [self.B, '5', 'red', 'green'],
                                                '3': [self.RPrime, '5', 'yellow', 'blue'],
                                                '5': [self.L, '3', 'yellow', 'green'],
                                                '7': [self.BPrime, '5', 'red', 'green']},
                                    
                                    'white': {'1': [self.FPrime, '3', 'blue', 'orange'],
                                                '3': [self.LPrime, '3', 'orange', 'green'],
                                                '5': [self.R, '5', 'orange', 'blue'],
                                                '7': [self.B, '5', 'blue', 'red']}                     
                                     }

        self.movesAndReverseDict = { self.R: self.RPrime, 
                            self.L: self.LPrime, 
                            self.U: self.UPrime, 
                            self.F: self.FPrime, 
                            self.B: self.BPrime, 
                            self.D: self.DPrime,
                            self.RPrime: self.R,
                            self.LPrime: self.L,
                            self.UPrime: self.U,
                            self.FPrime: self.F,
                            self.BPrime: self.B,
                            self.DPrime: self.D}
        
        self.movesAndLabelsDict = {  self.R: 'R', 
                                self.L: 'L', 
                                self.U: 'U', 
                                self.F: 'F', 
                                self.B: 'B', 
                                self.D: 'D',
                                self.RPrime: 'R\'',
                                self.LPrime: 'L\'',
                                self.UPrime: 'U\'',
                                self.FPrime: 'F\'',
                                self.BPrime: 'B\'',
                                self.DPrime: 'D\''}

        self.popUpWindowFromOtherFile = popUpWindow
        self.movesExecutedStack = []

        # status box
        self.statusBox = tk.Text(self.popUpWindowFromOtherFile, width=65, height=4, bg=self.popUpWindowFromOtherFile.cget('background'))
        self.statusBox.grid(row=0, column=21)

        # create four checkbox buttons
        self.checkbox_vars = [tk.IntVar() for _ in range(4)]
        self.checkbox_texts = ["Cross", "   F2L", "  OLL", "   PLL"]
        self.checkboxes = []

        # set the checkbox position
        for i in range(4):
            checkbox = tk.Checkbutton(self.popUpWindowFromOtherFile, text=self.checkbox_texts[i], variable=self.checkbox_vars[i])
            checkbox.grid(row=6+i, column=20, padx=15)
            self.checkboxes.append(checkbox) 
        
        # To make checkboxes unclickable
        for checkbox in self.checkboxes:
            checkbox.config(state=tk.DISABLED)

    

    def resetCube(self):
        self.solvingCube = False
        self.statusBox.delete('1.0', 'end')
        newFront = self.initialFront
        newTop = self.initialTop
        newBack = self.initialBack
        newBottom = self.initialBottom
        newRight = self.initialRight
        newLeft = self.initialLeft
        newSides = [newLeft, newFront, newRight, newBack, newTop, newBottom]
     
        self.assignNewColors(newFront, newTop, newBack, newBottom, newRight, newLeft, newSides)

        self.crossSolved = False
        self.F2LSolved = False
        self.OLLSolved = False
        self.PLLSolved = False

        for i in range(4):
            # uncheck the boxes
            self.checkbox_vars[i].set(0)

    def randomMove(self):
        randomMove = random.choice(list(self.movesAndReverseDict.keys()))
        randomMove()

    def randomScramble(self):
        self.solvingCube = False
       
        originalTimeBetweenMoves = self.moves.timeBetweenMoves
        self.moves.timeBetweenMoves = 0

        self.resetCube()
        self.movesExecutedStack = [] # allows to press button multiple times
        self.statusBox.delete('1.0', 'end')


        # randomly scramble
        while len(self.movesExecutedStack) < self.numberOfRandomMoves:
            randomMove = random.choice(list(self.movesAndReverseDict.keys()))
            randomMove()

            self.movesExecutedStack.append(randomMove)
            if len(self.movesExecutedStack) == 1:
                self.statusBox.insert('1.0', f'Random Scramble:\n')
                self.statusBox.insert('2.0', f'{self.movesAndLabelsDict.get(randomMove)}')
            else:
                self.statusBox.insert('end', f' {self.movesAndLabelsDict.get(randomMove)}')
            self.popUpWindowFromOtherFile.update()
        
        self.moves.timeBetweenMoves = originalTimeBetweenMoves

    def setDefault(self):
        self.initialFront = self.front
        self.initialTop = self.top
        self.initialBack = self.back
        self.initialBottom = self.bottom
        self.initialRight = self.right
        self.initialLeft = self.left
    
    def testingAStep(self, step):
        originalTimeBetweenMoves = self.moves.timeBetweenMoves
        self.moves.timeBetweenMoves = 0.0

        for _ in range(self.numOfTests):
            self.randomScramble()

            if step == 'Cross':
                self.solveCross()
                if (self.bottom[1:8:2] != ['white']*4 or
                    self.left[7] != 'green' or
                    self.front[7] != 'orange' or 
                    self.right[7] != 'blue' or
                    self.back[7] != 'red'):

                    return
                
            elif step == 'F2L':
                self.solveCross()
                self.solveF2L()

                if ([self.bottom[0], self.bottom[2], self.bottom[6], self.bottom[8]]  != ['white']*4 or
                    [self.left[3], self.left[5], self.left[6], self.left[8]] != ['green']*4 or
                    [self.front[3], self.front[5], self.front[6], self.front[8]] != ['orange']*4 or 
                    [self.right[3], self.right[5], self.right[6], self.right[8]] != ['blue']*4 or
                    [self.back[3], self.back[5], self.back[6], self.back[8]] != ['red']*4):               
            
                    return

            if step == 'OLL':
                self.solveCross()
                self.solveF2L()
                self.solveOLL()

                if self.top != ['yellow']*9:                    
                    return
            
            if step == 'solveCube':
                self.solveCube()

                if (self.top != ['yellow']*9 or 
                    self.left != ['green']*9 or 
                    self.front != ['orange']*9 or 
                    self.right != ['blue']*9 or 
                    self.back != ['red']*9 or 
                    self.bottom != ['white']*9):
                        
                        return

        self.resetCube()

        self.moves.timeBetweenMoves = originalTimeBetweenMoves

    def updatingColorsToRealSides(self):
        self.colorsToRealSides = {'orange': self.front, 'green': self.left,
                        'blue': self.right, 'red': self.back,
                        'yellow': self.top, 'white': self.bottom}




    def findWhitePieces(self, edgeOrCorner):
        sideNames = ['self.top', 'self.left', 'self.front', 'self.right', 'self.back', 'self.bottom']
        whitePieces = []

        if edgeOrCorner == 'edge':      # trying to find an edge white piece
            edgePieces = [self.top[1], self.top[3], self.top[5], self.top[7], 
                        self.left[1], self.left[3], self.left[5], self.left[7],
                        self.front[1], self.front[3], self.front[5], self.front[7], 
                        self.right[1], self.right[3], self.right[5], self.right[7], 
                        self.back[1], self.back[3], self.back[5], self.back[7], 
                        self.bottom[1], self.bottom[3], self.bottom[5], self.bottom[7]]
            
            for i, piece in enumerate(edgePieces):
                if piece == 'white':
                    whitePieces.append([sideNames[i//4], str(i%4*2+1)])

            return whitePieces
        
        else:       # trying to find a corner white piece
            possiblePieceIndexes = ['0', '2', '6', '8']
            cornerPieces = [self.top[0], self.back[2], self.left[0],     # top layer
                            self.top[2], self.back[0], self.right[2],
                            self.top[6], self.left[2], self.front[0],
                            self.top[8], self.front[2], self.right[0],

                            self.front[6], self.bottom[0], self.left[8], # bottom layer
                            self.front[8], self.bottom[2], self.right[6],
                            self.bottom[6], self.left[6], self.back[8],
                            self.bottom[8], self.right[8], self.back[6],]
            
            for i, piece in enumerate(cornerPieces):
                if i < 3:
                    cornerSpot = '1'
                elif i >= 3 and i < 6:
                    cornerSpot = '2'
                elif i >= 6 and i < 9:
                    cornerSpot = '3'
                elif i >= 9 and i < 12:
                    cornerSpot = '4'

                elif i >= 12 and i < 15:
                    cornerSpot = '5'
                elif i >= 15 and i < 18:
                    cornerSpot = '6'
                elif i >= 18 and i < 21:
                    cornerSpot = '7'
                else:       # i >= 21 and i < 24
                    cornerSpot = '8'

                if piece == 'white':
                    if i % 3 == 0 and i < 10:
                        sideName = sideNames[0]
                        pieceIndex = possiblePieceIndexes[i//3]

                    elif i == 2 or i == 7 or i == 14 or i == 19:
                        sideName = sideNames[1]
                        if i == 2 or i == 7:
                            pieceIndex = possiblePieceIndexes[i//4]
                        elif i == 14:
                            pieceIndex = possiblePieceIndexes[3]
                        else:
                            pieceIndex = possiblePieceIndexes[2]

                    elif i == 8 or i == 10 or i == 12 or i == 15:
                        sideName = sideNames[2]
                        if i == 8 or i == 10:
                            pieceIndex = possiblePieceIndexes[(i-8)//2]
                        else:
                            pieceIndex = possiblePieceIndexes[(i-10)//2+1]

                    elif i == 5 or i == 11 or i == 17 or i == 22:
                        sideName = sideNames[3]
                        if i == 17 or i == 22:
                            pieceIndex = possiblePieceIndexes[(i-15)//5+2]
                        elif i == 5:
                            pieceIndex = possiblePieceIndexes[1]
                        else:
                            pieceIndex = possiblePieceIndexes[0]

                    elif i == 1 or i == 4 or i == 20 or i == 23:
                        sideName = sideNames[4]
                        if i == 1:
                            pieceIndex = possiblePieceIndexes[1]
                        elif i == 4:
                            pieceIndex = possiblePieceIndexes[0]
                        elif i == 20:
                            pieceIndex = possiblePieceIndexes[3]
                        else:
                            pieceIndex = possiblePieceIndexes[2]

                    elif i == 13 or i == 16 or i == 18 or i == 21:
                        sideName = sideNames[5]
                        if i == 13 or i == 16:
                            pieceIndex = possiblePieceIndexes[i//14]
                        else:
                            pieceIndex = possiblePieceIndexes[i//19+2]

                    whitePieces.append([sideName, pieceIndex, cornerSpot])

            return whitePieces

    def findColorsWithWhite(self, edgeOrCorner):
        # updating the dictionary with the new sides
        self.updatingColorsToRealSides()
        
        if edgeOrCorner == 'edge':
            whereWhitesAre = self.findWhitePieces('edge')
            colorsThatWhiteIsOn = [[instanceOfWhite[0], self.sidesToColors[instanceOfWhite[0]], str(instanceOfWhite[1])] for instanceOfWhite in whereWhitesAre]
        else:
            whereWhitesAre = self.findWhitePieces('corner')
            colorsThatWhiteIsOn = [[instanceOfWhite[0], self.sidesToColors[instanceOfWhite[0]], str(instanceOfWhite[1]), instanceOfWhite[2]] for instanceOfWhite in whereWhitesAre]
        whitePieceData = []

                
        for whichWhitePieceIndex, whitePieceInstance in enumerate(colorsThatWhiteIsOn):  
            face = whitePieceInstance[0]
            faceColor = whitePieceInstance[1]
            pieceNumber = whitePieceInstance[2]

            if edgeOrCorner == 'edge':

                if pieceNumber == '1':      # go to the top to find edge piece
                    otherEdgePieceFace = self.colorsRelationToAnother[faceColor]['top']

                    if faceColor == 'orange':
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][7] # yellow
                        newPiecePosition = '7'
                    elif faceColor == 'green':
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][3] # yellow
                        newPiecePosition = '3'
                    elif faceColor == 'blue':
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][5] # yellow
                        newPiecePosition = '5'
                    elif faceColor == 'red':
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][1] # yellow
                        newPiecePosition = '1'
                    elif faceColor == 'yellow':
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][1] # red
                        newPiecePosition = '1'
                    else:   # color == 'white'
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][7] # orange
                        newPiecePosition = '7'


                elif pieceNumber == '3':      # go to the left to find edge piece
                    otherEdgePieceFace = self.colorsRelationToAnother[faceColor]['left']

                    if faceColor != 'yellow' and faceColor != 'white':
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][5]
                        newPiecePosition = '5'
                    elif faceColor == 'yellow':
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][1] # green
                        newPiecePosition = '1'
                    else:   # color == 'white'
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][7] # green
                        newPiecePosition = '7'


                elif pieceNumber == '5':      # go to the right to find edge piece
                    otherEdgePieceFace = self.colorsRelationToAnother[faceColor]['right']

                    if faceColor != 'yellow' and faceColor != 'white':
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][3]
                        newPiecePosition = '3'
                    elif faceColor == 'yellow':
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][1] # green
                        newPiecePosition = '1'
                    else:   # color == 'white'
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][7] # green
                        newPiecePosition = '7'

                elif pieceNumber == '7':      # go to the bottom to find edge piece
                    otherEdgePieceFace = self.colorsRelationToAnother[faceColor]['bottom']

                    if faceColor == 'orange':
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][1] # white
                        newPiecePosition = '1'
                    elif faceColor == 'green':
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][3] # white
                        newPiecePosition = '3'
                    elif faceColor == 'blue':
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][5] # white
                        newPiecePosition = '5'
                    elif faceColor == 'red':
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][7] # white
                        newPiecePosition = '7'
                    elif faceColor == 'yellow':
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][1] # orange
                        newPiecePosition = '1'
                    else:   # color == 'white'
                        otherEdgePiece = self.colorsToRealSides[otherEdgePieceFace][7] # red
                        newPiecePosition = '7'
                
                if otherEdgePiece == otherEdgePieceFace and self.sidesToColors[face] == 'white':
                    whitePieceData = whitePieceData
                
                else:
                    whitePieceData = ['white', otherEdgePiece, face, otherEdgePieceFace, newPiecePosition, whichWhitePieceIndex, pieceNumber]
                    return whitePieceData
                
            else:       # finding the other two colors of the edge piece
                cornerSpot = whitePieceInstance[3]

                if pieceNumber == '0':      # go to the top and left to find corner colors
                    firstOtherCornerFace = self.colorsRelationToAnother[faceColor]['top']
                    secondOtherCornerFace = self.colorsRelationToAnother[faceColor]['left']

                    if faceColor == 'orange':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][6] # yellow
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][2] # green
                        firstCornerPiecePosition = '6'
                        secondCornerPiecePosition = '2'
                    elif faceColor == 'green':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][0] # yellow
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][2] # red
                        firstCornerPiecePosition = '0'
                        secondCornerPiecePosition = '2'
                    elif faceColor == 'blue':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][8] # yellow
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][2] # orange
                        firstCornerPiecePosition = '8'
                        secondCornerPiecePosition = '2'
                    elif faceColor == 'red':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][2] # yellow
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][2] # blue
                        firstCornerPiecePosition = '2'
                        secondCornerPiecePosition = '2'
                    elif faceColor == 'yellow':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][2] # red
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][0] # green
                        firstCornerPiecePosition = '2'
                        secondCornerPiecePosition = '0'
                    else:   # color == 'white'
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][6] # orange
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][8] # green
                        firstCornerPiecePosition = '6'
                        secondCornerPiecePosition = '8'


                elif pieceNumber == '2':      # go to the top and right to find corner colors
                    firstOtherCornerFace = self.colorsRelationToAnother[faceColor]['top']
                    secondOtherCornerFace = self.colorsRelationToAnother[faceColor]['right']

                    if faceColor == 'orange':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][8] # yellow
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][0] # blue
                        firstCornerPiecePosition = '8'
                        secondCornerPiecePosition = '0'
                    elif faceColor == 'green':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][6] # yellow
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][0] # orange
                        firstCornerPiecePosition = '6'
                        secondCornerPiecePosition = '0'
                    elif faceColor == 'blue':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][2] # yellow
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][0] # red
                        firstCornerPiecePosition = '2'
                        secondCornerPiecePosition = '0'
                    elif faceColor == 'red':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][0] # yellow
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][0] # green
                        firstCornerPiecePosition = '0'
                        secondCornerPiecePosition = '2'
                    elif faceColor == 'yellow':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][0] # red
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][2] # blue
                        firstCornerPiecePosition = '0'
                        secondCornerPiecePosition = '2'
                    else:   # color == 'white'
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][8] # orange
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][6] # blue
                        firstCornerPiecePosition = '8'
                        secondCornerPiecePosition = '6'


                elif pieceNumber == '6':      # go to the bottom and left to find corner colors
                    firstOtherCornerFace = self.colorsRelationToAnother[faceColor]['bottom']
                    secondOtherCornerFace = self.colorsRelationToAnother[faceColor]['left']

                    if faceColor == 'orange':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][0] # white
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][8] # green
                        firstCornerPiecePosition = '0'
                        secondCornerPiecePosition = '8'
                    elif faceColor == 'green':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][6] # white
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][8] # red
                        firstCornerPiecePosition = '6'
                        secondCornerPiecePosition = '8'
                    elif faceColor == 'blue':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][2] # white
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][8] # orange
                        firstCornerPiecePosition = '2'
                        secondCornerPiecePosition = '8'
                    elif faceColor == 'red':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][8] # white
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][8] # blue
                        firstCornerPiecePosition = '0'
                        secondCornerPiecePosition = '2'
                    elif faceColor == 'yellow':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][0] # orange
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][2] # green
                        firstCornerPiecePosition = '0'
                        secondCornerPiecePosition = '2'
                    else:   # color == 'white'
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][8] # red
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][6] # green
                        firstCornerPiecePosition = '8'
                        secondCornerPiecePosition = '6'

                elif pieceNumber == '8':      # go to the bottom and right to find corner colors
                    firstOtherCornerFace = self.colorsRelationToAnother[faceColor]['bottom']
                    secondOtherCornerFace = self.colorsRelationToAnother[faceColor]['right']

                    if faceColor == 'orange':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][2] # white
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][6] # blue
                        firstCornerPiecePosition = '2'
                        secondCornerPiecePosition = '6'
                    elif faceColor == 'green':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][0] # white
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][6] # orange
                        firstCornerPiecePosition = '0'
                        secondCornerPiecePosition = '6'
                    elif faceColor == 'blue':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][8] # white
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][6] # red
                        firstCornerPiecePosition = '8'
                        secondCornerPiecePosition = '6'
                    elif faceColor == 'red':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][6] # white
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][6] # green
                        firstCornerPiecePosition = '6'
                        secondCornerPiecePosition = '6'
                    elif faceColor == 'yellow':
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][2] # orange
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][0] # blue
                        firstCornerPiecePosition = '2'
                        secondCornerPiecePosition = '0'
                    else:   # color == 'white'
                        firstOtherCornerColor = self.colorsToRealSides[firstOtherCornerFace][6] # red
                        secondOtherCornerColor = self.colorsToRealSides[secondOtherCornerFace][8] # blue
                        firstCornerPiecePosition = '6'
                        secondCornerPiecePosition = '8'

                if (firstOtherCornerFace == firstOtherCornerColor and self.colorsToRealSides[firstOtherCornerFace][self.edgeColorsBasedOffOfCornerSpot[cornerSpot][self.colorsToSides[firstOtherCornerFace]]] == firstOtherCornerColor and
                    secondOtherCornerFace == secondOtherCornerColor and self.colorsToRealSides[secondOtherCornerFace][self.edgeColorsBasedOffOfCornerSpot[cornerSpot][self.colorsToSides[secondOtherCornerFace]]] == secondOtherCornerColor and 
                    self.sidesToColors[face] == 'white'):
                    whitePieceData = whitePieceData
                else:
                    whitePieceData = ['white', firstOtherCornerColor, firstOtherCornerFace, firstCornerPiecePosition, secondOtherCornerColor, secondOtherCornerFace, secondCornerPiecePosition, face, whichWhitePieceIndex, pieceNumber, cornerSpot]              
                    return whitePieceData
            
        return whitePieceData
    
    def movingPiecesYellowToWhite(self):
        self.yellowToWhite = 1
        
        while self.currentOtherEdgeFace != self.otherEdge:
            self.UPrime()
            self.updatingHorizontalColorIndex()
        
        # get and execute move
        cubeMove = self.yellowToWhiteMoves[self.currentPrimaryEdgePiecePosition]

        cubeMove()
        cubeMove()
    
    def updatingHorizontalColorIndex(self):
        if self.solvingCube and self.yellowToWhite:
            currentFaceIndex = self.horizontalColors.index(self.currentOtherEdgeFace)
            currentWhitePieceLocationIndex = self.edgeLocations.index(self.currentPrimaryEdgePiecePosition)

            if currentFaceIndex <= 2:
                self.currentOtherEdgeFace = self.horizontalColors[currentFaceIndex+1]
            else:
                self.currentOtherEdgeFace = self.horizontalColors[0]

            if currentWhitePieceLocationIndex <= 2:
                self.currentPrimaryEdgePiecePosition = self.edgeLocations[currentWhitePieceLocationIndex+1]
            else:
                self.currentPrimaryEdgePiecePosition = self.edgeLocations[0]

    def movingToYellow(self):
        self.yellowToWhite = 0
        movesExecuted = []

        while self.currentPrimaryEdgeFace != 'yellow':

            # get white edge piece to the top (yellow side)
            cubeMove = self.gettingPrimaryEdgeToYellow[self.currentPrimaryEdgeFace][self.currentPrimaryEdgePiecePosition][0]
            movesExecuted.insert(0, cubeMove)
            cubeMove()

            edgePieceData = self.gettingPrimaryEdgeToYellow[self.currentPrimaryEdgeFace][self.currentPrimaryEdgePiecePosition]
            self.currentPrimaryEdgePiecePosition = edgePieceData[1]
            self.currentPrimaryEdgeFace = edgePieceData[2]
            self.currentOtherEdgeFace = edgePieceData[3]
            
            # move the white edge piece out of the way because we need to undo the moves to get the yellow piece to the top
            if self.currentPrimaryEdgeFace == 'yellow':
                self.UPrime()
                self.UPrime()

                oldWhiteIndex = self.edgeLocations.index(self.currentPrimaryEdgePiecePosition)
                self.currentPrimaryEdgePiecePosition = self.edgeLocations[(oldWhiteIndex + 2) % 4]

                oldOtherEdge = self.horizontalColors.index(self.currentOtherEdgeFace)
                self.currentOtherEdgeFace = self.horizontalColors[(oldOtherEdge + 2) % 4]

                # undo the moves that got white edge to the top
                for _ in range(len(movesExecuted)):
                    oppositeMove = self.movesAndReverseDict[movesExecuted[0]]
                    oppositeMove()

                    del movesExecuted[0]

    def findingASingularWhiteEdgePiece(self, cornerOrEdge):
        if cornerOrEdge == 'edge':
            whiteEdge = self.findColorsWithWhite('edge')

            if whiteEdge:
                otherEdgeColorFace = whiteEdge[3]
                self.currentOtherEdgeFace = self.colorsToRealSides[otherEdgeColorFace][4]
                self.otherEdge = whiteEdge[1]
        
        else:
            whiteEdge = self.findColorsWithWhite('corner')
   
        return whiteEdge

    def solveCross(self):
        self.solvingCube = True
        self.statusBox.delete('1.0', 'end')
        self.statusBox.insert('1.0', 'Cross Solution:\n')

        # get a displaced white edge piece
        whiteEdge = self.findingASingularWhiteEdgePiece('edge')

        if not whiteEdge:
            return

        # while there are displaced white edge pieces
        if whiteEdge:
            for _ in range(4):
                
                initialWhiteEdgeFace = self.sidesToColors[whiteEdge[2]]
                initialWhiteEdgePosition = whiteEdge[6]
                self.currentPrimaryEdgeFace = initialWhiteEdgeFace
                self.currentPrimaryEdgePiecePosition = initialWhiteEdgePosition

                # move the white piece to the top
                self.movingToYellow()

                # move the edge piece to the matching other edge color and then move to final correct destination
                self.movingPiecesYellowToWhite()
                

                # find next white edge piece
                whiteEdge = self.findingASingularWhiteEdgePiece('edge')

                if whiteEdge:
                    initialWhiteEdgeFace = self.sidesToColors[whiteEdge[2]]
                    initialWhiteEdgePosition = whiteEdge[6]
                else:
                    # cross is solved!
                    # check the Cross checkbox
                    self.crossSolved = True
                    self.checkbox_vars[0].set(1)
                    return

        # cross is not solved :(
        return
    
    def testingCross(self):
        self.testingAStep('Cross')




    def topLeftZCornerCheck(self):

        # white piece on top, corresponding edge z below
        if self.back[2] == self.back[5] and self.left[0] == self.left[3]:
            return 'white on top piece, top left, edge below z, matching'
        elif self.back[2] == self.left[3] and self.back[5] == self.left[0]:
            return 'white on top piece, top left, edge below z, reversed'
        
        # white piece on top, corresponding edge to the right
        elif self.back[2] == self.back[1] and self.left[0] == self.top[1]:
            return 'white on top piece, top left, edge to the right, matching'
        elif self.back[2] == self.top[1] and self.left[0] == self.back[1]:
            return 'white on top piece, top left, edge to the right, reversed'
        
        # white piece on top, corresponding edge below
        elif self.left[0] == self.left[1] and self.back[2] == self.top[3]:
            return 'white on top piece, top left, edge below, matching'
        elif self.left[0] == self.top[3] and self.back[2] == self.left[1]:
            return 'white on top piece, top left, edge below, reversed'
        
        return False
    
    def bottomLeftZCornerCheck(self):
        
        # white piece on top, corresponding edge z below
        if self.left[2] == self.left[5] and self.front[0] == self.front[3]:
            return 'white on top piece, bottom left, edge below z, matching'
        elif self.left[2] == self.front[3] and self.left[5] == self.front[0]:
            return 'white on top piece, bottom left, edge below z, reversed'
        
        # white piece on top, corresponding edge above
        elif self.left[1] == self.left[2] and self.top[3] == self.front[0]:
            return 'white on top piece, bottom left, edge above, matching'
        elif self.left[1] == self.front[0] and self.top[3] == self.left[2]:
            return 'white on top piece, bottom left, edge above, reversed'
        
        # white piece on top, corresponding edge to the right
        elif self.front[0] == self.front[1] and self.left[2] == self.top[7]:
            return 'white on top piece, bottom left, edge to the right, matching'
        elif self.left[2] == self.front[1] and self.front[0] == self.top[7]:
            return 'white on top piece, bottom left, edge to the right, reversed'
        
        return False
    
    def topRightZCornerCheck(self):

        # white piece on top, corresponding edge z below
        if self.back[0] == self.back[3] and self.right[2] == self.right[5]:
            return 'white on top piece, top right, edge below z, matching'
        elif self.back[3] == self.right[2] and self.back[0] == self.right[5]:
            return 'white on top piece, top right, edge below z, reversed'
        
        # white piece on top, corresponding edge to the left
        elif self.back[0] == self.back[1] and self.right[2] == self.top[1]:
            return 'white on top piece, top right, edge to the left, matching'
        elif self.back[1] == self.right[2] and self.top[1] == self.back[0]:
            return 'white on top piece, top right, edge to the left, reversed'
        
        # white piece on top, corresponding edge below
        elif self.right[1] == self.right[2] and self.back[0] == self.top[5]:
            return 'white on top piece, top right, edge below, matching'
        elif self.back[0] == self.right[1] and self.right[2] == self.top[5]:
            return 'white on top piece, top right, edge below, reversed'
        
        return False
    
    def bottomRightZCornerCheck(self):

        # white piece on top, corresponding edge z below
        if self.front[2] == self.front[5] and self.right[0] == self.right[3]:
            return 'white on top piece, bottom right, edge below z, matching'
        elif self.front[2] == self.right[3] and self.front[5] == self.right[0]:
            return 'white on top piece, bottom right, edge below z, reversed'
        
        # white piece on top, corresponding edge above
        elif self.right[0] == self.right[1] and self.top[5] == self.front[2]:
            return 'white on top piece, bottom right, edge above, matching'
        elif self.top[5] == self.right[0] and self.right[1] == self.front[2]:
            return 'white on top piece, bottom right, edge above, reversed'
        
        elif self.front[1] == self.front[2] and self.top[7] == self.right[0]:
            return 'white on top piece, bottom right, edge to the left, matching'
        elif self.top[7] == self.front[2] and self.front[1] == self.right[0]:
            return 'white on top piece, bottom right, edge to the left, reversed'
        
        return False
    
    def topLeftVerticalCornerCheck(self):
        self.comparisonEdgePieceFaceF2L = 'self.left'
        
        onTopCornerColor = self.top[0]
        toTheLeftCornerColor = self.left[0]

        if onTopCornerColor == self.top[3] and toTheLeftCornerColor == self.left[1]:
            return 'white on headlight piece, top left, edge below, matching'
        elif onTopCornerColor == self.left[1] and toTheLeftCornerColor == self.top[3]:
            return 'white on headlight piece, top left, edge below, reversed'
        
        elif onTopCornerColor == self.top[1] and toTheLeftCornerColor == self.back[1]:
            self.comparisonEdgePieceFaceF2L = 'self.back'
            return 'white on headlight piece, top left, edge to the right, matching'
        elif onTopCornerColor == self.back[1] and toTheLeftCornerColor == self.top[1]:
            self.comparisonEdgePieceFaceF2L = 'self.back'
            return 'white on headlight piece, top left, edge to the right, reversed'
        
        elif onTopCornerColor == self.back[5] and toTheLeftCornerColor == self.left[3]:
            return 'white on headlight piece, top left, edge below z, matching'
        elif onTopCornerColor == self.left[3] and toTheLeftCornerColor == self.back[5]:
            return 'white on headlight piece, top left, edge below z, reversed'
 
        return False
    
    def topLeftHorizontalCornerCheck(self):
        self.comparisonEdgePieceFaceF2L = 'self.back'

        onTopCornerColor = self.top[0]
        toTheBackCornerColor = self.back[2]
        
        if self.top[0] == self.top[1] and self.back[1] == self.back[2]:
            return 'white on outer piece, top left, edge to the right, matching'
        elif self.top[0] == self.back[1] and self.back[2] == self.top[1]:
            return 'white on outer piece, top left, edge to the right, reversed'
        
        elif self.top[0] == self.top[3] and self.back[2] == self.left[1]:
            self.comparisonEdgePieceFaceF2L = 'self.left'
            return 'white on outer piece, top left, edge below, matching'
        elif self.top[0] == self.left[1] and self.back[2] == self.top[3]:
            self.comparisonEdgePieceFaceF2L = 'self.left'
            return 'white on outer piece, top left, edge below, reversed'
        
        elif onTopCornerColor == self.left[3] and toTheBackCornerColor == self.back[5]:
            return 'white on outer piece, top left, edge below z, matching'
        elif onTopCornerColor == self.back[5] and toTheBackCornerColor == self.left[3]:
            return 'white on outer piece, top left, edge below z, reversed'
        
        return False
    
    def topRightVerticalCornerCheck(self):
        self.comparisonEdgePieceFaceF2L = 'self.right'

        onTopCornerColor = self.top[2]
        toTheRightCornerColor = self.right[2]
        
        if self.top[2] == self.top[5] and self.right[1] == self.right[2]:
            return 'white on headlight piece, top right, edge below, matching'
        elif self.top[2] == self.right[1] and self.top[5] == self.right[2]:
            return 'white on headlight piece, top right, edge below, reversed'

        if self.top[1] == self.top[2] and self.right[2] == self.back[1]:
            self.comparisonEdgePieceFaceF2L = 'self.back'
            return 'white on headlight piece, top right, edge to the left, matching'
        elif self.top[2] == self.back[1] and self.top[1] == self.right[2]:
            self.comparisonEdgePieceFaceF2L = 'self.back'
            return 'white on headlight piece, top right, edge to the left, reversed'
        
        elif onTopCornerColor == self.back[3] and toTheRightCornerColor == self.right[5]:
            return 'white on headlight piece, top right, edge below z, matching'
        elif onTopCornerColor == self.right[5] and toTheRightCornerColor == self.back[3]:
            return 'white on headlight piece, top right, edge below z, reversed'
        
        return False
    
    def topRightHorizontalCornerCheck(self):
        self.comparisonEdgePieceFaceF2L = 'self.back'

        onTopCornerColor = self.top[2]
        toTheBackCornerColor = self.back[0]
        
        if self.top[1] == self.top[2] and self.back[0] == self.back[1]:
            return 'white on outer piece, top right, edge to the left, matching'
        elif self.back[1] == self.top[2] and self.back[0] == self.top[1]:
            return 'white on outer piece, top right, edge to the left, reversed'
        
        elif self.top[2] == self.top[5] and self.back[0] == self.right[1]:
            self.comparisonEdgePieceFaceF2L = 'self.right'
            return 'white on outer piece, top right, edge below, matching'
        elif self.right[1] == self.top[2] and self.back[0] == self.top[5]:
            self.comparisonEdgePieceFaceF2L = 'self.right'
            return 'white on outer piece, top right, edge below, reversed'
        
        elif onTopCornerColor == self.right[5] and toTheBackCornerColor == self.back[3]:
            return 'white on outer piece, top right, edge below z, matching'
        elif onTopCornerColor == self.back[3] and toTheBackCornerColor == self.right[5]:
            return 'white on outer piece, top right, edge below z, reversed'
        
        return False
    
    def bottomLeftVerticalCornerCheck(self):
        self.comparisonEdgePieceFaceF2L = 'self.left'

        onTopCornerColor = self.top[6]
        toTheLeftCornerColor = self.left[2]
        
        if self.top[3] == self.top[6] and self.left[1] == self.left[2]:
            return 'white on headlight piece, bottom left, edge above, matching'
        elif self.left[1] == self.top[6] and self.top[3] == self.left[2]:
            return 'white on headlight piece, bottom left, edge above, reversed'

        elif self.top[6] == self.top[7] and self.left[2] == self.front[1]:
            self.comparisonEdgePieceFaceF2L = 'self.front'
            return 'white on headlight piece, bottom left, edge to the right, matching'
        elif self.front[1] == self.top[6] and self.top[7] == self.left[2]:
            self.comparisonEdgePieceFaceF2L = 'self.front'
            return 'white on headlight piece, bottom left, edge to the right, reversed'

        elif onTopCornerColor == self.front[3] and toTheLeftCornerColor == self.left[5]:
            return 'white on headlight piece, bottom left, edge below z, matching'
        elif onTopCornerColor == self.left[5] and toTheLeftCornerColor == self.front[3]:
            return 'white on headlight piece, bottom left, edge below z, reversed'
        
        return False
    
    def bottomLeftHorizontalCornerCheck(self):
        self.comparisonEdgePieceFaceF2L = 'self.front'

        onTopCornerColor = self.top[6]
        toTheFrontCornerColor = self.front[0]
        
        if self.top[6] == self.top[7] and self.front[0] == self.front[1]:
            return 'white on outer piece, bottom left, edge to the right, matching'
        elif self.top[6] == self.front[1] and self.front[0] == self.top[7]:
            return 'white on outer piece, bottom left, edge to the right, reversed'
        
        elif self.top[3] == self.top[6] and self.front[0] == self.left[1]:
            self.comparisonEdgePieceFaceF2L = 'self.left'
            return 'white on outer piece, bottom left, edge above, matching'
        elif self.top[6] == self.left[1] and self.front[0] == self.top[3]:
            self.comparisonEdgePieceFaceF2L = 'self.left'
            return 'white on outer piece, bottom left, edge above, reversed'
        
        elif onTopCornerColor == self.left[5] and toTheFrontCornerColor == self.front[3]:
            return 'white on outer piece, bottom left, edge below z, matching'
        elif onTopCornerColor == self.front[3] and toTheFrontCornerColor == self.left[5]:
            return 'white on outer piece, bottom left, edge below z, reversed'  
        
        return False
    
    def bottomRightVerticalCornerCheck(self):
        self.comparisonEdgePieceFaceF2L = 'self.right'

        onTopCornerColor = self.top[8]
        toTheRightCornerColor = self.right[0]
        
        if self.top[5] == self.top[8] and self.right[0] == self.right[1]:
            return 'white on headlight piece, bottom right, edge above, matching'
        elif self.top[5] == self.right[0] and self.top[8] == self.right[1]:
            return 'white on headlight piece, bottom right, edge above, reversed'

        elif self.top[7] == self.top[8] and self.right[0] == self.front[1]:
            self.comparisonEdgePieceFaceF2L = 'self.front'
            return 'white on headlight piece, bottom right, edge to the left, matching'
        elif self.top[7] == self.right[0] and self.top[8] == self.front[1]:
            self.comparisonEdgePieceFaceF2L = 'self.front'
            return 'white on headlight piece, bottom right, edge to the left, reversed'
        
        elif onTopCornerColor == self.front[5] and toTheRightCornerColor == self.right[3]:
            return 'white on headlight piece, bottom right, edge below z, matching'
        elif onTopCornerColor == self.right[3] and toTheRightCornerColor == self.front[5]:
            return 'white on headlight piece, bottom right, edge below z, reversed'
        
        return False
    
    def bottomRightHorizontalCornerCheck(self):
        self.comparisonEdgePieceFaceF2L = 'self.front'

        onTopCornerColor = self.top[8]
        toTheFrontCornerColor = self.front[2]
        
        if self.top[7] == self.top[8] and self.front[1] == self.front[2]:
            return 'white on outer piece, bottom right, edge to the left, matching'
        elif self.top[7] == self.front[2] and self.top[8] == self.front[1]:
            return 'white on outer piece, bottom right, edge to the left, reversed'
        
        elif self.top[5] == self.top[8] and self.right[1] == self.front[2]:
            self.comparisonEdgePieceFaceF2L = 'self.right'
            return 'white on outer piece, bottom right, edge above, matching'
        elif self.top[5] == self.front[2] and self.top[8] == self.right[1]:
            self.comparisonEdgePieceFaceF2L = 'self.right'
            return 'white on outer piece, bottom right, edge above, reversed'
        
        elif onTopCornerColor == self.right[3] and toTheFrontCornerColor == self.front[5]:
            return 'white on outer piece, bottom right, edge below z, matching'
        elif onTopCornerColor == self.front[5] and toTheFrontCornerColor == self.right[3]:
            return 'white on outer piece, bottom right, edge below z, reversed'
        
        return False
    

    def topLeftSeparatedCornerCheck(self, WhiteColorFace):
        if WhiteColorFace == 'self.top':

            # edge in top layer
            if self.left[0] == self.right[1] and self.back[2] == self.top[5]:
                return 'matching'
            elif self.left[0] == self.top[5] and self.back[2] == self.right[1]:
                return 'matching'
            
            elif self.left[0] == self.front[1] and self.back[2] == self.top[7]:
                return 'matching'
            elif self.left[0] == self.top[7] and self.back[2] == self.front[1]:
                return 'matching'
            
            # edge in middle layer
            elif self.left[0] == self.front[3] and self.back[2] == self.left[5]:
                return 'matching'
            elif self.left[0] == self.left[5] and self.back[2] == self.front[3]:
                return 'reversed'
            
            elif self.left[0] == self.right[3] and self.back[2] == self.front[5]:
                return 'matching'
            elif self.left[0] == self.front[5] and self.back[2] == self.right[3]:
                return 'reversed'
            
            elif self.left[0] == self.back[3] and self.back[2] == self.right[5]:
                return 'matching'
            elif self.left[0] == self.right[5] and self.back[2] == self.back[3]:
                return 'reversed'

        elif WhiteColorFace == 'self.back':
            if self.left[0] == self.right[1] and self.top[0] == self.top[5]:
                return 'matching'
            elif self.left[0] == self.top[5] and self.top[0] == self.right[1]:
                return 'reversed'

            elif self.left[0] == self.front[1] and self.top[0] == self.top[7]:
                return 'matching'
            elif self.left[0] == self.top[7] and self.top[0] == self.front[1]:
                return 'reversed'
            
            # edge in middle layer
            elif self.left[0] == self.front[3] and self.top[0] == self.left[5]:
                return 'matching'
            elif self.left[0] == self.left[5] and self.top[0] == self.front[3]:
                return 'reversed'
            
            elif self.left[0] == self.right[3] and self.top[0] == self.front[5]:
                return 'matching'
            elif self.left[0] == self.front[5] and self.top[0] == self.right[3]:
                return 'reversed'
            
            elif self.left[0] == self.back[3] and self.top[0] == self.right[5]:
                return 'matching'
            elif self.left[0] == self.right[5] and self.top[0] == self.back[3]:
                return 'reversed'

        # whiteColorFace = self.left  
        else:
            if self.back[2] == self.right[1] and self.top[0] == self.top[5]:
                return 'matching'
            elif self.back[2] == self.top[5] and self.top[0] == self.right[1]:
                return 'reversed'

            elif self.back[2] == self.front[1] and self.top[0] == self.top[7]:
                return 'matching'
            elif self.back[2] == self.top[7] and self.top[0] == self.front[1]:
                return 'reversed'
            
            # edge in middle layer
            elif self.back[2] == self.left[5] and self.top[0] == self.front[3]:
                return 'matching'
            elif self.back[2] == self.front[3] and self.top[0] == self.left[5]:
                return 'reversed'
            
            elif self.back[2] == self.front[5] and self.top[0] == self.right[3]:
                return 'matching'
            elif self.back[2] == self.right[3] and self.top[0] == self.front[5]:
                return 'reversed'
            
            elif self.back[2] == self.right[5] and self.top[0] == self.back[3]:
                return 'matching'
            elif self.back[2] == self.back[3] and self.top[0] == self.right[5]:
                return 'reversed'
            
        return False
  
    def topRightSeparatedCornerCheck(self, WhiteColorFace):
        if WhiteColorFace == 'self.top':
            if self.right[2] == self.left[1] and self.back[0] == self.top[3]:
                return 'matching'
            elif self.right[2] == self.top[3] and self.back[0] == self.left[1]:
                return 'matching'
            
            elif self.right[2] == self.front[1] and self.back[0] == self.top[7]:
                return 'matching'
            elif self.right[2] == self.top[7] and self.back[0] == self.front[1]:
                return 'matching'
            
            # edge in middle layer
            elif self.back[0] == self.left[3] and self.right[2] == self.back[5]:
                return 'matching'
            elif self.back[0] == self.back[5] and self.right[2] == self.left[3]:
                return 'reversed'
            
            elif self.back[0] == self.front[3] and self.right[2] == self.left[5]:
                return 'matching'
            elif self.back[0] == self.left[5] and self.right[2] == self.front[3]:
                return 'reversed'
            
            elif self.back[0] == self.right[3] and self.right[2] == self.front[5]:
                return 'matching'
            elif self.back[0] == self.front[5] and self.right[2] == self.right[3]:
                return 'reversed'
            

        if WhiteColorFace == 'self.right':
            if self.back[0] == self.front[1] and self.top[2] == self.top[7]:
                return 'matching'
            elif self.back[0] == self.top[7] and self.top[2] == self.front[1]:
                return 'reversed'
            
            elif self.back[0] == self.left[1] and self.top[2] == self.top[3]:
                return 'matching'
            elif self.back[0] == self.top[3] and self.top[2] == self.left[1]:
                return 'reversed'

            # edge in middle layer
            elif self.back[0] == self.left[3] and self.top[2] == self.back[5]:
                return 'matching'
            elif self.back[0] == self.back[5] and self.top[2] == self.left[3]:
                return 'reversed'
            
            elif self.back[0] == self.front[3] and self.top[2] == self.left[5]:
                return 'matching'
            elif self.back[0] == self.left[5] and self.top[2] == self.front[3]:
                return 'reversed'
            
            elif self.back[0] == self.right[3] and self.top[2] == self.front[5]:
                return 'matching'
            elif self.back[0] == self.front[5] and self.top[2] == self.right[3]:
                return 'reversed'
        
        # whiteColorFace = self.back
        else:
            if self.right[2] == self.left[1] and self.top[2] == self.top[3]:
                return 'matching'
            elif self.right[2] == self.top[3] and self.top[2] == self.left[1]:
                return 'reversed'
            
            elif self.right[2] == self.front[1] and self.top[2] == self.top[7]:
                return 'matching'
            elif self.right[2] == self.top[7] and self.top[2] == self.front[1]:
                return 'reversed'
            
            # edge in middle layer
            elif self.top[2] == self.left[3] and self.right[2] == self.back[5]:
                return 'matching'
            elif self.top[2] == self.back[5] and self.right[2] == self.left[3]:
                return 'reversed'
            
            elif self.top[2] == self.front[3] and self.right[2] == self.left[5]:
                return 'matching'
            elif self.top[2] == self.left[5] and self.right[2] == self.front[3]:
                return 'reversed'
            
            elif self.top[2] == self.right[3] and self.right[2] == self.front[5]:
                return 'matching'
            elif self.top[2] == self.front[5] and self.right[2] == self.right[3]:
                return 'reversed'
            
        return False
        
    def bottomLeftSeparatedCornerCheck(self, WhiteColorFace):
        if WhiteColorFace == 'self.top':
            if self.front[0] == self.back[1] and self.left[2] == self.top[1]:
                return 'matching'
            elif self.front[0] == self.top[1] and self.left[2] == self.back[1]:
                return 'matching'
            
            if self.front[0] == self.right[1] and self.left[2] == self.top[5]:
                return 'matching'
            elif self.front[0] == self.top[5] and self.left[2] == self.right[1]:
                return 'matching'
            
            # edge in middle layer
            elif self.front[0] == self.right[3] and self.left[2] == self.front[5]:
                return 'matching'
            elif self.front[0] == self.front[5] and self.left[2] == self.right[3]:
                return 'reversed'
            
            elif self.front[0] == self.back[3] and self.left[2] == self.right[5]:
                return 'matching'
            elif self.front[0] == self.right[5] and self.left[2] == self.back[3]:
                return 'reversed'
            
            elif self.front[0] == self.left[3] and self.left[2] == self.back[5]:
                return 'matching'
            elif self.front[0] == self.back[5] and self.left[2] == self.left[3]:
                return 'reversed'

        if WhiteColorFace == 'self.front':
            if self.left[2] == self.right[1] and self.top[5] == self.top[6]:
                return 'matching'
            elif self.left[2] == self.top[5] and self.top[6] == self.right[1]:
                return 'reversed'
            
            elif self.left[2] == self.back[1] and self.top[1] == self.top[6]:
                return 'matching'
            elif self.left[2] == self.top[1] and self.back[1] == self.top[6]:
                return 'reversed'
            
            # edge in middle layer
            elif self.top[6] == self.right[3] and self.left[2] == self.front[5]:
                return 'matching'
            elif self.top[6] == self.front[5] and self.left[2] == self.right[3]:
                return 'reversed'
            
            elif self.top[6] == self.back[3] and self.left[2] == self.right[5]:
                return 'matching'
            elif self.top[6] == self.right[5] and self.left[2] == self.back[3]:
                return 'reversed'
            
            elif self.top[6] == self.left[3] and self.left[2] == self.back[5]:
                return 'matching'
            elif self.top[6] == self.back[5] and self.left[2] == self.left[3]:
                return 'reversed'

        # whiteColorFace = self.left 
        else:
            if self.front[0] == self.right[1] and self.top[5] == self.top[6]:
                return 'matching'
            elif self.front[0] == self.top[5] and self.top[6] == self.right[1]:
                return 'reversed'
            
            elif self.front[0] == self.back[1] and self.top[1] == self.top[6]:
                return 'matching'
            elif self.front[0] == self.top[1] and self.back[1] == self.top[6]:
                return 'reversed'
            
            # edge in middle layer
            elif self.front[0] == self.right[3] and self.top[6] == self.front[5]:
                return 'matching'
            elif self.front[0] == self.front[5] and self.top[6] == self.right[3]:
                return 'reversed'
            
            elif self.front[0] == self.back[3] and self.top[6] == self.right[5]:
                return 'matching'
            elif self.front[0] == self.right[5] and self.top[6] == self.back[3]:
                return 'reversed'
            
            elif self.front[0] == self.left[3] and self.top[6] == self.back[5]:
                return 'matching'
            elif self.front[0] == self.back[5] and self.top[6] == self.left[3]:
                return 'reversed'
        
        return False
            
    def bottomRightSeparatedCornerCheck(self, WhiteColorFace):
        if WhiteColorFace == 'self.top':
            if self.front[2] == self.back[1] and self.right[0] == self.top[1]:
                return 'matching'
            elif self.front[2] == self.top[1] and self.right[0] == self.back[1]:
                return 'matching'
            
            elif self.front[2] == self.left[1] and self.right[0] == self.top[3]:
                return 'matching'
            elif self.front[2] == self.top[3] and self.right[0] == self.left[1]:
                return 'matching'
            
            # edge in middle layer
            elif self.right[0] == self.back[3] and self.front[2] == self.right[5]:
                return 'matching'
            elif self.right[0] == self.right[5] and self.front[2] == self.back[3]:
                return 'reversed'

            elif self.right[0] == self.left[3] and self.front[2] == self.back[5]:
                return 'matching'
            elif self.right[0] == self.back[5] and self.front[2] == self.left[3]:
                return 'reversed'
            
            elif self.right[0] == self.front[3] and self.front[2] == self.left[5]:
                return 'matching'
            elif self.right[0] == self.left[5] and self.front[2] == self.front[3]:
                return 'reversed'

        if WhiteColorFace == 'self.right':
            if self.front[2] == self.back[1] and self.top[1] == self.top[8]:
                return 'matching'
            elif self.front[2] == self.top[1] and self.top[8] == self.back[1]:
                return 'reversed'
            
            elif self.front[2] == self.left[1] and self.top[8] == self.top[3]:
                return 'matching'
            elif self.front[2] == self.top[3] and self.top[8] == self.left[1]:
                return 'reversed'

            # edge in middle layer
            elif self.top[8] == self.back[3] and self.front[2] == self.right[5]:
                return 'matching'
            elif self.top[8] == self.right[5] and self.front[2] == self.back[3]:
                return 'reversed'

            elif self.top[8] == self.left[3] and self.front[2] == self.back[5]:
                return 'matching'
            elif self.top[8] == self.back[5] and self.front[2] == self.left[3]:
                return 'reversed'
            
            elif self.top[8] == self.front[3] and self.front[2] == self.left[5]:
                return 'matching'
            elif self.top[8] == self.left[5] and self.front[2] == self.front[3]:
                return 'reversed'

        # whiteColorFace = self.front  
        else:
            if self.right[0] == self.back[1] and self.top[1] == self.top[8]:
                return 'matching'
            elif self.right[0] == self.top[1] and self.top[8] == self.back[1]:
                return 'reversed'
            
            elif self.right[0] == self.left[1] and self.top[3] == self.top[8]:
                return 'matching'
            elif self.right[0] == self.top[3] and self.top[8] == self.left[1]:
                return 'reversed'
            
            # edge in middle layer
            elif self.right[0] == self.back[3] and self.top[8] == self.right[5]:
                return 'matching'
            elif self.right[0] == self.right[5] and self.top[8] == self.back[3]:
                return 'reversed'

            elif self.right[0] == self.left[3] and self.top[8] == self.back[5]:
                return 'matching'
            elif self.right[0] == self.back[5] and self.top[8] == self.left[3]:
                return 'reversed'
            
            elif self.right[0] == self.front[3] and self.top[8] == self.left[5]:
                return 'matching'
            elif self.right[0] == self.left[5] and self.top[8] == self.front[3]:
                return 'reversed'
            
        return False


    def verticalWhiteNotOnTopF2L(self, whichCorner, whiteOnTopAfterMoving, matchedScrunchedAfterMoving, rightOrBottomEdgeIfWhiteOnTop):
        # get the moves to move the vertical pair to a horizontal pair in the top layer
        movesVerticalToHorizontal, comparisonFace, _, edgePieceLeftOrRight = self.goingFromVerticalToHorizontalPairF2L[whichCorner]

        # execute the moves
        for move in movesVerticalToHorizontal:
            move()

        # insert the pair into it's final position
        if whiteOnTopAfterMoving:
            self.whiteOnTopEdgeAdjacent(edgePieceLeftOrRight, comparisonFace, rightOrBottomEdgeIfWhiteOnTop)
        else:
            if matchedScrunchedAfterMoving:
                self.scrunchedMatchingTopF2L(edgePieceLeftOrRight, comparisonFace, 'Connected', 'Double')
            else:
                self.reversedHorizontalPairF2L(edgePieceLeftOrRight, comparisonFace, 'Scrunched', 'Together', False)

    def scrunchedMatchingTopF2L(self, edgePieceLeftOrRight, comparisonFace, separateOrConnected, doubleOrSingleRotation):
        # 'Right', 'self.front', 'Connected', 'Double'
        if separateOrConnected == 'Connected':
            # separate the matching scrunched F2L pair
            comparisonFace = self.splittingF2Pair(edgePieceLeftOrRight, comparisonFace, False)

        garbageCorner = self.findAGarbageCorner()

        # rotate and get the moves to connect the separated scrunched pieces
        if edgePieceLeftOrRight == 'Left':
            if doubleOrSingleRotation == 'Double':
                self.rotatingTopLayerReveredPairF2L(self.faceToTurnToDependingOnWhichCornerIsGarbageScrunchedEdgeOnLeft, comparisonFace, garbageCorner)
            else:
                self.rotatingTopLayerReveredPairF2L(self.faceToTurnToDependingOnWhichCornerIsGarbageOneTurnEdgeOnLeft, comparisonFace, garbageCorner)
            movesToConnectSeparateScrunchedPieces, secondComparisonFace = self.movesToConnectSeparateScrunchedPiecesEdgeOnLeftF2L[garbageCorner]
        else:
            if doubleOrSingleRotation == 'Double':
                self.rotatingTopLayerReveredPairF2L(self.faceToTurnToDependingOnWhichCornerIsGarbageScrunchedEdgeOnRight, comparisonFace, garbageCorner)
            else:
                self.rotatingTopLayerReveredPairF2L(self.faceToTurnToDependingOnWhichCornerIsGarbageOneTurnEdgeOnRight, comparisonFace, garbageCorner)
            movesToConnectSeparateScrunchedPieces, secondComparisonFace = self.movesToConnectSeparateScrunchedPiecesEdgeOnRightF2L[garbageCorner]
        
        # execute the moves to correctly connect the pieces
        if doubleOrSingleRotation == 'Double':
            for moves in movesToConnectSeparateScrunchedPieces:
                moves()
        else:
            for i in range(len(movesToConnectSeparateScrunchedPieces)):
                if i == 2:
                    continue
                movesToConnectSeparateScrunchedPieces[i]()

        # insert the F2L pair into it's final position
        if edgePieceLeftOrRight == 'Left':
            self.whiteOnOuterF2L(secondComparisonFace, True, False)
        else:
            self.whiteOnOuterF2L(secondComparisonFace, False, False)

    def whiteOnTopEdgeAdjacent(self, edgePieceLeftOrRight, comparisonFace, separatedEdgeToTheRightOrBottom):

        # separate the reversed F2L pair
        secondComparisonFace = self.splittingF2Pair(edgePieceLeftOrRight, comparisonFace, True)

        # connect and place separated F2L pair into final spot
        self.whiteOnTopEdgeSeparated(secondComparisonFace, separatedEdgeToTheRightOrBottom)

    def splittingF2Pair(self, edgePieceLeftOrRight, comparisonFace, doubleTopLayerRotation):

        # find an unsolved corner
        garbageCorner = self.findAGarbageCorner()
    
        # rotate top layer and get moves to use the garbage corner and separate the reversed pair
        if edgePieceLeftOrRight == 'Left':
            self.rotatingTopLayerReveredPairF2L(self.faceToTurnToDependingOnWhichCornerIsGarbageEdgeOnLeft, comparisonFace, garbageCorner)
            movesToSplitReversedPairF2L, secondComparisonFaceWhiteOnTop, secondComparisonFaceWhiteOnSide = self.movesToSeparateOnGarbageCornerWhiteOnRightF2L[garbageCorner]
        else:
            self.rotatingTopLayerReveredPairF2L(self.faceToTurnToDependingOnWhichCornerIsGarbageEdgeOnRight, comparisonFace, garbageCorner)
            movesToSplitReversedPairF2L, secondComparisonFaceWhiteOnTop, secondComparisonFaceWhiteOnSide = self.movesToSeparateOnGarbageCornerWhiteOnLeftF2L[garbageCorner]
        
        # execute the moves
        if doubleTopLayerRotation:
            for move in movesToSplitReversedPairF2L:
                move()
            return secondComparisonFaceWhiteOnTop
        
        else:
            for i in range(len(movesToSplitReversedPairF2L)):
                if i == 2:
                    continue
                movesToSplitReversedPairF2L[i]()

            return secondComparisonFaceWhiteOnSide

    def reversedHorizontalPairF2L(self, edgePieceLeftOrRight, comparisonFace, straightOrScrunched, splitOrTogether, rotateBefore):
        
        if rotateBefore:
            garbageCorner = self.findAGarbageCorner()
            if edgePieceLeftOrRight == 'Left':

                # dictionary is for scrunched but has correct key value pairs even though it is for edge on right (the F2L pair is straight not scrunched in this situation)
                self.rotatingTopLayerReveredPairF2L(self.faceToTurnToDependingOnWhichCornerIsGarbageEdgeOnRight, comparisonFace, garbageCorner)
                movesToAlignIntoNormalInsertPair, comparisonFace, _ = self.movesToSeparateOnGarbageCornerWhiteOnRightF2L[garbageCorner]
                for i in range(len(movesToAlignIntoNormalInsertPair)):
                    if i == 2:
                        continue
                    movesToAlignIntoNormalInsertPair[i]()
            else:
                
                self.rotatingTopLayerReveredPairF2L(self.faceToTurnToDependingOnWhichCornerIsGarbageEdgeOnLeft, comparisonFace, garbageCorner)
                movesToAlignIntoNormalInsertPair, comparisonFace, _ = self.movesToSeparateOnGarbageCornerWhiteOnLeftF2L[garbageCorner]
                for i in range(len(movesToAlignIntoNormalInsertPair)):
                    if i == 2:
                        continue
                    movesToAlignIntoNormalInsertPair[i]()

        # separate the reversed F2L pair
        if splitOrTogether == 'Together':
            if straightOrScrunched == 'Straight':
                comparisonFace = self.splittingF2Pair(edgePieceLeftOrRight, comparisonFace, True)
            else:
                comparisonFace = self.splittingF2Pair(edgePieceLeftOrRight, comparisonFace, False)
        
        # rotate top layer and get moves to insert into the final position
        if straightOrScrunched == 'Straight':
            if edgePieceLeftOrRight == 'Left':
                self.movingTopLayerToPrepForInputF2L(self.onePlusEdgeColorFaceWhiteOnTheRight, False, comparisonFace)
                movesToConnectPair = self.connectingOppositeF2LPiecesEdgeOnRight[self.comparisonColorF2L]
            else:
                self.movingTopLayerToPrepForInputF2L(self.onePlusEdgeColorFaceWhiteOnTheLeft, False, comparisonFace)
                movesToConnectPair = self.connectingOppositeF2LPiecesEdgeOnLeft[self.comparisonColorF2L]
                
        
        else:
            if edgePieceLeftOrRight == 'Left':
                self.movingTopLayerToPrepForInputF2L(self.onePlusEdgeColorFaceWhiteOnTheLeft, False, comparisonFace)
                movesToConnectPair = self.connectingOppositeF2LPiecesEdgeOnLeft[self.comparisonColorF2L]
            else:
                self.movingTopLayerToPrepForInputF2L(self.onePlusEdgeColorFaceWhiteOnTheRight, False, comparisonFace)
                movesToConnectPair = self.connectingOppositeF2LPiecesEdgeOnRight[self.comparisonColorF2L]
                
        # execute moves
        for moves in movesToConnectPair:
            moves()

    def reversedVerticalPairWhiteTop(self, whichCorner):

        # get the moves to get the pair from vertical to horizontal on the top layer
        movesVerticalToHorizontal, comparisonFace, _, edgePieceLeftOrRight = self.goingFromVerticalToHorizontalPairF2L[whichCorner]

        # execute moves
        for move in movesVerticalToHorizontal:
            move()

        self.reversedHorizontalPairF2L(edgePieceLeftOrRight, comparisonFace, 'Straight', 'Together', False)

    def rotatingTopLayerReveredPairF2L(self, finalFaceDict, comparisonFace, garbageCorner):
        self.comparisonEdgePieceFaceF2L = comparisonFace

        while self.comparisonEdgePieceFaceF2L != finalFaceDict[garbageCorner]:
                
                # turn the top layer of the cube and re-assign what face the F2L is on
                self.UPrime()
                horizontalColorsIndex = self.horizontalColors.index(self.sidesToColors[self.comparisonEdgePieceFaceF2L])
                if horizontalColorsIndex != 3:
                    self.comparisonEdgePieceFaceF2L = self.colorsToSides[self.horizontalColors[horizontalColorsIndex+1]]
                else:
                    self.comparisonEdgePieceFaceF2L = self.colorsToSides[self.horizontalColors[0]]

    def findAGarbageCorner(self):
        self.cubeCorners = [[self.left[3], self.left[6], self.back[5], self.back[8]],
                            [self.right[5], self.right[8], self.back[3], self.back[6]],
                            [self.front[3], self.front[6], self.left[5], self.left[8]],
                            [self.front[6], self.front[8], self.right[3], self.right[6]]]
        
        if self.cubeCorners[0] != ['green', 'green', 'red', 'red']:
            return 'top left'
        elif self.cubeCorners[1] != ['blue', 'blue', 'red', 'red']:
            return 'top right'
        elif self.cubeCorners[2] != ['orange', 'orange', 'green', 'green']:
            return 'bottom left'
        elif self.cubeCorners[3] != ['orange', 'orange', 'blue', 'blue']:
            return 'bottom right'

    def whiteOnTopLeftEdgeOnBottom(self, firstComparisonFace):

        # move top so edge is lined up with correct side
        self.comparisonEdgePieceFaceF2L = firstComparisonFace
        self.movingTopLayerToPrepForInputF2L(self.onePlusEdgeColorFaceWhiteOnTheLeft, True, firstComparisonFace)  

        # make into an adjacent pair
        constructF2LPair, leftOrRight = self.whichWayToTurnWhiteOnTopEdgeToTheRightF2L[self.comparisonColorF2L][self.otherColorF2L]
        for move in constructF2LPair:
            move()

        # inserting piece into final spot
        moves = self.insertingConstructedF2LPairWhitePieceOnTheLeft[self.comparisonEdgePieceColorF2L]
        if leftOrRight == 'Left':
            for executeMove in moves:
                executeMove()
        else:
            for move in moves:
                executeMove = self.movesAndReverseDict[move]
                executeMove()

    def whiteOnTopEdgeSeparated(self, comparisonFace, edgeToTheRightOrBottom):

        # rotate top layer to align edge with matching face
        self.movingTopLayerToPrepForInputF2L(self.onePlusEdgeColorFaceWhiteOnTheLeft, True, comparisonFace)
        
        # get moves to connect the separate corner and edge pair
        moves, secondComparisonFace, isWhiteOnLeft  = self.movesConnectingSeparateF2LPiecesWhiteOnTop[self.comparisonColorF2L][self.otherColorF2L]
        
        # execute the moves
        if edgeToTheRightOrBottom == 'Right':
            for executeMove in moves:
                executeMove()
        else:
            if self.otherColorF2L == next(iter(self.movesConnectingSeparateF2LPiecesWhiteOnTop[self.comparisonColorF2L])):
                for i in range(len(moves)):
                    moves[i]()
                    if i == 1:
                        moves[i]()
            else:
                for i in range(len(moves)):
                    if i == 2:
                        continue
                    moves[i]()
                    
        # insert the connected pair to it's final spot
        self.whiteOnOuterF2L(secondComparisonFace, isWhiteOnLeft, False)
    
    def verticalPairWhiteOnTop(self, whichCorner):

        # getting the piece from vertical to horizontal on the top layerx8i
        movesVerticalToHorizontal, comparisonFace, whiteLeftOrRight, _ = self.goingFromVerticalToHorizontalPairF2L[whichCorner]

        for move in movesVerticalToHorizontal:
            move()

        # rotating to the correct face
        if whiteLeftOrRight == 'Left':
                                              # (finalFaceDict, isWhiteOnTop, comparisonFace)
            self.movingTopLayerToPrepForInputF2L(self.onePlusEdgeColorFaceWhiteOnTheLeft, False, comparisonFace)
        else:
            self.movingTopLayerToPrepForInputF2L(self.onePlusEdgeColorFaceWhiteOnTheRight, False, comparisonFace)

        # inserting piece into final spot
        moves = self.insertingConstructedF2LPairWhitePieceOnTheLeft[self.comparisonColorF2L]
        if whiteLeftOrRight == 'Left':
            for executeMove in moves:
                executeMove()
        else:
            for move in moves:
                executeMove = self.movesAndReverseDict[move]
                executeMove()

    def whiteOnOuterF2L(self, comparisonEdgePieceFace, isWhiteOnLeft, isWhiteOnTop):

        # set the comparison edge piece face
        self.comparisonEdgePieceFaceF2L = comparisonEdgePieceFace

        # move the top layer to get prepare for final insertion
        if isWhiteOnLeft:
                                              # (finalFaceDict, isWhiteOnTop, comparisonFace)
            self.movingTopLayerToPrepForInputF2L(self.onePlusEdgeColorFaceWhiteOnTheLeft, isWhiteOnTop, comparisonEdgePieceFace)
        else:
            self.movingTopLayerToPrepForInputF2L(self.onePlusEdgeColorFaceWhiteOnTheRight, isWhiteOnTop, comparisonEdgePieceFace)

        # get the moves that will insert the F2L pair
        moves = self.insertingConstructedF2LPairWhitePieceOnTheLeft[self.comparisonColorF2L]

        # execute the moves
        if isWhiteOnLeft:
            for executeMove in moves:
                executeMove()
        else:
            for move in moves:
                executeMove = self.movesAndReverseDict[move]
                executeMove()

    def movingTopLayerToPrepForInputF2L(self, finalFaceDict, isWhiteOnTop, comparisonFace):

        # set the comparison edge piece face
        self.comparisonEdgePieceFaceF2L = comparisonFace

        # rotating top for when white is not on the side of the piece
        if not isWhiteOnTop:

            # turn the top layer until the edge color it is one away from it's corresponding face (cannot line up to the same color because of how piece is going to be inserted into final position)
            while self.comparisonEdgePieceFaceF2L != finalFaceDict[self.comparisonColorF2L]:

                # turn the top layer of the cube and re-assign what face the F2L is on
                self.UPrime()

                horizontalColorsIndex = self.horizontalColors.index(self.sidesToColors[self.comparisonEdgePieceFaceF2L])
                if horizontalColorsIndex != 3:
                    self.comparisonEdgePieceFaceF2L = self.colorsToSides[self.horizontalColors[horizontalColorsIndex+1]]
                else:
                    self.comparisonEdgePieceFaceF2L = self.colorsToSides[self.horizontalColors[0]]

        # rotating top for when white is on the top of the piece
        else:

            # turn the top layer until the edge color is on it's corresponding face
            while self.sidesToColors[self.comparisonEdgePieceFaceF2L] != self.comparisonColorF2L:

                # turn the top layer of the cube and re-assign what face the F2L is on
                self.UPrime()

                horizontalColorsIndex = self.horizontalColors.index(self.sidesToColors[self.comparisonEdgePieceFaceF2L])
                if horizontalColorsIndex != 3:
                    self.comparisonEdgePieceFaceF2L = self.colorsToSides[self.horizontalColors[horizontalColorsIndex+1]]
                else:
                    self.comparisonEdgePieceFaceF2L = self.colorsToSides[self.horizontalColors[0]]

    def findOtherEdgePieceForF2L(self, edgeColor1, edgeColor2):
        edgePieces = [['self.top', 'self.back', self.top[1], self.back[1]], ['self.top', 'self.left', self.top[3], self.left[1]], ['self.top', 'self.right', self.top[5], self.right[1]],
                      ['self.top', 'self.front', self.top[7], self.front[1]], ['self.front', 'self.left', self.front[3], self.left[5]], ['self.front', 'self.right', self.front[5], self.right[3]], 
                      ['self.right', 'self.back', self.right[5], self.back[3]], ['self.left', 'self.back', self.left[3], self.back[5]]]
            
        for i, piece in enumerate(edgePieces):
            if piece[2:] == [edgeColor1, edgeColor2] or piece[2:] == [edgeColor2, edgeColor1]:
                self.currentPrimaryEdgeFace = self.sidesToColors[piece[0]]
                if i < 4:
                    self.firstEdgePiecePositionF2L = str(i*2+1)
                elif i == 4 or i == 7:
                    self.firstEdgePiecePositionF2L = '3'
                else:
                    self.firstEdgePiecePositionF2L = '5'

                self.firstEdgePieceSideF2L = piece[0]
                self.secondEdgePieceSideF2L = piece[1]

                if i < 6:
                    self.comparisonColorF2L = piece[3]
                    self.otherColorF2L = piece[2]
                else:
                    self.comparisonColorF2L = piece[2]
                    self.otherColorF2L = piece[3]

                # return self.FirstEdgePieceSideF2L, self.SecondEdgePieceSideF2L, self.FirstEdgePiecePositionF2L
    

    def insertingAF2LPair(self, whiteCorner):

        cornerSpot = whiteCorner[10]
        if int(cornerSpot) > 4:     # if the corner piece is not on the top layer

            # moves to move the corner to the top layer
            movesToGetCornerToTopLayer = self.gettingCornerfromBottomLayerToTopLayer[cornerSpot]
            
            for move in movesToGetCornerToTopLayer:     # executing the moves
                move()

            # re-find a white corner piece after moving it to the top layer
            whiteCorner = self.findingASingularWhiteEdgePiece('corner')
            self.insertingAF2LPair(whiteCorner)     # insert the F2L pair when the corner is on the top layer
            return

        verticalOtherPieceColor = whiteCorner[1]
        secondOtherPieceColor = whiteCorner[4]
        whiteColorFace = whiteCorner[7]

        # find the F2L edge piece and assign both edge sides and positions
        self.findOtherEdgePieceForF2L(verticalOtherPieceColor, secondOtherPieceColor)
        edgeCornerRelationTest = self.topLayerCornerAndEdgePieceRelation[cornerSpot][whiteColorFace]
        areEdgeAndCornerTogether = edgeCornerRelationTest()

        # finds the second edge color position on the cube
        self.secondEdgePiecePositionF2L = self.gettingOtherEdgePositionFromFirstColorPosition[self.firstEdgePieceSideF2L][self.firstEdgePiecePositionF2L][0]
        
        # if the F2L pair is touching
        if areEdgeAndCornerTogether != False:
            inputToCornerRelatioMoves = areEdgeAndCornerTogether.split(', ')
            inputCornerSequenceResultsFromDictionaryPiecesTouching = self.cornerRelationMoves[inputToCornerRelatioMoves[0]][inputToCornerRelatioMoves[1]][inputToCornerRelatioMoves[2]][inputToCornerRelatioMoves[3]]
            
            # the function is the first element in the list
            movesForConnectedPieces = inputCornerSequenceResultsFromDictionaryPiecesTouching[0]
            arguments = inputCornerSequenceResultsFromDictionaryPiecesTouching[1:]
            movesForConnectedPieces(*arguments)

        # if the F2L pair are separate
        else:
            edgeSpot = self.twoEdgePiecePositionsToEdgePiece[self.firstEdgePieceSideF2L][self.firstEdgePiecePositionF2L]
           
            separatePiecesCheck = self.separatedCornerCheckF2L[cornerSpot]
            
            matchingReversedOrTurn = separatePiecesCheck(whiteColorFace)

            inputCornerSequenceResultsFromDictionaryPiecesSeparate = self.cornerRelationMovesWhenPiecesAreSeparated[cornerSpot][whiteColorFace][edgeSpot][matchingReversedOrTurn]

            if int(edgeSpot) > 4:
                movesToRotateTopLayer = self.topRotationsToMakeVerticalPairF2L[cornerSpot][edgeSpot]
                
                for move in movesToRotateTopLayer:  # rotate top layer to combine pieces into vertical F2L pair
                    move()

            movesForSeparatePieces = inputCornerSequenceResultsFromDictionaryPiecesSeparate[0]
            arguments = inputCornerSequenceResultsFromDictionaryPiecesSeparate[1:]
            movesForSeparatePieces(*arguments)  # insert pair into final spot
            return

    def solveF2L(self):
        if self.crossSolved:
            self.solvingCube = True
            self.statusBox.delete('1.0', 'end')
            self.statusBox.insert('1.0', 'F2L Solution:\n')

            # get a displaced white corner piece
            whiteCorner = self.findingASingularWhiteEdgePiece('corner')

            if not whiteCorner:
                return

            if whiteCorner:
                for _ in range(4):
                    self.insertingAF2LPair(whiteCorner)
                    whiteCorner = self.findingASingularWhiteEdgePiece('corner')
                    if not whiteCorner:
                        # F2L is solved!
                        # check the F2L checkbox
                        self.F2LSolved = True
                        self.checkbox_vars[1].set(1)
                        return
            
            # F2L is not solved :(
            return
        else:
            self.statusBox.delete('1.0', 'end')
            self.statusBox.insert('1.0', 'Need To Complete Previous Steps.')

    
    def testingF2L(self):
        self.testingAStep('F2L')




    def findingYellowPiecesOLL(self):
        firstLayerOfYellow = [1 if color == 'yellow' else 0 for color in self.back[2::-1]]
        secondLayerOfYellow = [1 if color == 'yellow' else 0 for color in [self.left[0]] + self.top[0:3] + [self.right[2]]]
        thirdLayerOfYellow = [1 if color == 'yellow' else 0 for color in [self.left[1]] + self.top[3:6] + [self.right[1]]]
        fourthLayerOfYellow = [1 if color == 'yellow' else 0 for color in [self.left[2]] + self.top[6:9] + [self.right[0]]]
        fifthLayerOfYellow = [1 if color == 'yellow' else 0 for color in self.front[0:3]]

        listOfYellowPieces = firstLayerOfYellow + secondLayerOfYellow + thirdLayerOfYellow + fourthLayerOfYellow + fifthLayerOfYellow
        listOfYellowPieces = ','.join(map(str, listOfYellowPieces))
        return listOfYellowPieces
                
    def findingAYellowPermutation(self, listOfYellowPieces):
        # see if any of the final OLL permutations are already present on the top layer
        if listOfYellowPieces in self.possibleOLLPerumtations:
            yellowPermutation, neededRotations = self.possibleOLLPerumtations[listOfYellowPieces]
            return yellowPermutation, neededRotations
        
        # if no final OLL see which beginning OLL there is
        else:
            numOfMatchingColors = 0
            for numOfPermutation, permutation in enumerate(self.nonFinalYellowPermutations):
                for permutationVariation in permutation[0]:
                    singleString = permutationVariation[0].replace(' ', '').replace('\n','')
                    for actual, theoretical in zip(listOfYellowPieces[:32:2], singleString[:32:2]):
                        if actual == theoretical == '1':
                            numOfMatchingColors += 1
                            if numOfPermutation != 2:
                                if numOfMatchingColors == 3:
                                    return permutation[1], permutationVariation[1]  # yellowPermutation, neededRotations
                            else:
                                if numOfMatchingColors == 1:
                                    return permutation[1], permutationVariation[1]  # yellowPermutation, neededRotations
                    numOfMatchingColors = 0

    def executingAnOLLAlgorithm(self, listOfYellowPieces):
        yellowPermutation, neededRotations = self.findingAYellowPermutation(listOfYellowPieces)
        
        # rotate top layer to position for OLL permutation if needed
        rotationMoves = self.rotations[neededRotations]
        for move in rotationMoves:
            move()
        
        # getting and executing the OLL algorithm
        permutationMoves = self.movesForOLLPermutations[yellowPermutation]
        for moves in permutationMoves:
            moves()

    def solveOLL(self):
        if self.F2LSolved:
            self.solvingCube = True
            self.statusBox.delete('1.0', 'end')
            self.statusBox.insert('1.0', 'OLL Solution:\n')

            listOfYellowPieces = self.findingYellowPiecesOLL()
            # a representation of an all yellow top, yellow = 1, non yellow = 0
            #   0,0,0,
            # 0,1,1,1,0,
            # 0,1,1,1,0,
            # 0,1,1,1,0,
            #   0,0,0

            # this is the same string as above just represented in one line
            allYellowOnTop ='0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0'

            # return if yellow side already solved
            if listOfYellowPieces == allYellowOnTop:
                return
            
            # solve the yellow side
            for _ in range(3):
                self.executingAnOLLAlgorithm(listOfYellowPieces)
                listOfYellowPieces = self.findingYellowPiecesOLL()

                if listOfYellowPieces == allYellowOnTop:
                    # update dictionary with the new sides
                    self.updatingColorsToRealSides()

                    # OLL is solved!
                    # check the OLL checkbox
                    self.OLLSolved = True
                    self.checkbox_vars[2].set(1)
                    return

            # update dictionary with the new sides
            self.updatingColorsToRealSides()

            # OLL is not solved:(
            return
        else:
            self.statusBox.delete('1.0', 'end')
            self.statusBox.insert('1.0', 'Need To Complete Previous Steps.')

    def testingOLL(self):
        self.testingAStep('OLL')




    def matchupTopLayerHeadlightsPLL(self):
        
        # if all headlights are already matching
        matchingHeadlights = self.back[0] == self.back[2] and self.left[0] == self.left[2] and self.front[0] == self.front[2] and self.right[0] == self.right[2]
        if matchingHeadlights:
            return
        
        # if all headlights are not already matching
        # this algorithm can be executed a maximum of two times
        for _ in range(2):
            
            # scan each side for matching headlights to rotate top layer into position for algorithm
            for numberOfSideChecked in range(4):
                # headlights of current side
                currentHeadlightsThatAreBeingScanned = self.colorsToRealSides[self.horizontalColors[numberOfSideChecked]][0:3:2]
                areHeadlightsMatching = currentHeadlightsThatAreBeingScanned[0] == currentHeadlightsThatAreBeingScanned[1]
                
                # if a side has matching headlights, rotate that side to the back so algorithm can be executed
                if areHeadlightsMatching:
                    neededRotation = self.movesForfirstPLLAlgorithm[numberOfSideChecked]
                    movesToRotate = self.rotations[neededRotation]
                    for move in movesToRotate:
                        move()
                    break   # no need to scan additional sides after rotation was made
    
            # get moves and execute PLL algorithm
            movesForMatchingHeadlightsAlgorithm = [self.RPrime, self.F, self.RPrime, self.B, self.B, self.R, 
                                                self.FPrime, self.RPrime, self.B, self.B, self.R, self.R]
            for move in movesForMatchingHeadlightsAlgorithm:
                move()

            # updating the dictionary with the new sides
            self.updatingColorsToRealSides()
            
            # if all headlights are matching exit function
            matchingHeadlights = self.back[0] == self.back[2] and self.left[0] == self.left[2] and self.front[0] == self.front[2] and self.right[0] == self.right[2]
            if matchingHeadlights:
                return
            
        return
    
    def getAndExecuteRotationMovesPLL(self):
        colorInBack = self.back[1]
        rotationNeeded = self.rotationToMatchTopLayer[colorInBack]
        movesToRotateTopLayer = self.rotations[rotationNeeded]

        for move in movesToRotateTopLayer:
            move()

    def matchupTopLayerMiddlePieces(self):

        # updating the dictionary with the new sides
        self.updatingColorsToRealSides()

        topLayerSolvedAndInPlace = (self.back[0] == self.back[1] == self.back[2] and
                        self.left[0] == self.left[1] == self.left[2] and
                        self.front[0] == self.front[1] == self.front[2] and
                        self.right[0] == self.right[1] == self.right[2] and
                        self.back[1] == 'red')
        
        topLayerSolvedAndNotInPlace = (self.back[0] == self.back[1] == self.back[2] and
                        self.left[0] == self.left[1] == self.left[2] and
                        self.front[0] == self.front[1] == self.front[2] and
                        self.right[0] == self.right[1] == self.right[2] and
                        self.back[1] != 'red')
        
        noMiddlePiecesSolved = (self.back[0] != self.back[1] and
                        self.left[0] != self.left[1] and
                        self.front[0] != self.front[1] and
                        self.right[0] != self.right[1])
        
        if topLayerSolvedAndInPlace:
            return
        
        elif topLayerSolvedAndNotInPlace:
            # rotate top layer to proper place
            self.getAndExecuteRotationMovesPLL()
            return

        # find and rotate the side that has all three matching colors so it is in the back
        if noMiddlePiecesSolved:

            # execute PLL Algorithm that places one edge in the correct spot
            for move in self.shiftingEdgesToTheRightPLLAlgorithm:
                move()

            # updating the dictionary with the new sides
            self.updatingColorsToRealSides()

        # find the solved side and rotate it to the back
        for numberOfSideChecked in range(4):
            currentSideTopLayer = self.colorsToRealSides[self.horizontalColors[numberOfSideChecked]][0:3]
            isCurrentSideTopLayerMatching = currentSideTopLayer[0] == currentSideTopLayer[1] == currentSideTopLayer[2]

            if isCurrentSideTopLayerMatching:
                neededRotation = self.movesForfirstPLLAlgorithm[numberOfSideChecked]
                movesToRotate = self.rotations[neededRotation]
                for move in movesToRotate:
                    move()

                break   # no need to scan additional sides after rotation was made

        # execute PLL Algorithm that shifts the edges to the right and makes all sides have a solid color
        if self.front[1] == self.right[0]:
            for move in self.shiftingEdgesToTheRightPLLAlgorithm:
                move()

        # execute PLL Algorithm that shifts the edges to the left and makes all sides have a solid color
        else:
            for move in self.shiftingEdgesToTheLeftPLLAlgorithm:
                move()
        
        # if the cube is solved then the top layer on the front side will be orange
        isTopLayerRotatedCorrectly = self.front[1] == 'orange'

        # rotate the top layer to solve the cube if it is not already solved
        if not isTopLayerRotatedCorrectly:
            self.getAndExecuteRotationMovesPLL()
        
        return
            
    def solvePLL(self):
        if self.OLLSolved:
            self.solvingCube = True
            self.statusBox.delete('1.0', 'end')
            self.statusBox.insert('1.0', 'PLL Solution:\n')

            # matchup top layer headlights on all sides
            self.matchupTopLayerHeadlightsPLL()

            # matchup top layer middle pieces on all sides
            self.matchupTopLayerMiddlePieces()

            # check the PLL checkbox
            self.PLLSolved = True
            self.checkbox_vars[3].set(1)
            return
        else:
            self.statusBox.delete('1.0', 'end')
            self.statusBox.insert('1.0', 'Need To Complete Previous Steps.')




    def solveCube(self):
        # cube already solved
        if (self.top == ['yellow']*9 and
           self.left == ['green']*9 and
           self.front == ['orange']*9 and
           self.right == ['blue']*9 and 
           self.back == ['red']*9 and 
           self.bottom == ['white']*9):
            
            return
                
        self.solveCross()
        self.solveF2L()
        self.solveOLL()
        self.solvePLL()

        if (self.top != ['yellow']*9 or 
           self.left != ['green']*9 or 
           self.front != ['orange']*9 or 
           self.right != ['blue']*9 or 
           self.back != ['red']*9 or 
           self.bottom != ['white']*9):
            
            # cube is not solved :(
            return
        
        # cube is solved!
        self.crossSolved = True
        self.F2LSolved = True
        self.OLLSolved = True
        self.PLLSolved = True
        self.moves.numOfMoves = 0
        return
    
    def testingSolveCube(self):
        self.testingAStep('solveCube')

    def testDistanceFromEndOfStatusBox(self, moveName):
        if self.solvingCube:
            currentInsertionPoint = self.statusBox.index('end-1c')

            # 65 characters in a tkinter textbox
            distanceToEndOfLine = 65 - int(currentInsertionPoint.split('.')[1])
            if distanceToEndOfLine <= 2:
                self.statusBox.insert('end', '\n')

            self.statusBox.insert('end', f'{moveName} ')
            return

    def R(self):
        self.front, self.top, self.back, self.bottom, self.right, self.left = self.moves.R()
        self.testDistanceFromEndOfStatusBox('R')
    
    def RPrime(self):
        self.front, self.top, self.back, self.bottom, self.right, self.left = self.moves.RPrime()
        self.testDistanceFromEndOfStatusBox('R\'')
    
    def L(self):
        self.front, self.top, self.back, self.bottom, self.right, self.left = self.moves.L()
        self.testDistanceFromEndOfStatusBox('L')
    
    def LPrime(self):
        self.front, self.top, self.back, self.bottom, self.right, self.left = self.moves.LPrime()
        self.testDistanceFromEndOfStatusBox('L\'')
    
    def U(self):
        self.front, self.top, self.back, self.bottom, self.right, self.left = self.moves.U()
        self.testDistanceFromEndOfStatusBox('U')
    
    def UPrime(self):
        self.front, self.top, self.back, self.bottom, self.right, self.left = self.moves.UPrime()
        self.testDistanceFromEndOfStatusBox('U\'')
    
    def F(self):
        self.front, self.top, self.back, self.bottom, self.right, self.left = self.moves.F()
        self.testDistanceFromEndOfStatusBox('F')
    
    def FPrime(self):
        self.front, self.top, self.back, self.bottom, self.right, self.left = self.moves.FPrime()
        self.testDistanceFromEndOfStatusBox('F\'')
    
    def B(self):
        self.front, self.top, self.back, self.bottom, self.right, self.left = self.moves.B()
        self.testDistanceFromEndOfStatusBox('B')
    
    def BPrime(self):
        self.front, self.top, self.back, self.bottom, self.right, self.left = self.moves.BPrime()
        self.testDistanceFromEndOfStatusBox('B\'')
    
    def D(self):
        self.front, self.top, self.back, self.bottom, self.right, self.left = self.moves.D()
        self.testDistanceFromEndOfStatusBox('D')
    
    def DPrime(self):
        self.front, self.top, self.back, self.bottom, self.right, self.left = self.moves.DPrime()
        self.testDistanceFromEndOfStatusBox('D\'')
