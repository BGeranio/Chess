class board:
    def __init__(self, gameState, turn):
        self.board = [[None]*8 for i in range(8)]
        self.gameState = gameState
        self.turn = turn

    def printBoard(self):
        alph = ['a','b','c','d','e','f','g','h']
        str=''
        str+='- 1 2 3 4 5 6 7 8'
        for i in range(8):
            str+='\n'
            str+= alph[i] + ' '
            for j in range(8):
                str+=self.board[i][j].getPiece()
                str+=' '
        str+='\n- - - - - - - -'
        return str
       
    
    def makeBoard(self):
        WPieceRow = ['rook','knight','bishop','queen','King', 'bishop','knight','rook']
        BPieceRow = ['rook','knight','bishop','King','queen', 'bishop','knight','rook']
        for i in range(8):
            for j in range(8):
                self.board[i][j] = cell('*', 'none', i, j)
                if i == 0:
                    self.board[i][j].setPiece(BPieceRow[j], 'black', i, j)
                elif i == 1: 
                    self.board[i][j].setPiece('pawn', 'black', i, j)
                elif i == 6:
                    self.board[i][j].setPiece('pawn', 'white', i, j)
                elif i == 7:
                    self.board[i][j].setPiece(WPieceRow[j], 'white', i, j)

    def setGameState(self, state):
        self.gameState = state

    def getTurn(self):
        return self.turn

    def gameWon(self):
        if self.gameState == 'win':
            return True
        return False

    def getBoard(self):
        return self.board

    def handleMoves(self, board, start, end):
        alphabet = ['a','b','c','d','e','f','g','h']
        beg1, end1 = 0, 0
        for i in range(len(alphabet)):
            if start[0] == alphabet[i]:
                beg1 = i
                break

        for i in range(len(alphabet)):
            if end[0] == alphabet[i]:
                end1 = i
                break
        print(beg1, int(start[1]), end1, int(end[1]))
        beginning = [beg1, int(start[1])]
        end = [end1, int(end[1])]
        for i in range(8):
            for j in range(8):
                if beginning == board.getBoard()[i][j].getPos():
                    checkMoves = board.getBoard()[i][j].checkMoves(board.getBoard())
                    for i in range(len(checkMoves)):
                        if checkMoves[i] == end:
                            temp0, temp1 = board.getBoard()[beginning[0]][beginning[1]].getWholePiece()
                            board.getBoard()[beginning[0]][beginning[1]].clear()
                            board.getBoard()[end[0]][end[1]].setPieceOnly(temp0, temp1)
                            print(board.printBoard())

class cell:
    def __init__(self, piece, color, row, col):
        self.piece = piece
        self.color = color
        self.row = row
        self.col = col
        
    def setPiece(self, piece, color, row, col):
        self.piece = piece
        self.color = color
        self.row = row
        self.col = col
    
    def getPiece(self):
        return str(self.piece[0])
    
    def getWholePiece(self):
        return self.piece, self.color

    def setPieceOnly(self, piece, color):
        self.piece = piece
        self.color = color
    
    def getColor(self):
        return self.color
    
    def getPos(self):
        return [self.row, self.col]

    def checkMoves(self, board):
        print(self.piece, self.color)
        moves = []
        if self.piece == 'pawn':
            if self.color == 'white':
                moves.append([self.row - 1, self.col])   

            if self.color == 'black':   
                moves.append([self.row + 1, self.col])


        return moves 
    
    def clear(self):
        self.piece = '*'
        self.color = 'none'

    
"""
newBoard = board('begin', 'white')

newBoard.makeBoard()

print(newBoard.printBoard())
"""

