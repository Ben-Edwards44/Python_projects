#Author: Ben-Edwards44
#Video explaining how the pattern works: https://www.youtube.com/watch?v=JbfhzlMk2eY


import pygame
import random
import time


SCREEN_SIZE = (500, 400)
OFFSET = 5
BG_COLOUR, LINE_COLOUR = (255, 255, 255), (0, 0, 0)
WAIT_TIME = 0.0025
points = []


pygame.init()
window = pygame.display.set_mode(SCREEN_SIZE)


def get_points():
    for y in range(0, SCREEN_SIZE[1], 10):
        for x in range(0, SCREEN_SIZE[0], 10):
            points.append((x + OFFSET, y + OFFSET))


def draw_lines():
    window.fill(BG_COLOUR)

    pygame.draw.line(window, (0, 0, 0), (0 + OFFSET, 0 + OFFSET), (0 + OFFSET, SCREEN_SIZE[1] - OFFSET))
    pygame.draw.line(window, (0, 0, 0), (0 + OFFSET, 0 + OFFSET), (SCREEN_SIZE[0] - OFFSET, 0 + OFFSET))
    pygame.draw.line(window, (0, 0, 0), (SCREEN_SIZE[0] - OFFSET, SCREEN_SIZE[1] - OFFSET), (SCREEN_SIZE[0] - OFFSET, 0 + OFFSET))
    pygame.draw.line(window, (0, 0, 0), (SCREEN_SIZE[0] - OFFSET, SCREEN_SIZE[1] - OFFSET), (0 + OFFSET, SCREEN_SIZE[1] - OFFSET))

    for i in range(SCREEN_SIZE[1] // 10):
        inx = i * SCREEN_SIZE[0] // 10
        for x in range(inx + random.randint(0, 1), inx + SCREEN_SIZE[0] // 10 - 1, 2):
            if points[x + 1][1] == points[x][1]:
                pygame.draw.line(window, LINE_COLOUR, points[x], points[x + 1])
                pygame.display.update()
                time.sleep(WAIT_TIME)

    for i in range(SCREEN_SIZE[0] // 10):
        for x in range(random.randint(0, 1), SCREEN_SIZE[1] // 10 - 1, 2):
            pygame.draw.line(window, LINE_COLOUR, points[x * SCREEN_SIZE[0] // 10 + i], points[(x + 1) * SCREEN_SIZE[0] // 10 + i])
            pygame.display.update()
            time.sleep(WAIT_TIME)


get_points()
draw_lines()


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            draw_lines()
            break
