class Player:
    def __init__(self, player_type, player_color):
        self.player_type = player_type
        self.player_color = player_color
        self.benched_pieces = []
        self.placed_pieces = []

    def getAllPieces(self):
        # Initialisation of the return value
        collection = []

        # Add all pieces currently on the board
        for placed_piece in self.placed_pieces:
            collection.append(placed_piece)
        # Add all pieces currently benched
        for benched_piece in self.benched_pieces:
            collection.append(benched_piece)

        # Return all pieces of the player
        return collection

    def addPiece(self, piece):
        self.placed_pieces.append(piece)