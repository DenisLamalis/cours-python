import pygame
import sys

import settings as constants
from cells import Cells
from skin import Skin

class MazeGrid:
    """ """
    def __init__(self, cells):
        """ """
        pygame.init()
        self.window = pygame.display.set_mode(constants.SET_MODE)
        
        self.cells = cells
        self.skin = Skin()

        self.display_maze(self.cells)
        self.draw_maze()

    def draw_maze(self):
        """ """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def display_maze(self, cells):
        """ """
        paths = list(cells.cells)
        i = 0
        for path in paths:
            pos = list(list(paths)[i])[0]
            typ = list(list(paths)[i])[1]
            if typ == 'wall':
                self.image = pygame.image.load(self.skin.image('wall')).convert()
            if typ == 'path':
                self.image = pygame.image.load(self.skin.image('path')).convert()
            if typ == 'start':
                self.image = pygame.image.load(self.skin.image('start')).convert()
            if typ == 'goal':
                self.image = pygame.image.load(self.skin.image('goal')).convert()
            pos_x = pos.y * 44
            pos_y = pos.x * 44
            self.window.blit(self.image, (pos_x, pos_y))
            i = i + 1
        pygame.display.flip()



#######################
# Tests & validations #
#######################

def test_maze_grid():
    cells = Cells(constants.FILENAME)
    maze = MazeGrid(cells)


if __name__ == "__main__":
    test_maze_grid()