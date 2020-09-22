import settings as constants
from position import Position

class Maze:

    def __init__(self, filename):
        """ initialize the maze. """
        self.filename = filename
        self.paths = set()
        self.walls = set()
        self.start = set()
        self.goal = set()
        self.items = set()

        self.organize_the_maze()
        self.put_items()

    def is_valid_cell(self, position):
        """ Return if the cell is valid or not. """     
        return position in self.paths

    def organize_the_maze(self):
        """ Organize the cells of the maze. """
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

    def put_items(self):
        """ put the items in the maze. """
        for item in constants.ITEMS:
            self.items.add(item)

    def is_special_cell(self, position):
        """ Determine if the cell is special """
        # est-ce que la case est dans start, goal ou items
        print(f'position envoyee {position}')
        print(self.start)
        if {(0,3)} == self.start:
            print('it is the start')
        # elif position in self.goal:
        #     print('it is the goal')
        # elif position in self.items:
        #     print('there are a item')
        else:
            print('nothing special')


#######################
# Tests & validations #
#######################

def main():
    maze = Maze(constants.FILENAME)

    # print('\n')    
    # # test de l'état de cellules
    # p1 = Position(-1,0)
    # p2 = Position(0, 0).right()
    # p3 = Position(5, 5).right()

    # print(f'Is the cell in position {p1} valide ? {maze.is_valid_cell(p1)}')    
    # print(f'Is the cell in position {p2} valide ? {maze.is_valid_cell(p2)}')
    # print(f'Is the cell in position {p3} valide ? {maze.is_valid_cell(p3)}')

    # print('\n')
    # # I validate that there are all the celles and all the coordinates  
    # print(f'Total of cells : {len(maze.paths) + len(maze.walls)}\n')
    
    # print(f'Positions of the {len(maze.paths)} paths  : {maze.paths}\n')
    # print(f'Positions of the {len(maze.walls)} walls : {maze.walls}\n')

    # print(f'The start is in this positions : {maze.start}\n')
    # print(f'The goal is in this positions : {maze.goal}\n') 
    # print(f'The items are in this positions : {maze.items}\n')

    print('\n')
    # testing if the cell is special or not
    maze.is_special_cell({(0,3)})

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