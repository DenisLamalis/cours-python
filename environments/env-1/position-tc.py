
class Position:
    """ Calculate the position """

    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)

    def __hash__(self):
        return hash(self.position)

    def up(self):
        return Position(x-1, y)

    def down(self):
        return Position(x+1, y)

    def right(self):
        return Position(x, y+1)

    def left(self):
        return Position(x, y-1)