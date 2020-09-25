import random
from ..data.settings import Constants

class Maze:
    """ """
    def __init__(self, filename):
        """ initialize the maze. """
        self.constants = Constants()
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
                    if col == self.constants.PATH_CHAR:
                        self.paths.add((x, y))
                    elif col == self.constants.START_CHAR:
                        self.start.add((x, y))
                        self.paths.add((x, y))
                    elif col == self.constants.GOAL_CHAR:
                        self.goal.add((x, y))
                        self.paths.add((x, y))
                    elif col == self.constants.WALL_CHAR:
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
