from position import Position

class Items:

    def __init__(self):
        self.items = set()

        self.choose_position()

    def choose_position(self):
        self.items.add(Position(13, 4))
        self.items.add(Position(12, 12))
        self.items.add(Position(8, 8))

