import pygame
import sys

from maze import Maze
import settings as constants

class MazeScreen:
    """ """
    def __init__(self, paths, walls, start, goal, items):
        pygame.init()
        self.window = pygame.display.set_mode((660, 660))
        self.paths = paths
        self.walls = walls
        self.start = start
        self.goal = goal
        self.items = items

        self.screen_paths()
        self.screen_walls()
        self.screen_start()
        self.screen_goal()

    def draw_maze(self):
        """ """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def screen_paths(self):
        """ """
        a_paths = {(4, 0), (4, 9), (8, 0), (3, 13), (5, 10), (8, 9), (14, 13), (0, 5), (2, 2), (11, 5), (2, 11), (13, 8), (6, 2), (7, 1), (6, 11), (7, 10), (4, 2), (5, 3), (8, 2), (9, 1), (5, 12), (8, 11), (0, 7), (2, 4), (11, 7), (13, 1), (13, 10), (7, 3), (7, 12), (3, 8), (14, 8), (9, 3), (11, 0), (5, 14), (0, 9), (6, 6), (7, 5), (7, 14), (12, 13), (3, 10), (5, 7), (14, 10), (9, 5), (9, 14), (13, 5), (7, 7), (14, 3), (3, 12), (14, 12), (9, 7), (6, 1), (7, 0), (1, 14), (3, 5), (4, 4), (9, 0), (3, 14), (14, 14), (4, 13), (9, 9), (10, 1), (13, 0), (10, 10), (1, 7), (13, 9), (7, 11), (14, 7), (5, 4), (9, 2), (5, 13), (8, 6), (1, 0), (13, 2), (10, 12), (1, 9), (11, 11), (2, 8), (13, 11), (7, 4), (6, 8), (12, 3), (3, 0), (12, 12), (5, 6), (8, 8), (10, 5), (13, 4), (0, 4), (2, 1), (10, 14), (1, 11), (2, 10), (12, 5), (3, 2), (14, 2), (4, 1), (12, 14), (4, 10), (1, 4), (11, 6), (1, 13), (2, 12), (6, 3), (6, 12), (12, 7), (14, 4), (4, 3), (10, 9), (1, 6), (9, 11), (2, 5), (11, 8), (2, 14), (6, 5), (12, 0), (6, 14), (7, 13), (12, 9), (14, 6), (4, 5), (11, 1), (8, 14), (9, 13), (0, 10), (2, 7), (13, 13), (12, 2), (12, 11), (4, 7), (5, 8), (10, 4), (1, 1), (0, 3), (9, 6), (11, 3), (10, 13), (11, 12), (2, 9), (13, 6), (7, 8)}
        a_paths = list(a_paths)
        self.image = pygame.image.load('images/floor.bmp').convert()
        i = 0
        for path in a_paths:
            pos = list(a_paths[i])
            pos_x = pos[1] * 44
            pos_y = pos[0] * 44
            self.window.blit(self.image, (pos_x, pos_y))
            i = i + 1

        pygame.display.flip()

    def screen_walls(self):
        """ """
        self.a_walls = {(12, 4), (5, 1), (10, 6), (9, 8), (0, 14), (11, 14), (3, 6), (9, 10), (1, 8), (6, 4), (6, 13), (5, 5), (8, 4), (0, 0), (9, 12), (11, 9), (13, 3), (1, 10), (13, 12), (3, 1), (14, 1), (0, 2), (11, 2), (1, 3), (1, 12), (13, 14), (12, 6), (3, 3), (5, 0), (5, 9), (4, 11), (11, 4), (10, 8), (1, 5), (13, 7), (2, 13), (7, 9), (12, 8), (14, 5), (5, 2), (5, 11), (8, 13), (2, 6), (7, 2), (12, 1), (12, 10), (3, 7), (4, 6), (10, 3), (0, 11), (14, 0), (3, 9), (14, 9), (4, 8), (1, 2), 
(0, 13), (11, 13), (6, 10), (3, 11), (14, 11), (8, 1), (8, 10), (10, 7), (0, 6), (2, 3), (3, 4), (4, 12), (8, 3), (10, 
0), (8, 12), (0, 8), (4, 14), (8, 5), (10, 2), (9, 4), (0, 1), (10, 11), (11, 10), (6, 7), (7, 6), (8, 7), (2, 0), (0, 
12), (6, 0), (6, 9)}
        self.a_walls = list(self.a_walls)
        self.image = pygame.image.load('images/wall.bmp').convert()
        i = 0
        for wall in self.a_walls:
            pos = list(self.a_walls[i])
            pos_x = pos[1] * 44
            pos_y = pos[0] * 44
            self.window.blit(self.image, (pos_x, pos_y))
            i = i + 1

        pygame.display.flip()

    def screen_start(self):
        a_start = list({(0, 3)})
        self.image = pygame.image.load('images/MacGyver.png').convert()
        pos_x = a_start[0][1] * 44
        pos_y = a_start[0][0] * 44
        self.window.blit(self.image, (pos_x, pos_y))

        pygame.display.flip()

    def screen_goal(self):
        a_goal = list({(4, 9)})
        self.image = pygame.image.load('images/Gardien.png').convert()
        pos_x = a_goal[0][1] * 44
        pos_y = a_goal[0][0] * 44
        self.window.blit(self.image, (pos_x, pos_y))

        pygame.display.flip()

    def screen_items(self):
        pass


if __name__ == '__main__':
    
    m = Maze(constants.FILENAME)   
    ms = MazeScreen(m.paths, m.walls, m.start, m.goal, m.items)
    ms.draw_maze()

