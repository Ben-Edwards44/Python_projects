#Author: Ben-Edwards44


import pygame
import time
import random


screen_size = (500, 500)
background_colour = (255, 255, 255)
box_colour = (0, 0, 0)
start_max_momentum = 14
start_momentum = 0.5
wait_time = 0.007
damper = 0.8
move_right = False
move_left = False


def main():
    global window

    pygame.init()
    window = pygame.display.set_mode(screen_size)
    window.fill(background_colour)
    pygame.display.update()


class ball:
    def __init__(self, x_pos):
        self.box_pos = [x_pos, 20]
        self.max_momentum = start_max_momentum
        self.momentum = start_momentum
        self.done = False

        self.bounce()

    def bounce(self):
        global move_left
        global move_right

        while self.max_momentum > 0.6 and not self.done:
            if self.box_pos[1] >= screen_size[0] - 50:
                self.momentum = -self.momentum
                self.max_momentum *= damper

            self.box_pos[1] += self.momentum

            if self.momentum < self.max_momentum:
                self.momentum += 0.2
            elif self.momentum < 0:
                self.momentum -= 1

            if move_right and self.box_pos[0] < screen_size[0] - 50:
                self.box_pos[0] += 2
            if move_left and self.box_pos[0] > 0:
                self.box_pos[0] -= 2

            window.fill(background_colour)
            pygame.draw.rect(window, box_colour, [self.box_pos[0], self.box_pos[1], 50, 50], 0)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_SPACE]:
                    self.done = True
                    ball1 = ball(random.randint(25, screen_size[0] - 75))

                if keys[pygame.K_LEFT]:
                    move_left = True
                else:
                    move_left = False

                if keys[pygame.K_RIGHT]:
                    move_right = True
                else:
                    move_right = False

            time.sleep(wait_time)

        if not self.done:
            pygame.draw.rect(window, box_colour, [self.box_pos[0], self.box_pos[1], 50, 50], 0)
            pygame.display.flip()


clock = pygame.time.Clock()
clock.tick(60)


main()
ball1 = ball(random.randint(25, screen_size[0] - 75))


while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        ball2 = ball(random.randint(25, screen_size[0] - 75))
