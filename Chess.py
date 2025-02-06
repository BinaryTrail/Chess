from utils.Board import Board


class Chess:
    def __init__(self):
        # Initialisation of class attributes
        self.board = []#Board()        # The Game board


    def play(self):
        board = Board()

        display = board.buildBoardDisplay()
        for row in display:
            print(row)

        return None