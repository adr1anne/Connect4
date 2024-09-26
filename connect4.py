#Adrianne Baik
#hw10pr2



def inarow_Neast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False            # Out-of-bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False            # O.o.b. column
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False            # Out-of-bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False            # O.o.b. column
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return True

class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # The string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-' + "\n"   # Bottom of the board

        for col in range(self.width):
            s += ' ' + str(col % 10)

        s += '\n'   
        return s    # The board is complete; return it

    def addMove(self, col, ox):
        H = self.height 
        for row in range(0,H):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
        self.data[H-1][col]=ox


    def clear(self):
        self.data = [[' ' for i in range(self.width)] for j in range(self.height)]
    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def allowsMove(self, c):
        if c in range(self.width):
            if self.data[0][c] == ' ':
                return True
        else:
            return False

    def isFull(self):
        H = self.height
        W = self.width
        D = self.data
        return all(D[0][col] != ' ' for col in range(W))

    def delMove(self, col):
        for x in range(self.height):
            if self.data[x][col] != ' ':
                self.data[x][col]=' '
                return
            
   
    def winsFor(self, ox):
        H = self.height
        W = self.width
        D = self.data

        # Check to see if ox wins, starting from any checker:
        for row in range(H):
            for col in range(W):
                if inarow_Neast(ox, row, col, D, 4) == True:
                    return True
                if inarow_Nsouth(ox, row, col, D, 4) == True:
                    return True
                if inarow_Nnortheast(ox, row, col, D, 4) == True:
                    return True
                if inarow_Nsoutheast(ox, row, col, D, 4) == True:
                    return True
                # you need three more, very similar, such checks
                # for the three other directions!

        # but, if it looks at EACH row and col and never finds a win...
        return False     # only gets here if it never returned True, above
     

    def hostGame(self):
        print()
        print('Welcome to Connect Four!')
        print(b)
        print()
        while True:
            X = -1
            while self.allowsMove(X) == False:
                user_string= input('Choose a column:')
                try:
                    X= int(user_string)
                except ValueError:
                    X = -1
            b.addMove(X,'x')
            print()
            print(b)
            print()
            if self.winsFor('x') == True:
                    print ('x wins')
                    break
        
            O = -1
            while self.allowsMove(O) == False:
                user_string= input('Choose a column:')
                try:
                     O= int(user_string)
                except ValueError:
                    O = -1
            b.addMove(O,'o')
            print()
            print(b)
            print()
            if self.winsFor('') == True:
                print ('O wins')
                break

            if self.isFull() == True:
                print('Tie')
                break






# This is the end of the Board class
# Below are some boards that will be re-created each time the file is run:

bigb = Board(15,5)
b = Board(7,6)

        