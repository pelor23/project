# Here we import method exit() from module called sys
from sys import exit

# Here we import two things: firstly the library called pygame
# Secondly from pygame.locals we import the entire contents
import pygame
from pygame.locals import *

# Here we set window size
SCREEN_SIZE = (800, 600)


# Here is our main class
class SpaceInvadersGame(object):
    # Here is the method responsible for initializing and setting the pygame library and display windows
    def __init__(self):
        pygame.init()
        flag = DOUBLEBUF
        self.surface = pygame.display.set_mode(SCREEN_SIZE, flag)
        self.gamestate = 1
        self.loop()

    # Here is the method, which is responsible for the termination of the game and exit to the main system
    def game_exit(self):
        """ funkcja przerywa dzialanie gry i wychodzi do systemu"""
        exit()

    # This is the main loop of the game, which supports the shutdown event and escape key.Here also will be located service of our game and events
    def loop(self):
        """ glowna petla gry """
        while self.gamestate == 1:
            for event in pygame.event.get():
                if (event.type == QUIT or
                        (event.type == KEYDOWN and event.key == K_ESCAPE)
                    ):
                    self.gamestate = 0
        self.game_exit()


if __name__ == '__main__':
    SpaceInvadersGame()
