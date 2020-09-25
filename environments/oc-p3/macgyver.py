from maze import Maze
from position import Position
import settings as constants

class MacGyver:
    """ """
    def __init__(self, maze):
        """ Initialize position and bag. """
        self.maze = maze
        self.mg_pos = self.maze.start_pos
        self.bag = ''
        self.paths = maze.paths

        self.move('d')
        self.move('s')
        self.move('s')
        self.move('s')
        self.move('d')
        self.move('s')
        self.move('z')
        self.move('z')
        self.move('z')



 
    def move(self, direction):
        if direction == 'z':
            if Position.up(self.mg_pos) in self.paths:
                self.mg_pos = Position.up(self.mg_pos)
                print(f'La case est valide, nouvelle position de MacGyver : {self.mg_pos}')
        if direction == 's':
            if Position.down(self.mg_pos) in self.paths:
                self.mg_pos = Position.down(self.mg_pos)
                print(f'La case est valide, nouvelle position de MacGyver : {self.mg_pos}')
        if direction == 'd':
            if Position.right(self.mg_pos) in self.paths:
                self.mg_pos = Position.right(self.mg_pos)
                print(f'La case est valide, nouvelle position de MacGyver : {self.mg_pos}')
        if direction == 'q':
            if Position.left(self.mg_pos) in self.paths:
                self.mg_pos = Position.left(self.mg_pos)
                print(f'La case est valide, nouvelle position de MacGyver : {self.mg_pos}')

    def in_bag(self):
        """ """
        pass


if __name__ == '__main__':
    
    instance_maze = Maze(constants.FILENAME) 
    instance_macgyver = MacGyver(instance_maze)
