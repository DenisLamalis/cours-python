
import settings as constants

class Map:

    def __init__(self, filename):
        self.filename = filename

        self.paths = set()
        self.walls = set()
        self.start = set()
        self.goal = set()
        self.items = set()

    def load_from_file(self):

        with open(self.filename) as infile:
            for x, line in enumerate(infile):
                for y, col in enumerate(line):
                    if col == constants.PATH_CHAR:
                        self.paths.add(Position(x, y))
                    elif col == constants.START_CHAR:
                        self.start.add(Position(x, y))
                        self.paths.add(Position(x, y))
                    elif col == constants.GOAL_CHAR:
                        self.goal.add(Position(x, y))
                        self.paths.add(Position(x, y))
                    elif col == constants.WALLS_CHAR:
                        self.walls.add(Position(x, y))


