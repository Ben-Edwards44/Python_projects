#Author: Ben-Edwards44


import pygame
import time
import math


SCREEN_SIZE = (500, 500)
RADIUS = 200
OFFSET = 10


magnitude = RADIUS / 58


pygame.init()
window = pygame.display.set_mode(SCREEN_SIZE)


def main():
    s = time.time()
    m = s / 60
    h = m / 60
    t = [h % 12, m % 60, s % 60]

    angs = [360 / 12 * t[0] - 90, 360 / 60 * t[1] - 90, 360 / 60 * t[2] - 90]

    window.fill((0, 0, 0))
    draw_hands(angs)
    draw_clock()

    pygame.display.set_caption(f"{int(t[0])} : {int(t[1])} : {t[2]:.2f}")
    pygame.display.update()


def draw_hands(theta):
    for i, x in enumerate(theta):
        mag = magnitude - OFFSET / 58

        if i == 0:
            point = rotate(math.radians(x), mag / 1.5)
        else:
            point = rotate(math.radians(x), mag)

        pygame.draw.line(window, (255, 255, 255), convert_coords(0, 0), convert_coords(point[0], point[1]), 2)


def draw_clock():
    pygame.draw.circle(window, (255, 255, 255), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2), RADIUS, 4)

    for i in range(0, 12):
        point = rotate(math.radians(360 / 12 * i), magnitude)
        point2 = rotate(math.radians(360 / 12 * i), magnitude / 1.4)
        pygame.draw.line(window, (255, 255, 255), (convert_coords(point[0], point[1])), (convert_coords(point2[0], point2[1])), 2)


convert_coords = lambda x, y: (int(x + SCREEN_SIZE[0] // 2), int(y + SCREEN_SIZE[1] // 2))
rotate = lambda theta, magnitude: (magnitude * math.degrees(math.cos(theta)), magnitude * math.degrees(math.sin(theta)))
        

while True:
    main()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()
