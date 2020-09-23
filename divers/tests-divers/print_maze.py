import pygame

# class PrintMaze:
#     """ """
#     def __init__(self, mg_game):
#         self.screen = mg_game.screen
#         self.screen_rect = mg_game.screen.get_rect()

#         self.image = pygame.image.load('images/aiguille.png')
#         self.rect = self.image.get_rect()
#         self.rect.midbottom = self.screen_rect.midbottom

#     def blitme(self):
#         self.screen.blit(self.image, self.rect)

class Maze:

    windowWidth = 660
    windowHeight = 660
    player = 0

    def __init__(self):
       self.M = 10
       self.N = 8
       self.on_render()
       self.maze = [ 1,1,1,1,1,1,1,1,1,1,
                     1,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,1,
                     1,0,1,1,1,1,1,1,0,1,
                     1,0,1,0,0,0,0,0,0,1,
                     1,0,1,0,1,1,1,1,0,1,
                     1,0,0,0,0,0,0,0,0,1,
                     1,1,1,1,1,1,1,1,1,1,]

    def draw(self, display_surf, image_surf):
       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
           if self.maze[ bx + (by*self.M) ] == 1:
               display_surf.blit(image_surf,( bx * 44 , by * 44))
      
           bx = bx + 1
           if bx > self.M-1:
               bx = 0 
               by = by + 1
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("images/floor.bmp").convert()
        self._block_surf = pygame.image.load("images/floor.bmp").convert()

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
        self.maze.draw(self._display_surf, self._block_surf)
        pygame.display.flip()

a = Maze()

a.on_init()