import pygame
import sys

class MazeScreen:
    """ """
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((660, 660))

        self.image()

    def draw_maze(self):
        """ """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def image(self):
        self.image = pygame.image.load('floor.bmp').convert()
        self.window.blit(self.image, (40, 40))
        pygame.display.flip()

if __name__ == '__main__':
    ms = MazeScreen()
    ms.draw_maze()