import pygame
import sys

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
        self.window = pygame.display.set_mode((660, 660))

        self.m = Maze(constants.FILENAME)  
        self.mg = MacGyver(self.m)

        # display the maze with pygame
        MazeScreen(self.m.paths, self.m.walls, self.m.start, self.m.goal, self.m.item1, self.m.item2, self.m.item3)

        self.start = self.m.start
        self.display_mac()

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            self.check_events()
    
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
            validate = self.mg.move('RIGHT')
            if validate == True:
                self.move_mac((44, 0))
            self.check_end()
        elif event.key == pygame.K_LEFT:
            validate = self.mg.move('LEFT')
            if validate == True:
                self.move_mac((-44, 0))
            self.check_end()
        elif event.key == pygame.K_DOWN:
            validate = self.mg.move('DOWN')
            if validate == True:
                self.move_mac((0, 44))
            self.check_end()
        elif event.key == pygame.K_UP:
            validate = self.mg.move('UP')
            if validate == True:
                self.move_mac((0, -44))
            self.check_end()
        elif event.key == pygame.K_q:
            sys.exit()

    def display_mac(self):
        """ Display MacGyver on the maze. """
        self.img_mg = pygame.image.load('images/MacGyver.png').convert()
        position_mac = list(self.start)[0]
        pos_x = position_mac.y * 44
        pos_y = position_mac.x * 44
        self.position_perso = pygame.Rect((pos_x, pos_y, 28, 38))
        self.window.blit(self.img_mg, self.position_perso)
        pygame.display.flip()

    def move_mac(self, move):
        """ """
        self.image = pygame.image.load('images/floor.bmp').convert()
        self.window.blit(self.image, self.position_perso)
        self.position_perso = self.position_perso.move(move)
        self.window.blit(self.img_mg, self.position_perso)
        pygame.display.flip() 


    def check_end(self):
        if self.mg.mac_goal == True:
            if 'item1' in self.mg.bag and 'item2' in self.mg.bag and 'item3' in self.mg.bag:
                print('win')
            else:
                print('loose')



if __name__ == "__main__":
    hmg = Main()
    hmg.run_game()
