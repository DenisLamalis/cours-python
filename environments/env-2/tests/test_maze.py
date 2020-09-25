
from .. maze import Maze

#######################
# Tests & validations #
#######################

def test_maze():
    maze = Maze(constants.FILENAME)

    #####    
    # Testing the organize of the cells
    #####
    print('\n')
    p1 = (-1,0)
    p2 = (0, 0)
    p3 = (5, 4)

    print(f'Is the cell in position {p1} valide ? {maze.is_valid_cell(p1)}')    
    print(f'Is the cell in position {p2} valide ? {maze.is_valid_cell(p2)}')
    print(f'Is the cell in position {p3} valide ? {maze.is_valid_cell(p3)}')

    #####
    # Testing that there are all the cells and all the coordinates
    ##### 
    print('\n') 
    print(f'Total of cells : {len(maze.paths) + len(maze.walls)}\n') 
    print(f'Positions of the {len(maze.paths)} paths  : {maze.paths}\n')
    print(f'Positions of the {len(maze.walls)} walls : {maze.walls}\n')

    print(f'The start is in this positions : {maze.start}\n')
    print(f'The goal is in this positions : {maze.goal}\n') 
    print(f'The items are in this positions : {maze.items}\n')

    #####
    # testing if the cell is special or not
    #####
    print('\n')
    cell_pos1 = (0, 3)
    cell_pos2 = (4, 9)
    cell_pos3 = (11, 7)
    cell_pos4 = (2, 9)

    maze.is_special_cell(cell_pos1)
    maze.is_special_cell(cell_pos2)    
    maze.is_special_cell(cell_pos3)
    maze.is_special_cell(cell_pos4)

    # #####
    # # testing the random item location generation
    # #####
    print('\n')
    print(f'Positions of the {len(maze.free_cells())} free paths  : {maze.free_cells()}\n')
    print(len(maze.free_cells()))
    print(maze.free_cells())



if __name__ == "__main__":
    test_maze()

