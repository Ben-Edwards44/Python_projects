#moreBouncePhysics.py
#Author: Ben-Edwards44


import pygame
import time
import random


screen_size = (450, 450)
wait_time = 0.002
damper_y = 0.8
damper_x = 0.7


def main():
    global window
    global damper_x

    window = pygame.display.set_mode(screen_size)
    window.fill((255, 255, 255))
    pygame.display.update()

    damper_x += random.randint(-2, 2) / 10
    ball1 = ball([random.randint(-15, 15) / 10, random.randint(-20, 20) / 10], [random.randint(45, screen_size[0] - 45), random.randint(15, 30)])
    ball1.bounce()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                damper_x = 0.7
                damper_x += random.randint(-2, 2) / 10
                ball1 = ball([random.randint(-10, 10) / 10, random.randint(-20, 20) / 10], [random.randint(45, screen_size[0] - 45), random.randint(15, 30)])
                ball1.bounce()


class ball:
    def __init__(self, start_momentum, start_pos):
        self.max_momentum_y = 4.5
        self.max_momentum_x = 1
        self.momentum_x = start_momentum[0]
        self.momentum_y = start_momentum[1]
        self.pos = start_pos

    def bounce(self):
        while self.max_momentum_y > 0.5:
            if self.momentum_y < self.max_momentum_y:
                self.momentum_y += 0.02
            
            if self.momentum_x > self.max_momentum_x:
                self.momentum_x = self.max_momentum_x

            if not 0 < self.pos[0] < screen_size[0] - 40:
                self.momentum_x *= -1
                self.max_momentum_x *= damper_x
            if not 0 < self.pos[1] < screen_size[1] - 40:
                self.momentum_y *= -1
                self.max_momentum_y *= damper_y

            self.pos[0] += self.momentum_x
            self.pos[1] += self.momentum_y

            window.fill((255, 255, 255))
            pygame.draw.rect(window, (0, 0, 0), [self.pos[0], self.pos[1], 40, 40])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            time.sleep(wait_time)


if __name__ == "__main__":
    main()
