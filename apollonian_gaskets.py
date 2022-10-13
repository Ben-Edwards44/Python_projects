import pygame
import math
import cmath
import random


ITERATIONS = 5000
NUM_CIRCLES = 3
MIN_RADIUS = 1
BG_COLOUR = (255, 255, 255)
LINE_COLOUR = (0, 0, 0)


def find_tangent_circle(circ1, circ2, circ3):
    #Descartes' theorem: https://en.wikipedia.org/wiki/Descartes%27_theorem

    c1, r1 = circ1
    c2, r2 = circ2
    c3, r3 = circ3

    k1 = 1 / r1
    k2 = 1 / r2
    k3 = 1 / r3

    new_k1 = k1 + k2 + k3 + 2 * math.sqrt(k1 * k2 + k2 * k3 + k3 * k1)
    new_k2 = k1 + k2 + k3 - 2 * math.sqrt(k1 * k2 + k2 * k3 + k3 * k1)
    new_c10 = (c1 * k1 + c2 * k2 + c3 * k3 + 2 * cmath.sqrt((k1 * k2 * c1 * c2 + k2 * k3 * c2 * c3 + k1 * k3 *c1 * c3))) / new_k1
    new_c11 = (c1 * k1 + c2 * k2 + c3 * k3 - 2 * cmath.sqrt((k1 * k2 * c1 * c2 + k2 * k3 * c2 * c3 + k1 * k3 *c1 * c3))) / new_k1
    new_c20 = (c1 * k1 + c2 * k2 + c3 * k3 + 2 * cmath.sqrt((k1 * k2 * c1 * c2 + k2 * k3 * c2 * c3 + k1 * k3 *c1 * c3))) / new_k2
    new_c21 = (c1 * k1 + c2 * k2 + c3 * k3 - 2 * cmath.sqrt((k1 * k2 * c1 * c2 + k2 * k3 * c2 * c3 + k1 * k3 *c1 * c3))) / new_k2

    new_circles = []
    new_circles.append((new_c10, 1 / new_k1))
    new_circles.append((new_c20, 1 / new_k2))
    new_circles.append((new_c11, 1 / new_k1))
    new_circles.append((new_c21, 1 / new_k2))

    correct_circles = []
    for i in new_circles:
        if check_tangent_all(i, (c1, r1), (c2, r2), (c3, r3)):
            correct_circles.append(i)

    return correct_circles


def check_tangent(circ1, circ2):
    c1, r1 = circ1
    c2, r2 = circ2

    distance_c = (c1.real - c2.real)**2 + (c1.imag - c2.imag)**2
    distance_r = (r1 + r2)**2

    if abs(distance_r - distance_c) < 0.0001:
        return True
    else:
        return False


def check_tangent_all(circ1, circ2, circ3, circ4):
    test_circles = (circ2, circ3, circ4)

    for i in test_circles:
        if not check_tangent(circ1, i):
            return False

    return True


def approx_equal(circ1, circ2):
    c1, r1 = circ1
    c2, r2 = circ2

    if abs(r1 - r2) < 0.0001 and abs(c1.real - c2.real) < 0.0001 and abs(c1.imag - c2.imag) < 0.0001:
        return True
    else:
        return False


def intersect(circ1, circ2):
    dist = abs(circ1[0] - circ2[0])
    r_min = min(abs(circ1[1]), abs(circ2[1]))
    r_max = max(abs(circ1[1]), abs(circ2[1]))
    
    return (dist + 0.0001 < r_min + r_max and dist + r_min > r_max + 0.0001)


def initial_circles(num):
    global circles

    circles = []

    theta = math.radians(360 / num)
    radius = math.sqrt(2 - 2 * math.cos(theta)) / 2 * 100
    radius_outer = radius + 100
    circles.append((complex(0, 0), -radius_outer))

    for n in range(num):
        new_angle = n * theta
        y = math.sin(new_angle - math.radians(90)) * 100
        x = math.cos(new_angle - math.radians(90)) * 100

        circles.append((complex(x, y), radius))

    radius_center = radius_outer - 2 * radius
    if radius_center > MIN_RADIUS:
        circles.append((complex(0, 0), radius_center))

    for i in circles:
        draw_circle(i)


def valid_circle(circ):
    if circ[1] < MIN_RADIUS:
        return False

    for i in circles:
        if intersect(circ, i) or approx_equal(circ, i):
            return False

    return True


def draw_circle(circle):
    center = (round(circle[0].real + 250), round(circle[0].imag + 250))
    radius = round(abs(circle[1]))

    pygame.draw.circle(window, LINE_COLOUR, center, radius, 1)
    pygame.display.update()


def init():
    global window

    pygame.init()
    pygame.display.set_caption("Apollonian Gasket Fractal")
    window = pygame.display.set_mode((500, 500))
    window.fill(BG_COLOUR)


def main():
    for _ in range(ITERATIONS):
        while True:
            c1 = random.choice(circles)
            c2 = random.choice(circles)
            c3 = random.choice(circles)

            if not approx_equal(c1, c2) and not approx_equal(c2, c3):
                if check_tangent(c1, c2) and check_tangent(c1, c3) and check_tangent(c2, c3):
                    break

        new = find_tangent_circle(c1, c2, c3)

        for i in new:
            if valid_circle(i):
                circles.append(i)
                draw_circle(i)

    print("Done!")


init()
initial_circles(NUM_CIRCLES)
main()


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()