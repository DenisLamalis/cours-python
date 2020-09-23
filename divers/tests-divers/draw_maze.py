import pygame
import sys

class MazeScreen:
    """ """
    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode((660, 660))

    def draw_maze(self):
        """ """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


if __name__ == '__main__':
    ms = MazeScreen()
    ms.draw_maze()