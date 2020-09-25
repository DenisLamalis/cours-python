
from maze import Maze
from draw_maze import MazeScreen
from macgyver import MacGyver
from position import Position

import settings as constants

class Main:
    """ Game management. """
    
    def __init__(self):
        """ Initialize the game. """
        pygame.init()

        self.m = Maze(constants.FILENAME)  
        self.mg = MacGyver(self.m)

        # display the maze with pygame
        MazeScreen(self.m.paths, self.m.walls, self.m.start, self.m.goal, self.m.items)

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            self.check_events()
            # self.check_special(cell_pos)
    
    def check_events(self):
        """ respond to keypresses. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """ respond to keypresses """

        if event.key == pygame.K_RIGHT:
            # move MacGyver to the right
            self.mg.move('RIGHT')
        elif event.key == pygame.K_LEFT:
            self.mg.move('LEFT')
        elif event.key == pygame.K_DOWN:
            self.mg.move('DOWN')
        elif event.key == pygame.K_UP:
            self.mg.move('UP')
        elif event.key == pygame.K_q:
            sys.exit()

    # def check_special(self, cell_pos):
        # if cell == item
        # if cell == goal
        # pass


if __name__ == "__main__":
    hmg = Main()
    hmg.run_game()
