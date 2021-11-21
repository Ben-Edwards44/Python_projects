import main as m

class grid:
    def __init__(self):
        self.turns = 0

        self.board = [[] for i in range(0, 3)]
        for i in range(0, 3):
            self.board[i] = [0 for j in range(0, 3)]

        self.converted_board = [[] for i in range(0, 3)]
        for i in range(0, 3):
            self.converted_board[i] = [0 for j in range(0, 3)]

    def take_input(self):
        print("")

        if self.turns % 2 == 0:
            print("X to move")
            self.turn = 1
        else:
            print("O to move")
            self.turn = 2

        try:
            player_input_x = int(input("Enter x coordinate: "))
            player_input_y = int(input("enter y coordinate: "))
        except ValueError:
            print("Please use valid coordinates")
            self.take_input()

        if -1 < player_input_x < 3 and -1 < player_input_y < 3 and self.board[player_input_y][player_input_x] == 0:
            self.board[player_input_y][player_input_x] = self.turn
        else:
            print("Choose a different square")
            self.take_input()

        self.turns += 1
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
            print("It is a draw!")
            retry(self)
        else:
            self.take_input()

    def print_board(self):
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


def main():
    print("")
    print("    0 [ ] [ ] [ ]")
    print("y:  1 [ ] [ ] [ ]")
    print("    2 [ ] [ ] [ ] ")
    print("x:     0   1   2")
    print("")

    my_grid = grid()
    my_grid.take_input()


def retry(grid_object):
    print("")
    player_input = input("Again? (y/n) ")

    if player_input == "y" or player_input == "Y" or player_input == "yes":
        del grid_object
        print("")
        m.main()
    else:
        quit()