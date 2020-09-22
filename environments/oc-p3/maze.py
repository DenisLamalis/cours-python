import settings as constants
from position import Position
from items import Items

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
        items_object = Items()
        for item in items_object.items:
            self.items.add(item)

    def is_valid_cell(self, position):
        """ Return if the cell is valid or not. """     
        return position in self.paths

    def is_special_cell(self, cell_pos):
        """ Determine if the cell is special """
        if cell_pos in self.start:
            print('it is the start')
        elif cell_pos in self.goal:
            print('it is the goal')
        elif cell_pos in self.items:
            print('there are a item')
        else:
            print('nothing special')


#######################
# Tests & validations #
#######################

def main():
    maze = Maze(constants.FILENAME)

    # print('\n')
    # #####    
    # # test de l'état de cellules
    # #####
    # p1 = Position(-1,0)
    # p2 = Position(0, 0).right()
    # p3 = Position(5, 5).right()

    # print(f'Is the cell in position {p1} valide ? {maze.is_valid_cell(p1)}')    
    # print(f'Is the cell in position {p2} valide ? {maze.is_valid_cell(p2)}')
    # print(f'Is the cell in position {p3} valide ? {maze.is_valid_cell(p3)}')

    # print('\n')
    # #####
    # # I validate that there are all the cells and all the coordinates
    # #####  
    # print(f'Total of cells : {len(maze.paths) + len(maze.walls)}\n')
    
    # print(f'Positions of the {len(maze.paths)} paths  : {maze.paths}\n')
    # print(f'Positions of the {len(maze.walls)} walls : {maze.walls}\n')

    # print(f'The start is in this positions : {maze.start}\n')
    # print(f'The goal is in this positions : {maze.goal}\n') 
    # print(f'The items are in this positions : {maze.items}\n')

    print('\n')
    #####
    # testing if the cell is special or not
    #####
    cell_pos1 = Position(0, 3)
    cell_pos2 = Position(4, 9)
    cell_pos3 = Position(8, 8)

    maze.is_special_cell(cell_pos1)
    maze.is_special_cell(cell_pos2)    
    maze.is_special_cell(cell_pos3)

if __name__ == "__main__":
    main()

