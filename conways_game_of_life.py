import pygame
from random import randint


SCREEN_SIZE = (600, 600)
WIDTH, HEIGHT = 200, 200
COLOUR_ALIVE, COLOUR_DEAD = (0, 0, 0), (255, 255, 255)


pygame.init()
window = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Conway's game of life")
cell_width = SCREEN_SIZE[1] // WIDTH
cell_height = SCREEN_SIZE[0] // HEIGHT


class Cell:
    def __init__(self, alive, index_1, index_2):
        self.alive = alive
        self.inx_1 = index_1
        self.inx_2 = index_2

        self.neighbours = []
        self.total = 0

    def find_neighbours(self):
        for y in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= self.inx_1 + y < HEIGHT and 0 <= self.inx_2 + j < WIDTH:
                        if cells[self.inx_1 + y][self.inx_2 + j] != self:
                            self.neighbours.append(cells[self.inx_1 + y][self.inx_2 + j])

    def update_total(self):
        self.total = 0
        for i in self.neighbours:
            if i.alive:
                self.total += 1

    def update_state(self):
        if self.alive and not 2 <= self.total <= 3:
            self.alive = False
        elif not self.alive and self.total == 3:
            self.alive = True


def update_cells():
    for i in cells:
        for x in i:
            x.update_total()

    for i in cells:
        for x in i:
            x.update_state()


def draw_cells():
    window.fill(COLOUR_DEAD)

    for i, x in enumerate(cells):
        for j, k in enumerate(x):
            if k.alive:
                pygame.draw.rect(window, COLOUR_ALIVE, (j * cell_width, i * cell_height, cell_width, cell_height))
            
    pygame.display.update()


def create_cells():
    global cells

    cells = [[Cell(False, x, i) for i in range(WIDTH)] for x in range(HEIGHT)]
    for i in range(HEIGHT // 2 - (HEIGHT // 3), HEIGHT // 2 + (HEIGHT // 3)):
        for x in range(WIDTH // 2 - (WIDTH // 3), WIDTH // 2 + (WIDTH // 3)):
            alive = not randint(0, 1)
            cells[i][x].alive = alive

create_cells()

for i in cells:
    for x in i:
        x.find_neighbours()


clock = pygame.time.Clock()
while True:
    clock.tick(10)
    update_cells()
    draw_cells()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()