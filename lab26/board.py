class Board:
    def __init__(self, board, display_board):
        self.board = board
        self.display_board = display_board

    def board():
        board = [None, None, None, None, None, None, None, None, None]
        return board

    def display_board():
        print('''
        
        -------------------------------------------- Tic-Tac-Toe Game --------------------------------------------
        
        The rules are simple, chose a position where you'd like to make your mark using the diagram below, 
        alternate turns with your friend and the first to three in a row wins. X's or O's can match horizontally, 
        vertically, and diagonally.
        
            0 | 1 | 2
            3 | 4 | 5
            6 | 7 | 8
        
        Player with the 'X's goes first.
        
        Good Luck!
        ''')
