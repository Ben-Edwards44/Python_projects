import pygame
from time import sleep


# Cool values for c: (-0.52, 0.57) (-0.4, 0.6) (-0.6078, 0.4380) (0.295, 0.55) (-0.624, 0.435)
c = (-0.624, 0.435)
RANGE = (-1, 1)
SCREEN_SIZE = (500, 500)


pygame.init()
pygame.display.set_caption(f"Julia Set with c = {c[0]} + {c[1]}i")
window = pygame.display.set_mode(SCREEN_SIZE)


def create_julia_set(max_iterations):
    spacing_x = abs(RANGE[0] - RANGE[1]) / SCREEN_SIZE[0]
    spacing_y = abs(RANGE[0] - RANGE[1]) / SCREEN_SIZE[1]

    for i in range(SCREEN_SIZE[0]):
        for x in range(SCREEN_SIZE[1]):
            real = i * spacing_x + RANGE[0]
            imaginary = x * spacing_y + RANGE[0]

            colour = check_diverge((real, imaginary), max_iterations)

            pygame.draw.circle(window, (colour, colour, colour), (i, x), 1)

    pygame.display.update()


# f(z) = z^2 + c
def check_diverge(complex_num, max_iterations):
    za, zb = complex_num
    for i in range(max_iterations):
        z_squared = [za**2 - zb**2, 2 * za * zb]

        for x in range(2):
            z_squared[x] += c[x]

        za, zb = z_squared

        if abs(za) > 10 or abs(zb) > 10:
            return i % 255

    return 255


def update_c(mouse_pos):
    global c

    spacing_x = abs(RANGE[0] - RANGE[1]) / SCREEN_SIZE[0]
    spacing_y = abs(RANGE[0] - RANGE[1]) / SCREEN_SIZE[1]

    real = mouse_pos[0] * spacing_x + RANGE[0]
    imaginary = mouse_pos[1] * spacing_y + RANGE[0]

    c = (real, imaginary)


create_julia_set(100)


while True:
    if pygame.mouse.get_pressed(3)[0]:
        update_c(pygame.mouse.get_pos())
        pygame.display.set_caption(f"Julia Set with c = {c[0]} + {c[1]}i")
        create_julia_set(50)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()
