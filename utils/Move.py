class Move:
    FORMAT = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    def __init__(self, n, old_pos, new_pos, moved_piece, eaten_piece = None):
        self.position = n               # The move history position
        self.old_pos = old_pos          # The old position of the moved piece
        self.new_pos = new_pos          # The new position of the moved piece
        self.piece_moved = moved_piece  # The piece that was moved
        self.piece_eaten = eaten_piece  # The piece that was eaten, None if none were eaten

    @staticmethod
    def formatMoveToString(pos):
        # Get x and y values from args
        pos_y = pos[0]
        pos_x = pos[1]

        # Format y value
        pos_y = str(pos_y +1)
        # Error! value should be in [0,7]
        if int(pos_y) > 7 or int(pos_y) < 0:
            return -1

        # Format x value
        for (key, val) in Move.FORMAT.items():
            if val == pos_x:
                pos_x = key
                break
        # Error! value should be in [A,H]
        if type(pos_x) is not str:
            return -1

        # Return format (y, x) -> X0 == xy
        return f"{pos_x}{pos_y}"

    @staticmethod
    def formatMoveToPos(pos):
        # Get x and y values from args
        pos_y = pos[1]
        pos_x = pos[0]

        # Format y value
        pos_y = int( pos_y ) -1
        # Format x value
        pos_x = int( Move.FORMAT[ pos_x ] )

        # Create returnable tuple value
        pos = (pos_y, pos_x)

        # Return format X0 == xy -> (y, x)
        return pos
