import random
import data.settings as constants

class Maze:
    """ """
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
        with open(self.filename) as map_file:

            for x, line in enumerate(map_file):
                for y, col in enumerate(line):
                    if col == constants.PATH_CHAR:
                        self.paths.add((x, y))
                    elif col == constants.START_CHAR:
                        self.start.add((x, y))
                        self.paths.add((x, y))
                    elif col == constants.GOAL_CHAR:
                        self.goal.add((x, y))
                        self.paths.add((x, y))
                    elif col == constants.WALL_CHAR:
                        self.walls.add((x, y))

    def put_items(self):
        """ put the items in the maze. """
        free_paths = self.paths.difference(self.start)
        free_paths = free_paths.difference(self.goal)
        items_object = set(random.sample(free_paths, 3))
        for item in items_object:
            self.items.add(item)
            print(item)

    def is_valid_cell(self, cell_pos):
        """ Return if a cell is valid or not. """     
        return cell_pos in self.paths

    def is_special_cell(self, cell_pos):
        """ Determine if a cell is special (will be modify without the print) """
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

def test_maze():
    maze = Maze(constants.FILENAME)

    #####    
    # Testing the organize of the cells
    #####
    # print('\n')
    # p1 = (-1,0)
    # p2 = (0, 0)
    # p3 = (5, 4)

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
    # print(f'The items are in this positions : {maze.items}\n')

    #####
    # testing if the cell is special or not
    #####
    # print('\n')
    # cell_pos1 = (0, 3)
    # cell_pos2 = (4, 9)
    # cell_pos3 = (11, 7)
    # cell_pos4 = (2, 9)

    # maze.is_special_cell(cell_pos1)
    # maze.is_special_cell(cell_pos2)    
    # maze.is_special_cell(cell_pos3)
    # maze.is_special_cell(cell_pos4)

    # #####
    # # testing the random item location generation
    # #####
    # print('\n')
    # print(f'Positions of the {len(maze.free_cells())} free paths  : {maze.free_cells()}\n')
    # print(len(maze.free_cells()))
    # print(maze.free_cells())



if __name__ == "__main__":
    test_maze()

