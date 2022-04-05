import pygame
from random import randint
from time import sleep


LENGTH = 80
SCREEN_SIZE = (800, 300)


pygame.init()
window = pygame.display.set_mode(SCREEN_SIZE)
window.fill((255, 255, 255))


def binary_search(array, n):
    draw_array(array)

    middle_index = len(array) // 2
    item = array[middle_index]

    if item == n:
        return middle_index
    elif item < n:
        return middle_index + 1 + binary_search(array[middle_index + 1:len(array)], n)
    else:
        return binary_search(array[0:middle_index], n)


def draw_array(array):
    window.fill((255, 255, 255))

    width = SCREEN_SIZE[0] // LENGTH - 1
    spacing = width + 1
    height = width if width > 10 else 10
    pygame.draw.rect(window, (0, 255, 0), (spacing * target_value, int(SCREEN_SIZE[1] // 2 - height * 2.5), width, height))

    for i in arr:
        if i in array:
            pygame.draw.rect(window, (0, 0, 0), (i * spacing, SCREEN_SIZE[1] // 2 - 10, width, height))
        else:
            pygame.draw.rect(window, (100, 100, 100), (i * spacing, SCREEN_SIZE[1] // 2 - 10, width, height))

    pygame.display.update()
    sleep(1)


arr = [i for i in range(LENGTH)]
target_value = arr[randint(0, LENGTH - 1)]
index = binary_search(arr, target_value)
draw_array([index])


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()