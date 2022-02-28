#Author: Ben-Edwards44


import math
import pygame


SCREEN_SIZE = (500, 500)


pygame.init()
window = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Spring Physics")
window.fill((255, 255, 255))


class spring:
    def __init__(self, spring_constant, rest_pos, anchor_pos, initial_extension):
        self.k = spring_constant
        self.anchor_pos = anchor_pos
        self.x = rest_pos[0]
        self.y = rest_pos[1] + initial_extension

        self.velocity_y = 0
        self.velocity_x = 0

        self.rest_length = math.sqrt((self.anchor_pos[0] - rest_pos[0])**2 + (self.anchor_pos[1] - rest_pos[1])**2)

    def calculate_force(self):
        length = math.sqrt((self.x - self.anchor_pos[0])**2 + (self.y - self.anchor_pos[1])**2)
        return self.k * (length - self.rest_length)

    def calc_theta(self):
        if self.x == self.anchor_pos[0]:
            return math.radians(90)

        gradient = (self.y - self.anchor_pos[1]) / (self.x - self.anchor_pos[0])
        return math.atan(gradient)

    def update_pos(self):
        f = self.calculate_force()
        theta = self.calc_theta()

        if theta < 0:
            theta += math.radians(180)

        self.velocity_y += -f * math.sin(theta)
        self.velocity_x += -f * math.cos(theta)

        if self.x < self.anchor_pos[0] and abs(self.x - self.anchor_pos[0]) > 4:
            self.velocity_x += 0.001 * abs(self.x - self.anchor_pos[0])
        elif self.x > self.anchor_pos[0] and abs(self.x - self.anchor_pos[0]) > 4:
            self.velocity_x -= 0.001 * abs(self.x - self.anchor_pos[0])

        self.y += self.velocity_y
        self.x += self.velocity_x

        self.velocity_y *= 0.99
        self.velocity_x *= 0.99

    def draw(self):
        self.update_pos()

        window.fill((255, 255, 255))

        pygame.draw.line(window, (0, 0, 0), self.anchor_pos, (int(self.x), int(self.y)), 6)

        for i in range(2):
            pygame.draw.circle(window, (255 * i, 255 * i, 255 * i), (int(self.x), int(self.y)), 20 - i * 6)

        pygame.display.update()


s = spring(0.01, (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2 + 50), (SCREEN_SIZE[0] // 2, 0), 100)


clock = pygame.time.Clock()
while True:
    clock.tick(60)
    s.draw()

    if pygame.mouse.get_pressed(3)[0]:
        s.velocity_y = 0
        s.velocity_x = 0
        s.x, s.y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
