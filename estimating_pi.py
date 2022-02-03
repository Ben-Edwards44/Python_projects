#Author: Ben-Edwards44


import random
import math
import pygame


SCREEN_SIZE = (400, 400)
RADIUS = 100
SAMPLES = 5e3


def draw_background():
    global window

    pygame.init()
    window = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Estimating Pi")
    window.fill((0, 0, 0))

    pygame.draw.circle(window, (255, 255, 255), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2), RADIUS, 4)
    pygame.draw.rect(window, (255, 255, 255), (SCREEN_SIZE[0] // 2 - RADIUS, SCREEN_SIZE[1] // 2 - RADIUS, RADIUS * 2, RADIUS * 2), 4)

    pygame.display.update()


def place_points():
    successes = 0
    total = 0

    for _ in range(int(SAMPLES)):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        draw_points(x, y)

        if length(x, y) <= 1:
            successes += 1

        total += 1

        display_estimate(successes / total * 4)


length = lambda x, y: math.sqrt(x**2 + y**2)


def draw_points(x, y):
    colour = (0, 255, 0) if length(x, y) < 1 else (255, 0, 0)

    pygame.draw.circle(window, colour, (int(SCREEN_SIZE[0] // 2 + x * RADIUS), int(SCREEN_SIZE[1] // 2 + y * RADIUS)), 2)
    pygame.display.update()


def display_estimate(pi_estimate):
    pygame.draw.rect(window, (0, 0, 0), (10, SCREEN_SIZE[1] // 2 + RADIUS + 20, SCREEN_SIZE[0] - 20, 50))
    font = pygame.font.Font(None, 24)
    text = font.render(str(pi_estimate), True, (255, 255, 255), (0, 0, 0))
    r = text.get_rect()
    r.center = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2 + 1.5 * RADIUS)

    window.blit(text, r)
    pygame.display.update()


draw_background()
place_points()


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()
