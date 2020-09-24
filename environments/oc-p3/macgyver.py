from maze import Maze
import settings as constants

class MacGyver:
    """ """
    def __init__(self, position):
        self.mg_pos = position
 
    def move(self):
        """ """
        print(self.mg_pos)


if __name__ == '__main__':
    
    instance_maze = Maze(constants.FILENAME) 
    print(instance_maze.start) 
    instance_macgyver = MacGyver(instance_maze.start)
