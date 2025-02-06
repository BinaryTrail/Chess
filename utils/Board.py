from Pieces.Pawn import Pawn
from Pieces.Rook import Rook
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Queen import Queen

from utils.Color import Color
from utils.Player import Player


class Board:
    def __init__(self):
        # Constante de classe
        self.RESET_COLOR = Color().RESET

        # Initialisation of class attributes
        self.player1 = Player("human", Color().WHITE)
        self.player2 = Player("computer", Color().DARK_GRAY)
        self.board = self.initBoard()               # Populate board and allocate pieces to players
        self.move_history = []                      # history of all played moves

    def initBoard(self):
        # Declare board as an empty 8x8 grid
        board = []
        for i in range(0, 8):
            row = [None] * 8
            board.append(row)

        # Create and insert the pawns
        for i in range(0,8):
            # Instantiate the Pawns
            white_pawn = Pawn("white", (6, i))
            black_pawn = Pawn("black", (1, i))
            # Place the Pawns on the board
            board[6][i] = white_pawn
            board[1][i] = black_pawn
            # Add pieces to player collection
            self.player1.addPiece(white_pawn)
            self.player2.addPiece(black_pawn)

        # Create and insert the Rooks
        for i in [0, 7]:
            # Instantiate the Rooks
            white_rook = Rook("white", (7, i))
            black_rook = Rook("black", (0, i))
            # Insert the Rooks in the board
            board[7][i] = white_rook
            board[0][i] = black_rook
            # Add pieces to player collection
            self.player1.addPiece(white_rook)
            self.player2.addPiece(black_rook)

        # Create and insert the Knights
        for i in [1,6]:
            # Instantiate the Knights
            white_knight = Knight("white", (7, i))
            black_knight = Knight("black", (0, i))
            # Insert the Knights in the board
            board[7][i] = white_knight
            board[0][i] = black_knight
            # Add pieces to player collection
            self.player1.addPiece(white_knight)
            self.player2.addPiece(black_knight)

        # Create and insert the Bishops
        for i in [2, 5]:
            # Instantiate the Bishops
            white_bishop = Bishop("white", (7, i))
            black_bishop = Bishop("black", (0, i))
            # Insert the Bishops in the board
            board[7][i] = white_bishop
            board[0][i] = black_bishop
            # Add pieces to player collection
            self.player1.addPiece(white_bishop)
            self.player2.addPiece(black_bishop)

        # Instantiate the Kings
        white_king = King("white", (7,4))
        black_king = King("black", (0,4))
        # Insert the Kings in the board
        board[7][4] = white_king
        board[0][4] = black_king
        # Add pieces to player collection
        self.player1.addPiece(white_king)
        self.player2.addPiece(black_king)

        # Instantiate the Queens
        white_queen = Queen("white", (7,3))
        black_queen = Queen("black", (0,3))
        # Insert the Queens in the board
        board[7][3] = white_queen
        board[0][3] = black_queen
        # Add pieces to player collection
        self.player1.addPiece(white_queen)
        self.player2.addPiece(black_queen)

        # End of initialisation
        return board


    def buildBoardDisplay(self):
        color = Color()

        display = []
        header = "  ╭ A ─ B ─ C ─ D ─ E ─ D ─ F ─ G ╮"
        display.append(header)

        for i in range(0,8):
            # Add a row seperator
            if i == 0:  # Top of the board
                display.append("╭─╔═══════════════════════════════╗")
            else:       # Row seperator
                display.append("│ ╟───┼───┼───┼───┼───┼───┼───┼───╢")

            # Add row
            row = ""
            # Build the Row cell by cell
            for j in range(0, len(self.board[i])):
                # Build the Front of the cell
                if j == 0:
                    row += f"{str(i+1)} ║ "
                else:

                    row += "│ "

                # Build the content of the cell ! s(Verify team and assign a specific color) !
                if self.board[i][j] is not None:
                    # Add an occupied cell
                    if self.board[i][j] in self.player1.placed_pieces:
                        row += f"{self.player1.player_color}{self.board[i][j].icon}{self.RESET_COLOR}"
                    elif self.board[i][j] in self.player2.placed_pieces:
                        row += f"{self.player2.player_color}{self.board[i][j].icon}{self.RESET_COLOR}"
                    else:
                        pass # Error! - Implement exception?

                    row += " "
                else:
                    # Add an empty cell
                    row += "  "

                # Build the end of the row
                if j == len(self.board[i])-1:
                    # Add the border of the grid
                    row += "║"
            # Add row to display
            display.append(row)

            # Add the bottom of the board
            if i == 7:
                display.append("╰─╚═══════════════════════════════╝")

        return display

    def buildHistoryDisplay(self):
        pass

    def buildBenchDisplay(self):
        pass

    def displayBoard(self):

        board = self.buildBoardDisplay()
        move_history = self.buildHistoryDisplay()
        bench = self.buildBenchDisplay()


        return None