# Here we import method exit() from module called sys
from sys import exit

# Here we import two things: firstly the library called pygame;
# Secondly from pygame.locals we import the entire contents.
import pygame
from pygame.locals import *

# Here we set window size.
SCREEN_SIZE = (800, 600)
# Here we have constant, which stores pygame clock.
CLOCK = pygame.time.Clock()


# Here we have bullet's class
class Bullet:
    ## Here is method coords of bullet and image of our bullet.
    def __init__(self, surface, x_coord, y_coord):
        self.surface = surface
        self.x = x_coord + 24
        self.y = y_coord
        self.image = pygame.image.load('laser.png')
        return

    ## Here is method which updates coords of this bullet.
    def update(self, y_amount=5):
        self.y -= y_amount
        self.surface.blit(self.image, (self.x, self.y))
        return


# Here is our main class.
class SpaceInvadersGame(object):
    ## Here is the method responsible for initializing and setting the pygame library and display windows.
    def __init__(self):
        pygame.init()
        flag = DOUBLEBUF
        self.surface = pygame.display.set_mode(SCREEN_SIZE, flag)
        self.surface.fill((0, 0, 0))
        gamefont = pygame.font.Font(None, 15)
        self.bullets_array = []


        hello_label = gamefont.render("Press ENTER to start the game", 1, (255, 255, 0))
        self.surface.blit(hello_label, (100, 100))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_RETURN:
                    self.gamestate = 1
                    self.loop()
                if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                    exit()


    ## Here is the method, which is responsible for the termination of the game and exit to the main system.
    def game_exit(self):
        """ This function interrupts the action of the game and exit to the system"""
        exit()


    ## This is the main loop of the game, which supports the shutdown event and escape key.
    ## Here also will be located service of our game and events
    def loop(self):
        """ Main loop of the game """
        can_shoot = True
        fire_wait = 500
        while self.gamestate == 1:
            for event in pygame.event.get():
                if (event.type == QUIT or
                        (event.type == KEYDOWN and event.key == K_ESCAPE)
                    ):
                    self.gamestate = 0
        self.game_exit()
        keys = pygame.key.get_pressed()

        if keys[K_RIGHT] and self.player_x < SCREEN_SIZE[0] - 50:
            self.move(1, 0)

        if keys[K_LEFT] and self.player_x > 0:
            self.move(-1, 0)

        if keys[K_SPACE] and can_shoot:
            bullet = Bullet(self.surface, self.player_x, self.player_y)
            self.bullets_array.append(bullet)
            can_shoot = False

        if not can_shoot and fire_wait <= 0:
            can_shoot = True
            fire_wait = 500

        fire_wait -= CLOCK.tick(60)

        self.surface.fill((0, 0, 0))
        self.surface.blit(self.player, (self.player_x, self.player_y))

        for bullet in self.bullets_array:
            bullet.update()
            if bullet.y < 0:
                self.bullets_array.remove(bullet)

        pygame.display.flip()


    ## Here we add new method, which set our user.
    def draw_player(self):
        self.player = pygame.image.load("space_ship.png")
        self.speed = 1.2
        self.player_x = SCREEN_SIZE[0]/2 - 25
        self.player_y = SCREEN_SIZE[1] - 75


    ## Here we add method, which is responsible for updating player position.
    def move(self, dirx, diry):
        self.player_x = self.player_x + (dirx * self.speed)
        self.player_y = self.player_y + (diry * self.speed)


if __name__ == '__main__':
    SpaceInvadersGame()
