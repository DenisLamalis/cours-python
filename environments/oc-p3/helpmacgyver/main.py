import pygame
import sys

from maze import Maze
from displaymaze import DisplayMaze
from macgyver import MacGyver
# from position import Position
from settings import Settings


class Main:
    """ Game management. """

    def __init__(self):
        """ Initialize the game. """
        pygame.init()
        self.settings = Settings()
        self.window = pygame.display.set_mode(self.settings.maze_dimensions)
        self.m = Maze(self.settings.FILENAME)
        self.mg = MacGyver(self.m)

        # display the maze with pygame
        DisplayMaze(self.m.paths, self.m.walls, self.m.start, self.m.goal, self.m.item1, self.m.item2, self.m.item3)

        self.start = self.m.start
        self.display_mac()
        self.state = True

    def run_game(self):
        """ Start the main loop for the game. """

        while self.state is True:
            # self.msg_win()
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
            if validate is True:
                self.move_mac(((self.settings.cell_dimension_x), 0))
            self.check_end()
        elif event.key == pygame.K_LEFT:
            validate = self.mg.move('LEFT')
            if validate is True:
                self.move_mac(((self.settings.cell_dimension_x * -1), 0))
            self.check_end()
        elif event.key == pygame.K_DOWN:
            validate = self.mg.move('DOWN')
            if validate is True:
                self.move_mac((0, (self.settings.cell_dimension_x)))
            self.check_end()
        elif event.key == pygame.K_UP:
            validate = self.mg.move('UP')
            if validate is True:
                self.move_mac((0, (self.settings.cell_dimension_x * -1)))
            self.check_end()
        elif event.key == pygame.K_q:
            sys.exit()

    def display_mac(self):
        """ Display MacGyver on the maze. """
        self.img_mg = pygame.image.load(self.settings.macgyver).convert()
        position_mac = list(self.start)[0]
        pos_x = position_mac.y * 44
        pos_y = position_mac.x * 44
        self.position_perso = pygame.Rect((pos_x, pos_y, 28, 38))
        self.window.blit(self.img_mg, self.position_perso)
        pygame.display.flip()

    def move_mac(self, move):
        """ I'm moving the image of MacGYver. """
        self.image = pygame.image.load(self.settings.floor).convert()
        self.window.blit(self.image, self.position_perso)
        self.position_perso = self.position_perso.move(move)
        self.window.blit(self.img_mg, self.position_perso)
        pygame.display.flip()

    def check_end(self):
        """ I'm checking if this is the end cell. """
        if self.mg.mac_goal is True:
            if 'item1' in self.mg.bag and 'item2' in self.mg.bag and 'item3' in self.mg.bag:
                self.win_game()
            else:
                self.loose_game()

    def loose_game(self):
        """ I'm saying this is a loose game and I'm closing the game. """
        self.msg_loose()
        self.state = False
        pygame.time.wait(3000)
        return self.state

    def win_game(self):
        """ I'm saying this is a win game and I'm closing the game. """
        self.msg_win()
        pygame.time.wait(3000)
        self.state = False
        return self.state

    def msg_loose(self):
        """ I display the loose text. """
        font = pygame.font.SysFont("arial", 56)
        text = font.render("  You loose !  ", True, (255, 255, 255), (0, 0, 0))
        self.window.blit(text, (200, 300))
        pygame.display.flip()

    def msg_win(self):
        """ I display the win text"""
        font = pygame.font.SysFont("arial", 56)
        text = font.render("  You win !  ", True, (0, 0, 0), (255, 255, 255))
        self.window.blit(text, (200, 300))
        pygame.display.flip()


if __name__ == "__main__":
    hmg = Main()
    hmg.run_game()
