import pygame
import time


VISULISE = True
WAIT_TIME = 0.0001
NUM = 512


def pascals_triangle(n):
    global triangle
    global screen_size

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
            continue

        triangle.append([])
        for x in range(len(triangle[i - 1]) + 1):
            if x == 0 or x == len(triangle[i - 1]):
                triangle[i].append(1)
                continue

            triangle[i].append(triangle[i - 1][x] + triangle[i - 1][x - 1])

    for i in range(n):
        for x, y in enumerate(triangle[i]):
            if y % 2 == 0:
                triangle[i][x] = 0
            else:
                triangle[i][x] = 1

    screen_size = (len(triangle[-1]), n)


def convert_triangle():
    global final_triangle

    final_triangle = [[] for _ in range(len(triangle))]
    for j, i in enumerate(triangle):
        if len(i) < screen_size[0]:
            s = (screen_size[0] - len(i)) // 2

            for _ in range(s):
                final_triangle[j].append(0)
            for x in triangle[j]:
                final_triangle[j].append(x)
            for _ in range(s):
                final_triangle[j].append(0)


def draw_sierpinski_triangle():
    for j, i in enumerate(final_triangle):
        for x, y in enumerate(i):
            if y == 1:
                pygame.draw.circle(window, (0, 0, 0), (x, j), 1)

        if VISULISE:
            pygame.display.update()
            time.sleep(WAIT_TIME)

    pygame.display.update()


pascals_triangle(NUM)


pygame.init()
window = pygame.display.set_mode(screen_size)
window.fill((255, 255, 255))


convert_triangle()
draw_sierpinski_triangle()


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()