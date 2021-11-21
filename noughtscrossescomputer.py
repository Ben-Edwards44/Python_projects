import main as m
import time


wait_time = 0.75


class grid:
    def __init__(self, impossible):
        self.impossible = impossible
        self.turns = 0

        self.converted_board = [[] for i in range(0, 3)]
        for i in range(0, 3):
            self.converted_board[i] = [0 for j in range(0, 3)]

        self.board = [[] for i in range(0, 3)]
        for i in range(0, 3):
            self.board[i] = [0 for j in range(0, 3)]

    def player_input(self):
        try:
            input_x = int(input("Enter x coordinate: "))
            input_y = int(input("Enter y coordinate: "))
        except ValueError:
            print("Enter valid coordinates")
            print("")
            self.player_input()

        if -1 < input_x < 3 and -1 < input_y < 3 and self.board[input_y][input_x] == 0:
            self.board[input_y][input_x] = 1
        else:
            print("Choose different square")
            print("")
            self.player_input()

        self.print_board()

    def check_win(self):
        #checks wins horizontally
        for i in range(0, 3):
            row = [j for j in self.board[i]]

            if row[0] == row[1] and row[1] == row[2] and row[0] != 0:
                if row[0] == 1:
                    print("X wins!")
                else:
                    print("O wins!")

                retry(self)

        #checks wins vertically
        for i in range(0, 3):
            column = [self.board[j][i] for j in range(0, 3)]
            
            if column[0] == column[1] and column[1] == column[2] and column[0] != 0:
                if column[0] == 1:
                    print("X wins!")
                else:
                    print("O wins!")

                retry(self)

        #checks wins diagonally
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            if self.board[0][0] == 1:
                print("X wins!")
            else:
                print("O wins!")

            retry(self)

        if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2] and self.board[2][0] != 0:
            if self.board[2][0] == 1:
                print("X wins!")
            else:
                print("O wins!")

            retry(self)

        #checks for a draw
        zero_count = 0
        for i in self.board:
            if i.count(0) != 0:
                zero_count += 1
    
        if zero_count == 0:
            print("It's a draw!")
            retry(self)
        else:
            if self.turns % 2 == 0:
                self.player_input()
            else:
                self.calculate_comp_move()

    def calculate_comp_move(self):
        time.sleep(wait_time)

        #checks to see anyone has 2 in a row
        num = [2, 1]
        for t in num:
            #horizontal
            for i in range(0, 3):
                row = [j for j in self.board[i]]
                if row.count(t) == 2:
                    for x in row:
                        self.index_of_x = row.index(x)
                        if x == 0:
                            self.board[i][self.index_of_x] = 2
                            self.print_board()

            #vertical
            for i in range(0, 3):
                column = [self.board[j][i] for j in range(0, 3)]
                if column.count(t) == 2:
                    for x in column:
                        if x == 0:
                            col_index = column.index(x)
                            self.board[col_index][i] = 2
                            self.print_board()

            #diagonal
            diagonal1 = [self.board[i][i] for i in range(0, 3)]
            diagonal2 = [self.board[0][2], self.board[1][1], self.board[2][0]]
            if diagonal1.count(t) == 2:
                for i in range(0, 3):
                    if diagonal1[i] == 0:
                        inx = diagonal1.index(diagonal1[i])
                        self.board[inx][inx] = 2
                        self.print_board()

            if diagonal2.count(t) == 2:
                for i in range(0, 3):
                    if diagonal2[i] == 0:
                        if i == 0:
                            self.board[0][2] = 2
                        if i == 2:
                            self.board[2][0] = 2
                        if i == 1:
                            self.board[1][1] = 2
                        self.print_board()

        #first turn
        count_1 = 0
        for i in range(0, 3):
            for x in range(0, 3):
                if self.board[i][x] == 1:
                    count_1 += 1
                    inx1 = i
                    inx2 = x

        if count_1 == 1:
            if inx1 == 1 and inx2 == 1:
                #if player moves in the center
                self.board[2][0] = 2
                self.print_board()
            elif inx1 == inx2 or abs(inx1 - inx2) == 2:
                #if player move in the corner
                self.board[1][1] = 2
                self.print_board()
            else:
                #if player moves to an edge
                if inx1 == 0 or inx2 == 2:
                    self.board[0][2] = 2
                    self.print_board()
                elif inx1 == 2 or inx2 == 0:
                    self.board[2][0] = 2
                    self.print_board()

        if self.impossible:
            #makes it impossible to win against impossible mode
            if self.board[0][2] == 1 and self.board[2][0] == 1 and self.board[0][1] == 0:
                self.board[0][1] = 2
                self.print_board()

            if (self.board[0][1] == 1 or self.board[2][1] == 1) and (self.board[1][0] == 1 or self.board[1][2]) and self.board[1][1] == 0:
                self.board[1][1] = 2
                self.print_board()

        #move to somewhere empty if haven't moved already
        for i in range(0, 3):
            for x in range(0, 3):
                if self.board[i][x] == 0:
                    self.board[i][x] = 2
                    self.print_board()

    def print_board(self):
        self.turns += 1
        print("")

        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == 0:
                    self.converted_board[i][j] = " "
                elif self.board[i][j] == 1:
                    self.converted_board[i][j] = "X"
                elif self.board[i][j] == 2:
                    self.converted_board[i][j] = "O"

        for i in range(0, 3):
            print(self.converted_board[i])

        self.check_win()


def main(impossible):
    print("")
    print("    0 [ ] [ ] [ ]")
    print("y:  1 [ ] [ ] [ ]")
    print("    2 [ ] [ ] [ ] ")
    print("x:     0   1   2")
    print("")

    my_grid = grid(impossible)
    my_grid.player_input()


def retry(grid_object):
    print("")
    player_input = input("Again? (y/n) ")

    if player_input == "y" or player_input == "Y" or player_input == "yes":
        del grid_object
        print("")
        m.main()
    else:
        quit()