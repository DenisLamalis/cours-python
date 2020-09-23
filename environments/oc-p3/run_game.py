import sys
import pygame

from print_maze import PrintMaze

class MacGyver:
    """ """
    def __init__(self):
        """ """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Help MacGyver to escape")
        self.cell = PrintMaze(self)

    def run_game(self):
        """ """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.cell.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    mg = MacGyver()
    mg.run_game()
