from maze import Maze
from draw_maze import MazeScreen

import settings as constants


class Main:
    """ """

    def __init__(self):
        """ Initialize the game. """
        # draw the maze
        self.m = Maze(constants.FILENAME)  
        self.ms = MazeScreen(self.m.paths, self.m.walls, self.m.start, self.m.goal, self.m.items)

    def run_game(self):
        """ """
        # attend un évènement clavier valide
        # mouvement de macgyver
        pass


if __name__ == "__main__":
    Main()
    pass
