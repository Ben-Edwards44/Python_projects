#Author: Ben-Edwards44
#How it works: https://www.youtube.com/watch?v=-RdOwhmqP5s&t=1334s


import random


POLYNOMIAL = (3, 4, 2, 1, -5)


def differentiate(polynomial):
    derivative = []
    for i, x in enumerate(polynomial):
        derivative.append((len(polynomial) - 1 - i) * x)

    for i in derivative:
        if i == 0:
            derivative.remove(i)

    return derivative


def find_eq_tangent(x):
    derivative = differentiate(POLYNOMIAL)

    m = 0
    for i, j in enumerate(derivative):
        m += x**(len(derivative) - 1 - i) * j

    y = 0
    for i, j in enumerate(POLYNOMIAL):
        y += x**(len(POLYNOMIAL) - 1 - i) * j

    c = y - m * x
 
    return (-c) / m


def main():
    x = random.randint(-1000, 1000)
    prev = None

    while prev == None or abs(x - prev) > 1e-7:
        prev = x
        x = find_eq_tangent(x)

    roots.append(x)


def sort_roots():
    roots.sort()

    avg_roots = []
    for i, x in enumerate(roots):
        if i + 1 < len(roots) and abs(x - roots[i + 1]) > 0.1 or i == len(roots) - 1:
            avg_roots.append(roots[0:i + 1])

            for _ in range(i + 1):
                roots.pop(0)

    for i in avg_roots:
        print(sum(i) / len(i))


roots = []

for _ in range(int(1e3)):
    main()

sort_roots()
