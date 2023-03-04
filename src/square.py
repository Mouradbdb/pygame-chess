


class Square :
    def __init__(self,row,col , piece = None):
        self.row = row
        self.piece = piece
        self.col = col
    def has_piece(self):
        return self.piece !=None