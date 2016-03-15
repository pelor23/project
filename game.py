# Here we import method exit() from module called sys
from sys import exit

# Here we import two things: firstly the library called pygame;
# Secondly from pygame.locals we import the entire contents.
import pygame
from pygame.locals import *

# Here we set window size.
SCREEN_SIZE = (800, 600)


# Here is our main class.
class SpaceInvadersGame(object):
    # Here is the method responsible for initializing and setting the pygame library and display windows.
    def __init__(self):
        pygame.init()
        flag = DOUBLEBUF
        self.surface = pygame.display.set_mode(SCREEN_SIZE, flag)
        self.gamestate = 1
        self.loop()

        # Below we add welcome text and support the enter key.
        ## This line of code clears the screen and sets the background color to black.
        self.surface.fill((0, 0, 0))


        ## Here we set the font.
        ## We call it with the value None (at this point pygame load the default font used in pygame)
        ## and set its size to 15.
        gamefont = pygame.font.Font(None, 15)
        ## Font rendering with the inscription.
        ## We set two additional parameters - apart from the content, add information, that font is to be smoothed,
        ## and what is its color.
        hello_label = gamefont.render("Press ENTER to start the game", 1, (255, 255, 0))
        ## We add the label to display.
        self.surface.blit(hello_label, (100, 100))
        ## We send here a signal to update the displayed image.
        pygame.display.flip()
        ## Additionally, we set the loop to listen pressing the enter button
        ## and start the game and the handle shutdown the window and escape key.
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_RETURN:
                    self.gamestate = 1
                    self.loop()
                if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                    exit()

    # Here is the method, which is responsible for the termination of the game and exit to the main system.
    def game_exit(self):
        """ This function interrupts the action of the game and exit to the system"""
        exit()

    # This is the main loop of the game, which supports the shutdown event and escape key.
    # Here also will be located service of our game and events
    def loop(self):
        """ Main loop of the game """
        while self.gamestate == 1:
            for event in pygame.event.get():
                if (event.type == QUIT or
                        (event.type == KEYDOWN and event.key == K_ESCAPE)
                    ):
                    self.gamestate = 0
        self.game_exit()

        keys = pygame.key.get_pressed()

        if keys[K_RIGHT]:
            self.move(1, 0)

        if keys[K_LEFT]:
            self.move(-1, 0)

        self.surface.fill((0, 0, 0))
        self.surface.blit(self.player, (self.player_x, self.player_y))

        pygame.display.flip()

    # Here we add new method, which set our user.
    def draw_player(self):
        ## Here we load a image for player.
        self.player = pygame.image.load("space_ship.png")
        ## Here we set his/her speed.
        self.speed = 1.2
        ## Here we set his/her start position.
        self.player_x = SCREEN_SIZE[0]/2 - 25
        self.player_y = SCREEN_SIZE[1] - 75

    # Here we add method, which is responsible for updating player position.
    def move(self, dirx, diry):
        self.player_x = self.player_x + (dirx * self.speed)
        self.player_y = self.player_y + (diry * self.speed)


if __name__ == '__main__':
    SpaceInvadersGame()
