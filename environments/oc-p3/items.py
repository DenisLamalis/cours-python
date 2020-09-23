from position import Position

class Items:

    def __init__(self):
        self.items = set()

        self.choose_position()

    def choose_position2(self):
        """ I choose 3 positions for items. (will be modify with random position) """
        self.items.add(Position(13, 4))
        self.items.add(Position(12, 12))
        self.items.add(Position(8, 8))

# choisir 3 positions dans (les positions valides - start - goal)

        def choose_position(self):
        """ I choose 3 positions for items. (will be modify with random position) """
        self.items.add(Position(13, 4))
        self.items.add(Position(12, 12))
        self.items.add(Position(8, 8))