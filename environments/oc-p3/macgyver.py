from maze import Maze
import settings as constants

class MacGyver:
    """ """
    def __init__(self, maze):
        """ Initialize position and bag. """
        self.maze = maze
        self.mg_position = self.maze.start_pos
        print(self.mg_position)
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
    instance_macgyver = MacGyver(instance_maze)
