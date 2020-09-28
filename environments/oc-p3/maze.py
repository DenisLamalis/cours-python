import random

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
        self.item1 = set()
        self.item2 = set()
        self.item3 = set()
        self.player = set()

        self.organize_the_maze()
        self.put_items()

    @property
    def start_pos(self):
        return list(self.start)[0]    
    
    @property
    def item1_pos(self):
        return list(self.item1)[0]
    
    @property
    def item2_pos(self):
        return list(self.item2)[0]

    @property
    def item3_pos(self):
        return list(self.item3)[0]
    

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
                        self.player.add(Position(x, y))
                    elif col == constants.GOAL_CHAR:
                        self.goal.add(Position(x, y))
                        self.paths.add(Position(x, y))
                    elif col == constants.WALL_CHAR:
                        self.walls.add(Position(x, y))

    def put_items(self):
        """ put the items in the maze. """
        free_paths = self.paths.difference(self.start)
        free_paths = free_paths.difference(self.goal)
        items_object = set(random.sample(free_paths, 3))
        self.item1.add(list(items_object)[0])
        self.item2.add(list(items_object)[1])
        self.item3.add(list(items_object)[2])

    def is_valid_cell(self, position):
        """ Return if a cell is valid or not. """     
        return position in self.paths

    def is_special_cell(self, cell_pos):
        """ Determine if a cell is special (will be modify without the print) """
        if cell_pos in self.start:
            return False
        elif cell_pos in self.goal:
            return 'goal'
        elif cell_pos in self.item1:
            return 'item1'
        elif cell_pos in self.item2:
            return 'item2'
        elif cell_pos in self.item3:
            return 'item3'
        else:
            return False   


#######################
# Tests & validations #
#######################

def test_maze():
    maze = Maze(constants.FILENAME)

    # print('\n')
    # #####    
    # # Testing the organize of the cells
    # #####
    # p1 = Position(-1,0)
    # p2 = Position(0, 0).right()
    # p3 = Position(5, 5).right()

    # print(f'Is the cell in position {p1} valide ? {maze.is_valid_cell(p1)}')    
    # print(f'Is the cell in position {p2} valide ? {maze.is_valid_cell(p2)}')
    # print(f'Is the cell in position {p3} valide ? {maze.is_valid_cell(p3)}')

    # print('\n')
    #####
    # Testing that there are all the cells and all the coordinates
    #####  
    # print(f'Total of cells : {len(maze.paths) + len(maze.walls)}\n') 
    # print(f'Positions of the {len(maze.paths)} paths  : {maze.paths}\n')
    # print(f'Positions of the {len(maze.walls)} walls : {maze.walls}\n')

    # print(f'The start is in this positions : {maze.start}\n')
    # print(f'The goal is in this positions : {maze.goal}\n') 
    # print(f'The item1 are in this positions : {maze.item1}\n')
    # print(f'The item2 are in this positions : {maze.item2}\n')
    # print(f'The item3 are in this positions : {maze.item3}\n')

    # print('\n')
    #####
    # testing if the cell is special or not
    #####
    # cell_pos1 = Position(0, 3)
    # cell_pos2 = Position(4, 9)
    # cell_pos3 = Position(11, 7)
    # cell_pos4 = Position(2, 9)

    # maze.is_special_cell(cell_pos1)
    # maze.is_special_cell(cell_pos2)    
    # maze.is_special_cell(cell_pos3)
    # maze.is_special_cell(cell_pos4)

    # print('\n')
    # #####
    # # testing the random item location generation
    # #####
    # # print(f'Positions of the {len(maze.free_cells())} free paths  : {maze.free_cells()}\n')
    # # print(len(maze.free_cells()))
    # # print(maze.free_cells())



if __name__ == "__main__":
    test_maze()

