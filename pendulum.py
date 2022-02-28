#Author: Ben-Edwards44
#An article on the physics of a pendulum: https://www.physicsclassroom.com/class/waves/Lesson-0/Pendulum-Motion


import math
import random
import pygame


SCREEN_SIZE = (600, 600)
INITIAL_NUM = 2


pygame.init()
window = pygame.display.set_mode(SCREEN_SIZE)


class pendulum:
    def __init__(self, mass, arm_length, center, start_pos):
        self.mass = mass
        self.arm_length = arm_length
        self.center = center
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.max_y = start_pos[1]
        self.prev_x = self.x
        
        self.accelerate = False
        self.multiplier = 0.1
        self.total_energy = self.mass * 9.8 * (self.arm_length - self.y)

    def find_velocity(self):
        grav_potential_energy = self.mass * 9.8 * (self.arm_length - self.y)
        kinetic_energy = self.total_energy - grav_potential_energy

        return math.sqrt(abs(kinetic_energy) / (0.5 * self.mass))

    def find_next_pos(self):
        theta = abs(math.degrees(math.atan(-(self.x / self.y))))
        velocity_x = self.find_velocity() * math.cos(math.radians(theta)) * self.multiplier

        if self.accelerate:
            self.x += velocity_x
        else:
            self.x -= velocity_x

        self.y = math.sqrt(self.arm_length**2 - self.x**2)

        if self.y <= self.max_y and abs(self.prev_x - self.x) > 1:
            self.accelerate = not self.accelerate
            self.prev_x = self.x

    convert_coords = lambda self, x, y: (int(x + self.center[0]), int(y + self.center[1]))

    def draw(self):
        self.find_next_pos()

        pygame.draw.circle(window, (255, 255, 255), self.convert_coords(self.x, self.y), 5)
        pygame.draw.line(window, (255, 255, 255), self.center, self.convert_coords(self.x, self.y))


def display_pendulums():
    window.fill((0, 0, 0))

    for i in pendulums:
        i.draw()

    pygame.display.update()


def make_pendulums(n):
    for _ in range(n):
        length = random.randint(10, SCREEN_SIZE[1] // 2)
        pendulums.append(pendulum(random.randint(1, 100), length, (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2), (length - 1, 1)))


if __name__ == "__main__":
    pendulums = []
    make_pendulums(INITIAL_NUM)

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        display_pendulums()

        if pygame.mouse.get_pressed(3)[0]:
            make_pendulums(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
