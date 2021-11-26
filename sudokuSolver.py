#Author Ben-Edwards44


import pygame


screen_size = (630, 630)
visulise_steps = True

grid = [[] for i in range(9)]
for i in range(9):
    grid[i] = [0 for i in range(9)]


def main():
    #set up pygame
    global window

    pygame.init()
    window = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Sudoku Solver")
    window.fill((255, 255, 255))
    pygame.display.update()

    draw_grid()
    event_handeler()


def draw_grid():
    #draw background lines to make up the grid
    for i in range(1, 10):
        if i % 3 == 0:
            pygame.draw.rect(window, (0, 0, 0), [0, screen_size[0] // 9 * i, screen_size[0], 2])
            pygame.draw.rect(window, (0, 0, 0), [screen_size[0] // 9 * i, 0, 2, screen_size[0]])
        else:
            pygame.draw.rect(window, (0, 0, 0), [0, screen_size[0] // 9 * i, screen_size[0], 1])
            pygame.draw.rect(window, (0, 0, 0), [screen_size[0] // 9 * i, 0, 1, screen_size[0]])

    #draw lines around outside of grid
    pygame.draw.rect(window, (0, 0, 0), [0, 0, screen_size[0], 2])
    pygame.draw.rect(window, (0, 0, 0), [0, 0, 2, screen_size[0]])
    pygame.draw.rect(window, (0, 0, 0), [0, screen_size[0] - 2, screen_size[0], 2])
    pygame.draw.rect(window, (0, 0, 0), [screen_size[0] - 2, 0, 2, screen_size[0]])

    pygame.display.update()


def event_handeler():
    #check for user input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                show_steps()

            if keys[pygame.K_1]:
                input_nums(1)
            if keys[pygame.K_2]:
                input_nums(2)
            if keys[pygame.K_3]:
                input_nums(3)
            if keys[pygame.K_4]:
                input_nums(4)
            if keys[pygame.K_5]:
                input_nums(5)
            if keys[pygame.K_6]:
                input_nums(6)
            if keys[pygame.K_7]:
                input_nums(7)
            if keys[pygame.K_8]:
                input_nums(8)
            if keys[pygame.K_9]:
                input_nums(9)


def input_nums(num):
    #display numbers inputted by user
    global grid

    coords = pygame.mouse.get_pos()
    new_coords = [i // (screen_size[0] // 9) for i in coords]

    grid[new_coords[1]][new_coords[0]] = num

    display_num(str(num), new_coords)


def display_num(num, pos):
    #display numbers on the grid
    font = pygame.font.Font("freesansbold.ttf", 30)
    text = font.render(num, True, (0, 0, 0))
    surface = text.get_rect()
    surface.topleft = [pos[0] * (screen_size[0] // 9) + 28, pos[1] * (screen_size[0] // 9) + 28]

    pygame.draw.rect(window, (255, 255, 255), [pos[0] * (screen_size[0] // 9) + 2, pos[1] * (screen_size[0] // 9) + 2, screen_size[0] // 9 - 4, screen_size[0] // 9 - 4])
    if num != "0":
        window.blit(text, surface)
    pygame.display.update()


def display_result(result, done):
    for x in range(9):
        for i, y in enumerate(result[x]):
            display_num(str(y), [i, x])

    if done:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()


def show_steps():
    global visulise_steps

    #draw boxes for yes and no buttons
    pygame.draw.rect(window, (25, 25, 25), [100, 370, 100, 55])
    pygame.draw.rect(window, (25, 25, 25), [425, 370, 100, 55])
    pygame.draw.rect(window, (25, 25, 25), [160, 280, 310, 65])

    #set up text
    font = pygame.font.Font("freesansbold.ttf", 45)
    text = font.render("Show steps?", True, (255, 255, 255))
    surface = text.get_rect()
    surface.center = [screen_size[0] // 2, screen_size[0] // 2]

    font1 = pygame.font.Font("freesansbold.ttf", 45)
    text1 = font1.render("Yes", True, (255, 255, 255))
    surface1 = text1.get_rect()
    surface1.center = [150, 400]

    font2 = pygame.font.Font("freesansbold.ttf", 45)
    text2 = font2.render("No", True, (255, 255, 255))
    surface2 = text2.get_rect()
    surface2.center = [475, 400]

    #render text
    window.blit(text, surface)
    window.blit(text1, surface1)
    window.blit(text2, surface2)
    pygame.display.update()

    #check for user input
    selected = False
    while not selected:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                #yes button
                if 100 <= pos[0] <= 200 and 370 <= pos[1] <= 425:
                    selected = True
                    visulise_steps = True
                    my_solver = solver(grid)

                #no button
                elif 425 <= pos[0] <= 525 and 370 <= pos[1] <= 425:
                    selected = True
                    visulise_steps = False
                    my_solver = solver(grid)

            if event.type == pygame.QUIT:
                quit()


#solves the sudoku puzzle
class solver:
    def __init__(self, board):
        window.fill((255, 255, 255))
        draw_grid()
        display_result(board, False)

        self.board = board
        self.solved = False
        self.solve()

    def get_possible(self, x, y):
        nums = [i for i in range(1, 10)]

        #row
        for i in self.board[x]:
            if i in nums:
                nums.remove(i)

        #column
        for i in range(0, 9):
            if self.board[i][y] in nums:
                nums.remove(self.board[i][y])

        #box
        if 0 <= x <= 2:
            box_x = 1
        elif x <= 5:
            box_x = 4
        else:
            box_x = 7
        if 0 <= y <= 2:
            box_y = 1
        elif y <= 5:
            box_y = 4
        else:
            box_y = 7

        index_x = [i for i in range(box_x - 1, box_x + 2)]
        index_y = [i for i in range(box_y - 1, box_y + 2)]

        for i in index_x:
            for j in index_y:
                if self.board[i][j] in nums:
                    nums.remove(self.board[i][j])

        self.possible_nums = nums

    def solve(self):
        #use backtracking to solve sudoku puzzle
        for x in range(0, 9):
            for y in range(0, 9):
                if self.board[x][y] == 0:
                    for j in range(1, 10):
                        self.get_possible(x, y)
                        if j in self.possible_nums:
                            self.get_possible(x, y)
                            self.board[x][y] = j
                            if visulise_steps:
                                display_result(self.board, False)
                            self.solve()
                            self.board[x][y] = 0
                    return

        display_result(self.board, True)


if __name__ == "__main__":
    main()
