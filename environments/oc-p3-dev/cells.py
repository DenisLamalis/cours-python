import settings as constants
from position import Position

class Cells:
    """ I'm the object who create the cell of the grid. """
    def __init__(self, filename):
        """ initialize the maze. """
        self.filename = filename
        self.cells = set()

        self.organize_the_maze()

    def organize_the_maze(self):
        """ Organize the cells of the maze. """
        with open(self.filename) as infile:
            for x, line in enumerate(infile):
                for y, col in enumerate(line):
                    if col == constants.PATH_CHAR:
                        self.cells.add((Position(x, y), 'path'))
                    elif col == constants.START_CHAR:
                        self.cells.add((Position(x, y), 'start'))
                    elif col == constants.GOAL_CHAR:
                        self.cells.add((Position(x, y), 'goal'))
                    elif col == constants.WALL_CHAR:
                        self.cells.add((Position(x, y), 'wall'))


#######################
# Tests & validations #
#######################

def test_cells():
    cells_in = Cells(constants.FILENAME)

    print(f'Total of cells for this maze: {constants.HEIGHT * constants.WIDTH}')
    print(f'Total of cells generate: {len(cells_in.cells)}')
    print(f'A random cell : {list(cells_in.cells)[0]}')
    print(f'A random cell position : {list(cells_in.cells)[0][0]}')
    print(f'A random cell type : {list(cells_in.cells)[0][1]}')


if __name__ == "__main__":
    test_cells()

