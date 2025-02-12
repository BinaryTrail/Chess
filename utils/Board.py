#from Pieces import *

from Pieces.Pawn import Pawn
from Pieces.Rook import Rook
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Queen import Queen


from utils.Color import Color
from utils.Move import Move
from utils.Player import Player
import json

class Board:
    # Class constants
    BOARD_DIMENSIONS = 8
    def __init__(self):
        # Load Game config
        self.config = Board.loadConfig()
        # Initialise Player data
        self.player1 = self.player2 = None
        self.initPlayers()
        # Initialise Board
        self.board = self.initBoard()
        # Initialise a empty history
        self.move_history = []


    @staticmethod
    def loadConfig():
        # Fetch default config
        with open("./configs/default.json", encoding='utf-8') as json_file:
            # Convert json file to dictionary
            config = json.load(json_file)

        # Return dictionary
        return config

    # Need to implement picking black or white
    def initPlayers(self):
        # Get player 1 color
        player1_color = self.config["display"]["white-color"]
        player1_color_code = self.config["color"][player1_color]

        # Get player 2 color
        player2_color = self.config["display"]["black-color"]
        player2_color_code = self.config["color"][player2_color]

        # Change Player data
        self.player1 = Player("human", player1_color_code)
        self.player2 = Player("computer", player2_color_code)

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

    def displayBoard(self):
        # Initiate an empty display
        display = []

        # Build the board
        board_display = self.buildBoardDisplay()
        for row in board_display:
            display.append(row)

        # Build the mov history
        history_display = self.buildHistoryDisplay()
        for i in range(0, len(history_display)):
            display[i+1] += " " +  history_display[i]

        # Build the bench
        bench_display = self.buildBenchDisplay()
        display.append("")
        for row in bench_display:
            display.append(row)

        # Display the result
        return display

    def buildBoardDisplay(self):
        # Initialise an empty display
        board_display = []

        # Build Header
        board_display.append(f"  {self.buildBoardHeaderDisplay()}")

        # Build the body of the Board
        for i_row in range(0, len(self.board)):
            # Build game rows and seperator rows
            rows = self.buildBoardRowDisplay(i_row)

            # Add them to the display
            for row in rows:
                board_display.append(row)

        # Return completed board
        return board_display


    def buildBoardHeaderDisplay(self):
        # Initiate dictionary shortcuts
        colors = self.config["color"]
        board = self.config["display"]["board"]
        symbols = self.config["display"]["board"]["symbols"]

        # Fetch color pallet from config
        index_border_color_name = board["header-border-color"]
        index_color_name =  board["header-index-color"]

        # Build color shortcuts
        index_border_color = f"\033[{colors[index_border_color_name]}m"
        index_color =  f"\033[{colors[index_color_name]}m"
        reset_color =  f"\033[{colors["RESET"]}m"

        # Instantiate an empty header
        header = ""

        ################################################################################################################
        # Build the board header
        ################################################################################################################
        # Add left corner
        header += f"{index_border_color}{symbols["header-left"]}{reset_color}"

        # Build the header's body
        for i in range(0, len(Move.FORMAT.keys())):
            # Add the column letter identifier
            header += f" {index_color}{list(Move.FORMAT.keys())[i]}{reset_color}"

            # Add a seperator between letters
            if i < len(Move.FORMAT.keys()) -1:
                header += f" {index_border_color}{symbols["header-seperator"]}{reset_color}"
            # Add the right corner instead if the end is reached
            else:
                header += f" {index_border_color}{symbols["header-right"]}{reset_color}"

        ################################################################################################################
        # Board header build completed
        ################################################################################################################
        return header


    def buildBoardRowDisplay(self, i_row):
        # Initialise an empty row
        row_display = []

        # Initiate dictionary shortcuts
        colors = self.config["color"]
        board = self.config["display"]["board"]
        symbols = self.config["display"]["board"]["symbols"]

        # Fetch color pallet from config
        border_color_name = board["container-color"]
        grid_color_name = board["grid-color"]
        index_color_name =  board["header-index-color"]
        index_border_color_name = board["header-border-color"]

        # Build color shortcuts
        player1_color = f"\033[{self.player1.color_code}m"
        player2_color = f"\033[{self.player2.color_code}m"
        border_color = f"\033[{colors[border_color_name]}m"
        grid_color = f"\033[{colors[grid_color_name]}m"
        index_color = f"\033[{colors[index_color_name]}m"
        index_border_color = f"\033[{colors[index_border_color_name]}m"
        reset_color = f"\033[{colors["RESET"]}m"

        ################################################################################################################
        # Build top border of the board
        ################################################################################################################
        if i_row == 0:
            # Add the left index top corner
            row = f"{index_border_color}{symbols["sidebar-top"]}{symbols["sidebar-connector"]}{reset_color}"
            # Add the top left corner
            row += f"{border_color}{symbols["border-top-left"]}"

            # Build the middle
            for i in range(0, len(self.board[i_row])):
                # Add the borders on top of each cell
                row+= f"{symbols["border-top-disconnected"]}"*3

                # Add the last corner
                if i == len(self.board[i_row])-1:
                    row += f"{symbols["border-top-right"]}"
                # Add connections at the cell intersections
                else:
                    row += f"{symbols["border-top-connected"]}"

            # Add completed top border to display
            row_display.append(f"{row}{reset_color}")

        ################################################################################################################
        # Build populated rows
        ################################################################################################################
        # Add the sidebar identificators
        row = f"{index_color}{i_row +1}{reset_color} "
        # Add the left side border of the board
        row += f"{border_color}{symbols["border-left-disconnected"]}{reset_color}"
        # Go through the cells of the board
        for cell in self.board[i_row]:
            # Add an empty cell
            if cell is None:
                row += f" " * 3
            # Require white and black implementation and color codes
            elif cell in self.player1.placed_pieces:
                row += f"{player1_color} {cell.icon} {reset_color}"
            elif cell in self.player2.placed_pieces:
                row += f"{player2_color} {cell.icon} {reset_color}"
            else: # Error!
                pass

            # Add the other border at the end
            if cell == len(self.board[i_row]) - 1:
                row += f"{border_color}{symbols["border-right-disconnected"]}{reset_color}"
            # Add seperator in between cells of a row
            else:
                row += f"{grid_color}{symbols["grid-vertical"]}{reset_color}"
        # Remove the last grid seperator (and his color codes...)
        row = row[0:-(len(grid_color)+len(reset_color)+1)]
        # Add a border instead
        row += f"{border_color}{symbols["border-left-disconnected"]}{reset_color}"
        # Add the completed row to the display
        row_display.append(row)

        ################################################################################################################
        # Build the seperator or border under the row
        ################################################################################################################
        if i_row == 7:
            # Add the left index bottom border
            row = f"{index_border_color}{symbols["sidebar-bottom"]}{symbols["sidebar-connector"]}{reset_color}"
            # Add the top left corner
            row += f"{border_color}{symbols["border-bottom-left"]}"

            # Build the middle
            for i in range(0, len(self.board[i_row])):
                # Add the borders on top of each cell
                row += f"{symbols["border-bottom-disconnected"]}" * 3

                # Add the last corner
                if i == len(self.board[i_row]) - 1:
                    row += f"{symbols["border-bottom-right"]}"
                # Add connections at the cell intersections
                else:
                    row += f"{symbols["border-bottom-connected"]}"

            # Add completed top border to display
            row_display.append(f"{row}{reset_color}")

        # Build the seperator
        else:
            # Add the left index seperator
            row = f"{index_border_color}{symbols["sidebar-seperator"]}{reset_color} "
            # Add the left border
            row += f"{border_color}{symbols["border-left-connected"]}{reset_color}"

            # Start building grid
            row+= f"{grid_color}"
            # Build the middle
            for i in range(0, len(self.board[i_row])):
                # Add the grid-like separation between rows
                row += f"{symbols["grid-horizontal"]}" * 3

                # Add the other border at the end
                if i == len(self.board[i_row]) - 1:
                    # End of grid
                    row += f"{reset_color}"
                    # Build border
                    row += f"{border_color}{symbols["border-right-connected"]}{reset_color}"
                # Add connections at the cell intersections
                else:
                    row += f"{symbols["grid-intersection"]}"

            # Add completed top border to display
            row_display.append(row)

        ################################################################################################################
        # Row Build is completed
        ################################################################################################################
        return row_display


    def buildHistoryDisplay(self):
        # Create an empty display
        history_display = []

        # Build the header of the display
        header_display = self.buildHistoryHeader()
        for row in header_display:
            history_display.append(row)

        # build the rows for the display
        row_display = self.buildHistoryRowDisplay()
        for row in row_display:
            history_display.append(row)

        # return the completed display
        return history_display


    def buildHistoryHeader(self):
        # Display constants
        DISPLAY_WIDTH = 24
        COLUMN_WIDTH = [5, 4, 6, 4]
        COLUMN_NAMES = ["#Rd", "Pc", "From", "To"]

        # Declare return value
        display = []

        # Initiate dictionary shortcuts
        colors = self.config["color"]
        move_history = self.config["display"]["move-history"]
        symbols = self.config["display"]["move-history"]["symbols"]

        # Fetch color pallet from config
        title_color_name = move_history["title-color"]
        border_color_name = move_history["container-color"]
        grid_color_name = move_history["grid-color"]

        # Build color shortcuts
        title_color = f"\033[{colors[title_color_name]}m"
        border_color = f"\033[{colors[border_color_name]}m"
        grid_color = f"\033[{colors[grid_color_name]}m"
        reset_color = f"\033[{colors["RESET"]}m"

        ################################################################################################################
        # Build the Header of the Move History display
        ################################################################################################################
        # Build the top border
        row = f"{border_color}{symbols["border-top-left"]}"
        row += f"{symbols["border-top-disconnected"]}" * (DISPLAY_WIDTH - 2)
        row += f"{symbols["border-top-right"]}{reset_color}"
        display.append(row)

        # Build the Header content
        row = f"{border_color}{symbols["border-left-disconnected"]}{reset_color}"

        row+= " " *5
        row+= f"{title_color}Move History{reset_color}"
        row+= " " *5

        row += f"{border_color}{symbols["border-right-disconnected"]}{reset_color}"
        display.append(row)

        ################################################################################################################
        # Build the column seperator between rows and header
        ################################################################################################################
        # Add the left border
        row = f"{border_color}{symbols["border-left-connected"]}{reset_color}"

        # Build the column grid
        row += f"{grid_color}"
        for width in COLUMN_WIDTH:
            # Add Colum spacing
            row += f"{symbols["grid-horizontal"]}" *width
            # Add column connection
            row += f"{symbols["grid-intersection"]}"
        # Remove the extra connection
        row = row [0:-1]
        row += f"{reset_color}"

        # Add right border
        row += f"{border_color}{symbols["border-right-connected"]}{reset_color}"
        # Add row to display
        display.append(row)

        ################################################################################################################
        # Build the column names
        ################################################################################################################
        # Add the left border
        row = f"{border_color}{symbols["border-left-disconnected"]}{reset_color}"

        for i in range(0, len(COLUMN_NAMES)):
            # Add the Column name
            row += f"{title_color}"
            row += f" {COLUMN_NAMES[i]} "
            row += f"{reset_color}"

            # Add the column seperator
            if i != len(COLUMN_NAMES) - 1:
                row += f"{grid_color}{symbols["grid-vertical"]}{reset_color}"

        # Add the right border
        row += f"{border_color}{symbols["border-right-disconnected"]}{reset_color}"

        # Add the row to display
        display.append(row)

        ################################################################################################################
        # Build is complete
        ################################################################################################################
        return display


    def buildHistoryRowDisplay(self):
        # Display constants
        DISPLAY_WIDTH = 24
        COLUMN_WIDTH = [5, 4, 6, 4]
        COLUMN_NAMES = ["#Rd", "Pc", "From", "To"]

        # Declare return value
        display = []

        # Initiate dictionary shortcuts
        colors = self.config["color"]
        move_history = self.config["display"]["move-history"]
        symbols = self.config["display"]["move-history"]["symbols"]

        # Fetch color pallet from config
        title_color_name = move_history["title-color"]
        subtext_color_name = move_history["subtext-color"]
        border_color_name = move_history["container-color"]
        grid_color_name = move_history["grid-color"]

        # Build color shortcuts
        player1_color = f"\033[{self.player1.color_code}m"
        player2_color = f"\033[{self.player2.color_code}m"
        title_color =   f"\033[{colors[title_color_name]}m"
        subtext_color = f"\033[{colors[subtext_color_name]}m"
        border_color = f"\033[{colors[border_color_name]}m"
        grid_color = f"\033[{colors[grid_color_name]}m"
        reset_color = f"\033[{colors["RESET"]}m"

        ################################################################################################################
        # Build populated rows
        ################################################################################################################
        # Declare a counter for how many blank lines to add after
        blank_lines = 0
        for n_row in range(12, 0, -1):
            # Not enough moves were played to display this i'th move
            if n_row > len(self.move_history):
                blank_lines += 1

            # We Build the Row
            else:
                # Define observed move
                move = self.move_history[-n_row]
                # Collect history position
                temp_nrd =str(move.position)
                temp_nrd = (" " * (3-len(temp_nrd))) + temp_nrd
                col_nrd = f" {subtext_color}{temp_nrd}{reset_color} "
                # Collect piece icon data
                if move.piece_moved in self.player1.getAllPieces():
                    pc_color = player1_color
                else:
                    pc_color = player2_color
                col_pc = f"  {pc_color}{move.piece_moved.icon}{reset_color} "
                # Collect Position data
                col_from = f"  {subtext_color}{Move.formatMoveToString(move.old_pos)}{reset_color}  "
                col_to = f" {subtext_color}{Move.formatMoveToString(move.new_pos)}{reset_color} "

                # Add left border
                row = f"{border_color}{symbols["border-left-disconnected"]}{reset_color}"
                # Add grid row
                sep = f"{grid_color}{symbols["grid-vertical"]}{reset_color}"
                row+= f"{col_nrd}{sep}{col_pc}{sep}{col_from}{sep}{col_to}"
                # Add right border
                row+= f"{border_color}{symbols["border-right-disconnected"]}{reset_color}"

                # Add row to display
                display.append(row)

        ################################################################################################################
        # Build empty rows
        ################################################################################################################
        for i in range(0, blank_lines):
            # Add left border
            row = f"{border_color}{symbols["border-left-disconnected"]}{reset_color}"

            # Add blank row
            for j in range(0, len(COLUMN_WIDTH)):
                row += " "*COLUMN_WIDTH[j]
                if j != len(COLUMN_WIDTH) - 1:
                    row += f"{symbols["grid-vertical"]}"

            # Add right border
            row += f"{border_color}{symbols["border-right-disconnected"]}{reset_color}"
            # Add row to display
            display.append(row)

        ################################################################################################################
        # Build bottom border
        ################################################################################################################
        # Add left border
        row = f"{border_color}{symbols["border-bottom-left"]}{reset_color}"

        # Add Bottom border
        row+= f"{grid_color}"
        for i in range(0, len(COLUMN_WIDTH)):
            row+= f"{symbols["border-bottom-disconnected"]*COLUMN_WIDTH[i]}"
            if i != len(COLUMN_WIDTH)-1:
                row += f"{symbols["border-bottom-connected"]}"
        row+= f"{reset_color}"

        # Add right border
        row += f"{border_color}{symbols["border-bottom-right"]}{reset_color}"

        # Add row to display
        display.append(row)

        ################################################################################################################
        # History row build is completed
        ################################################################################################################
        return display


    def buildBenchDisplay(self):
        # Display constants
        DISPLAY_WIDTH = 60

        # Declare return value
        display = []

        # Initiate dictionary shortcuts
        colors = self.config["color"]
        bench = self.config["display"]["bench"]
        symbols = self.config["display"]["bench"]["symbols"]

        # Fetch color pallet from config
        title_color_name = bench["title-color"]
        border_color_name = bench["container-color"]
        grid_color_name = bench["grid-color"]

        # Build color shortcuts
        player1_color = f"\033[{self.player1.color_code}m"
        player2_color = f"\033[{self.player2.color_code}m"
        title_color = f"\033[{colors[title_color_name]}m"
        border_color = f"\033[{colors[border_color_name]}m"
        grid_color = f"\033[{colors[grid_color_name]}m"
        reset_color = f"\033[{colors["RESET"]}m"

        ################################################################################################################
        # Build top border
        ################################################################################################################
        row = f"{border_color}"
        row += f"{symbols["border-top-left"]}"
        row += f"{symbols["border-top-disconnected"]}" * (DISPLAY_WIDTH - 2)
        row += f"{symbols["border-top-right"]}"
        row += f"{reset_color}"
        # Add row to display
        display.append(row)

        ################################################################################################################
        # Build the Player 1 bench
        ################################################################################################################
        # Build player 1 bench header
        row = f"{border_color}{symbols["border-left-disconnected"]}{reset_color}"
        row += f"{title_color} Player 1's bench:{reset_color}"
        row += " " * (DISPLAY_WIDTH-20)
        row += f"{border_color}{symbols["border-right-disconnected"]}{reset_color}"
        # Add row to display
        display.append(row)

        # Build player 1 bench content
        # Add left border
        row = f"{border_color}{symbols["border-left-disconnected"]}{reset_color}"
        # Add player pieces
        row += f"{player1_color}"
        for piece in self.player1.benched_pieces:
            row += f" {piece.icon}"
        row += f"{reset_color}"
        # Add fill remains empty space
        row += " " * (DISPLAY_WIDTH - 2 - (len(self.player1.benched_pieces)*2))
        # Add right border
        row += f"{border_color}{symbols["border-right-disconnected"]}{reset_color}"
        # Add row to display
        display.append(row)

        ################################################################################################################
        # Build Bench seperator
        ################################################################################################################
        # Add left border
        row = f"{border_color}{symbols["border-left-connected"]}{reset_color}"
        # Build grid
        row += f"{grid_color}{symbols["grid-horizontal"] * (DISPLAY_WIDTH-2)}{reset_color}"
        # Add right border
        row += f"{border_color}{symbols["border-right-connected"]}{reset_color}"

        # Add row to display
        display.append(row)

        ################################################################################################################
        # Build the Player 2 bench
        ################################################################################################################
        # Build player 1 bench header
        row = f"{border_color}{symbols["border-left-disconnected"]}{reset_color}"
        row += f"{title_color} Player 2's bench:{reset_color}"
        row += " " * (DISPLAY_WIDTH - 20)
        row += f"{border_color}{symbols["border-right-disconnected"]}{reset_color}"
        # Add row to display
        display.append(row)

        # Build player 1 bench content
        # Add left border
        row = f"{border_color}{symbols["border-left-disconnected"]}{reset_color}"
        # Add player pieces
        row += f"{player2_color}"
        for piece in self.player2.benched_pieces:
            row += f" {piece.icon}"
        row += f"{reset_color}"
        # Add fill remains empty space
        row += " " * (DISPLAY_WIDTH - 2 - (len(self.player2.benched_pieces) * 2))
        # Add right border
        row += f"{border_color}{symbols["border-right-disconnected"]}{reset_color}"
        # Add row to display
        display.append(row)

        ################################################################################################################
        # Build bottom border
        ################################################################################################################
        row = f"{border_color}"
        row += f"{symbols["border-bottom-left"]}"
        row += f"{symbols["border-top-disconnected"]}" * (DISPLAY_WIDTH - 2)
        row += f"{symbols["border-bottom-right"]}"
        row += f"{reset_color}"
        # Add row to display
        display.append(row)

        ################################################################################################################
        # Bench build is completed
        ################################################################################################################
        return display

