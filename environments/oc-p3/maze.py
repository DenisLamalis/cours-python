import settings as constants
from position import Position

class Maze:

    def __init__(self, filename):
        """ initialize the maze """

        self.filename = filename
        self.paths = set()
        self.walls = set()
        self.start = set()
        self.goal = set()
        self.items = set()

    def organize_the_maze(self):
        """ Organize the cells of the maze """

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
                    elif col == constants.WALL_CHAR:
                        self.walls.add(Position(x, y))


# Tests #
#########

def main():
    map = Maze('map-1.txt')

    p1 = Position(-1,0)
    # print(map.is_valid_path(p1))
    print(p1 in map)

    p2 = Position(0, 0).right()
    # print(map.is_valid_path(p2))
    print(p2 in map)

    p3 = Position(5, 5).right()
    # print(map.is_valid_path(p3))
    print(p3 in map)

    print(map.start)


if __name__ == "__main__":
    main()



###########################

#    def open_file(self):
#         current_map = []
        
#         map_file = open(self.filename,'r')
#         for line in map_file:
#             current_map.append(line.strip())
#         map_file.close()

#         print('Map : ',current_map)

# ma_map = Maze('map-1.txt')

# print(ma_map.open_file())

    # def find_cell_attribute(self, x, y):
    #     return current_map[x-1][y-1]