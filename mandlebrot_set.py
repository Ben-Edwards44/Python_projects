import pygame


SCREEN_SIZE = (650, 650)
RANGE_X = (-1.5, 1.5)
RANGE_Y = (-1.5, 1.5)


pygame.init()
window = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Mandlebrot set")


def mandlebrot_set():
    for i in range(-SCREEN_SIZE[0], 1):
        for x in range(-SCREEN_SIZE[1] // 2, SCREEN_SIZE[1] // 2):
            for y in range(2):
                a = RANGE_X[y] / SCREEN_SIZE[0] * i
                b = RANGE_Y[y] / SCREEN_SIZE[1] * x

                c = find_limit(a, b)
                pygame.draw.circle(window, (c, c, c), (i + SCREEN_SIZE[0], x + SCREEN_SIZE[1] // 2), 1)
                
    pygame.display.update()


def find_limit(a, b):
    origional_a, origional_b = a, b

    for i in range(1, 51):
        new_a = a**2 - b**2
        new_b = 2 * a * b

        a = new_a + origional_a
        b = new_b + origional_b

        if abs(a + b) > 10:
            return 255 - (255 // i + 50 % 255)

    return 0


mandlebrot_set()


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()