from Pieces.Piece import Piece


class Knight(Piece):
    def __init__(self, team, pos):
        super().__init__(team, pos)
        self.icon = "♘"

    def getPossibleMoves(self):
        pass
