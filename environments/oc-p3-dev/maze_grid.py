import settings as constants
from cells import Cells

class MazeGrid:
    """ """
    def __init__(self, cells):
        """ """
        self.cells = cells

        self.display_grid(self.cells)

    def display_grid(self, cells):
        """ """
        print(cells.cells)





#######################
# Tests & validations #
#######################

def test_maze_grid():
    cells = Cells(constants.FILENAME)
    maze = MazeGrid(cells)





if __name__ == "__main__":
    test_maze_grid()