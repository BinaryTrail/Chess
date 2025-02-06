class Move:
    def __init__(self, n, old_pos, new_pos, moved_piece, eaten_piece = None):
        self.position = n               # The move history position
        self.old_pos = old_pos          # The old position of the moved piece
        self.new_pos = new_pos          # The new position of the moved piece
        self.piece_moved = moved_piece  # The piece that was moved
        self.piece_eaten = eaten_piece  # The piece that was eaten, None if none were eaten
