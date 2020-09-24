from maze import Maze
import settings as constants

class MacGyver:
    """ """
    def __init__(self, position):
        """ Initialize position and bag. """
        self.mg_pos = position
        self.bag = ''
 
    def move(self):
        """ """
        #
        pass

    def in_bag(self):
        """ """
        pass


if __name__ == '__main__':
    
    instance_maze = Maze(constants.FILENAME) 
    instance_macgyver = MacGyver(instance_maze.start)
