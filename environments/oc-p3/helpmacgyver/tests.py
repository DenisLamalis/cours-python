
#######################
# Tests & validations #
#######################

def test_maze():
    settings = Settings()
    maze = Maze(settings.FILENAME)

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