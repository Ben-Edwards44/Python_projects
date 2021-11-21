import time

grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def main():
    #reset grid
    grid.clear()
    for i in range(0, 3):
        grid.append([])
        for x in range(0, 3):
            grid[i].append(0)

    mode = input("Mode (easy/medium/impossible): ")

    print("    1 [ ] [ ] [ ]")
    print("y:  2 [ ] [ ] [ ]")
    print("    3 [ ] [ ] [ ] ")
    print("x:     1   2   3")
    time.sleep(.5)
    print("")
    print("")

    if mode == "impossible":
        check_input(True, False)
    elif mode == "easy":
        check_input(False, False)
    elif mode == "medium":
        check_input(True, True)
    else:
        print("select valid mode")
        main()

def check_win(impossible, medium):
    won = False

    #horizontals
    if grid[0] == [1,1,1]:
        print("X wins!")
        won = True
    if grid[0] == [2,2,2]:
        print("O wins!")
        won = True
        if impossible and medium == False:
            time.sleep(.5)
            print("You better tell me how you did that...")

    if grid[1] == [1,1,1]:
        print("X wins!")
        won = True
    if grid[1] == [2,2,2]:
        print("O wins!")
        won = True
        if impossible and medium == False:
            time.sleep(.5)
            print("You better tell me how you did that...")

    if grid[2] == [1,1,1]:
        print("X wins!")
        won = True
    if grid[2] == [2,2,2]:
        print("O wins!")
        won = True
        if impossible and medium == False:
            time.sleep(.5)
            print("You better tell me how you did that...")

    #verticals
    if grid[0][0] == 1 and grid[1][0] == 1 and grid[2][0] == 1:
        print("X wins!")
        won = True
    if grid[0][0] == 2 and grid[1][0] == 2 and grid[2][0] == 2:
        print("O wins!")
        won = True
        if impossible and medium == False:
            time.sleep(.5)
            print("But...")
            time.sleep(.5)
            print("How?!")
            print("You were not supposed to do that...")

    if grid[0][1] == 1 and grid[1][1] == 1 and grid[2][1] == 1:
        print("X wins!")
        won = True
    if grid[0][1] == 2 and grid[1][1] == 2 and grid[2][1] == 2:
        print("O wins!")
        won = True
        if impossible and medium == False:
            print("But...")
            time.sleep(.5)
            print("How?!")
            print("You were not supposed to do that...")

    if(grid[0][2] == 1 and grid[1][2] == 1 and grid[2][2] == 1):
        print("X wins!")
        won = True
    if(grid[0][2] == 2 and grid[1][2] == 2 and grid[2][2] == 2):
        print("O wins!")
        won = True
        if impossible and medium == False:
            print("But...")
            time.sleep(.5)
            print("How?!")
            print("You were not supposed to do that...")

    #diagonals
    if grid[0][0] == 1 and grid[1][1] == 1 and grid[2][2] == 1:
        print("X wins!")
        won = True
    if grid[0][0] == 2 and grid[1][1] == 2 and grid[2][2] == 2:
        print("O wins!")
        won = True
        if impossible and medium == False:
            time.sleep(.5)
            print("I don't know how you did that...")

    if grid[0][2] == 1 and grid[1][1] == 1 and grid[2][0] == 1:
        print("X wins!")
        won = True
    if grid[0][2] == 2 and grid[1][1] == 2 and grid[2][0] == 2:
        print("O wins!")
        won = True
        if impossible and medium == False:
            time.sleep(.5)
            print("I don't know how you did that...")

    if won == False:
        filled_spaces = 0

        for i in range(0, 3):
            for x in range(0, 3):
                if grid[i][x] != 0:
                    filled_spaces += 1

        if filled_spaces == 9:
            print("Draw")
            time.sleep(.25)
            print("nobody wins")
            filled_spaces == 21
            won = True
            again()
    else:
        again()

def check_input(impossible, medium):
    print("")

    x_coord = input("x coordinate: ")
    y_coord = input("y coordinate: ")

    try:
        x_coord = int(x_coord)
        y_coord = int(y_coord)
    except ValueError:
        print("")
        print("Try again")
        check_input(impossible, medium)

    if x_coord > 3 or y_coord > 3:
        print("square out of range")
        print("")
        check_input(impossible, medium)
    
    if grid[y_coord - 1][x_coord - 1] == 0:
        grid[y_coord - 1][x_coord - 1] = 2
    else:
        print("that square is already taken")
        print("")
        check_input(impossible, medium)

    print_grid(True, grid[0][0], grid[0][1], grid[0][2], False, impossible, medium)
    print_grid(True, grid[1][0], grid[1][1], grid[1][2], False, impossible, medium)
    print_grid(True, grid[2][0], grid[2][1], grid[2][2], True, impossible, medium)
    check_win(impossible, medium)

def comp_move(impossible, medium):
    time.sleep(1.25)

    moved = False

    #get win horizontal
    if moved == False:
        if grid[0].count(1) == 2:
            for i in range(0, 3):
                if grid[0][i] == 0:
                    grid[0][i] = 1
                    moved = True

        if grid[1].count(1) == 2:
            for i in range(0, 3):
                if grid[1][i] == 0:
                    grid[1][i] = 1
                    moved = True

        if grid[2].count(1) == 2:
            for i in range(0, 3):
                if grid[2][i] == 0:
                    grid[2][i] = 1
                    moved = True

    #get win vertical
    if moved == False:
        if grid[0][0] == 1 and grid[1][0] == 1:
            if grid[2][0] == 0:
                grid[2][0] = 1
                moved = True
        if grid[0][0] == 1 and grid[2][0] == 1:
            if grid[1][0] == 0:
                grid[1][0] = 1
                moved = True
        if grid[1][0] == 1 and grid[2][0] == 1:
            if grid[0][0] == 0:
                grid[0][0] = 1
                moved = True

        if grid[0][1] == 1 and grid[1][1] == 1:
            if grid[2][1] == 0:
                grid[2][1] = 1
                moved = True
        if grid[0][1] == 1 and grid[2][1] == 1:
            if grid[1][1] == 0:
                grid[1][1] = 1
                moved = True
        if grid[1][1] == 1 and grid[2][1] == 1:
            if grid[0][1] == 0:
                grid[0][1] = 1
                moved = True

        if grid[0][2] == 1 and grid[1][2] == 1:
            if grid[2][2] == 0:
                grid[2][2] = 1
                moved = True
        if grid[0][2] == 1 and grid[2][2] == 1:
            if grid[1][2] == 0:
                grid[1][2] = 1
                moved = True
        if grid[1][2] == 1 and grid[2][2] == 1:
            if grid[0][2] == 0:
                grid[0][2] = 1
                moved = True

    #get win diagonal
    if moved == False:
        if grid[0][0] == 1 and grid[1][1] == 1:
            if grid[2][2] == 0:
                grid[2][2] = 1
                moved = True
        if grid[0][0] == 1 and grid[2][2] == 1:
            if grid[1][1] == 0:
                grid[1][1] = 1
                moved = True
        if grid[2][2] == 1 and grid[1][1] == 1:
            if grid[0][0] == 0:
                grid[0][0] = 1
                moved = True

        if grid[0][2] == 1 and grid[1][1] == 1:
            if grid[2][0] == 0:
                grid[2][0] = 1
                moved = True
        if grid[0][2] == 1 and grid[2][0] == 1:
            if grid[1][1] == 0:
                grid[1][1] = 1
                moved = True
        if grid[2][0] == 1 and grid[1][1] == 1:
            if grid[0][2] == 0:
                grid[0][2] = 1
                moved = True

    #defend loss horizontal
    if moved == False:
        if grid[0].count(2) == 2:
            for i in range(0, 3):
                if grid[0][i] == 0:
                    grid[0][i] = 1
                    moved = True

        if grid[1].count(2) == 2:
            for i in range(0, 3):
                if grid[1][i] == 0:
                    grid[1][i] = 1
                    moved = True

        if grid[2].count(2) == 2:
            for i in range(0, 3):
                if grid[2][i] == 0:
                    grid[2][i] = 1
                    moved = True

    #defend loss vertical
    if moved == False:
        if grid[0][0] == 2 and grid[1][0] == 2:
            if grid[2][0] == 0:
                grid[2][0] = 1
                moved = True
        if grid[0][0] == 2 and grid[2][0] == 2:
            if grid[1][0] == 0:
                grid[1][0] = 1
                moved = True
        if grid[1][0] == 2 and grid[2][0] == 2:
            if grid[0][0] == 0:
                grid[0][0] = 1
                moved = True

        if grid[0][1] == 2 and grid[1][1] == 2:
            if grid[2][1] == 0:
                grid[2][1] = 1
                moved = True
        if grid[0][1] == 2 and grid[2][1] == 2:
            if grid[1][1] == 0:
                grid[1][1] = 1
                moved = True
        if grid[1][1] == 2 and grid[2][1] == 2:
            if grid[0][1] == 0:
                grid[0][1] = 1
                moved = True

        if grid[0][2] == 2 and grid[1][2] == 2:
            if grid[2][2] == 0:
                grid[2][2] = 1
                moved = True
        if grid[0][2] == 2 and grid[2][2] == 2:
            if grid[1][2] == 0:
                grid[1][2] = 1
                moved = True
        if grid[1][2] == 2 and grid[2][2] == 2:
            if grid[0][2] == 0:
                grid[0][2] = 1
                moved = True

    #defend loss diagonal
    if moved == False:
        if grid[0][0] == 2 and grid[1][1] == 2:
            if grid[2][2] == 0:
                grid[2][2] = 1
                moved = True
        if grid[0][0] == 2 and grid[2][2] == 2:
            if grid[1][1] == 0:
                grid[1][1] = 1
                moved = True
        if grid[2][2] == 2 and grid[1][1] == 2:
            if grid[0][0] == 0:
                grid[0][0] = 1
                moved = True

        if grid[0][2] == 2 and grid[1][1] == 2:
            if grid[2][0] == 0:
                grid[2][0] = 1
                moved = True
        if grid[0][2] == 2 and grid[2][0] == 2:
            if grid[1][1] == 0:
                grid[1][1] = 1
                moved = True
        if grid[2][0] == 2 and grid[1][1] == 2:
            if grid[0][2] == 0:
                grid[0][2] = 1
                moved = True

    #if player move 1 is not in the center
    if moved == False and impossible:
        if grid[0].count(2) + grid[1].count(2) + grid[2].count(2) == 1 and grid[1][1] == 0:
            grid[1][1] = 1
            moved = True

    if moved == False and impossible == False:
        if grid[0].count(2) + grid[1].count(2) + grid[2].count(2) == 1 and grid[1][1] == 0:
            if grid[0][0] == 0:
                grid[0][0] = 1
                moved = True
            else:
                grid[0][2] = 1
                moved = True

    #if player move 1 is in the center
    if moved == False and impossible:
        if grid[0].count(2) + grid[1].count(2) + grid[2].count(2) == 1 and grid[1][1] == 2:
            grid[2][0] = 1
            moved = True

    if moved == False and impossible == False:
        if grid[0].count(2) + grid[1].count(2) + grid[2].count(2) == 1 and grid[1][1] == 2:
            grid[0][1] = 1
            moved = True

    #impossible sorting out that one time where you can beat it
    if grid[2][1] == 2 and grid[1][2] == 2 and moved == False and impossible:
        if grid[2][0] == 0:
            grid[2][0] = 1
            moved = True
    if grid[1][0] == 2 and grid[0][1] == 2 and moved == False and impossible:
        if grid[2][0] == 0:
            grid[2][0] = 1
            moved = True
    if grid[1][0] == 2 and grid[2][1] == 2 and moved == False and impossible:
        if grid[2][0] == 0:
            grid[2][0] = 1
            moved = True
    if grid[1][2] == 2 and grid[0][1] == 2 and moved == False and impossible:
        if grid[2][0] == 0:
            grid[2][0] = 1
            moved = True

    #sorting out another time where you can beat it on impossible
    if grid[0][2] == 2 and grid[1][1] == 2 and impossible and moved == False:
        if grid[2][2] == 0:
            grid[2][2] = 1
            moved = True

    #move to edge if nowhere else is free on easy and impossible
    if medium == False:
        if moved == False:
            if grid[0][1] == 0:
                grid[0][1] = 1
                moved = True
        if moved == False:
            if grid[1][0] == 0:
                grid[1][0] = 1
                moved = True
        if moved == False:
            if grid[1][2] == 0:
                grid[1][2] = 1
                moved = True
        if moved == False:
            if grid[2][1] == 0:
                grid[2][1] = 1
                moved = True

    #check if moved, if not move somewhere free
    if moved:
        print_grid(False, grid[0][0], grid[0][1], grid[0][2], False, impossible, medium)
        print_grid(False, grid[1][0], grid[1][1], grid[1][2], False, impossible, medium)
        print_grid(False, grid[2][0], grid[2][1], grid[2][2], True, impossible, medium)
        check_win(impossible, medium)
        check_input(impossible, medium)
    else:
        for i in range(0, 3):
            for x in range(0, 3):
                if grid[i][x] == 0:
                    #if grid[i + 1][x] == 2 or grid[i][x + 1] == 2:
                    grid[i][x] = 1
                    moved = True
                    print_grid(False, grid[0][0], grid[0][1], grid[0][2], False, impossible, medium)
                    print_grid(False, grid[1][0], grid[1][1], grid[1][2], False, impossible, medium)
                    print_grid(False, grid[2][0], grid[2][1], grid[2][2], True, impossible, medium)
                    check_input(impossible, medium)

def print_grid(from_input, n1, n2, n3, done, impossible, medium):

    if n1 == 0:
        n1 = "[ ]"
    if n1 == 1:
        n1 = "[X]"
    if n1 == 2:
        n1 = "[O]"

    if n2 == 0:
        n2 = "[ ]"
    if n2 == 1:
        n2 = "[X]"
    if n2 == 2:
        n2 = "[O]"

    if n3 == 0:
        n3 = "[ ]"
    if n3 == 1:
        n3 = "[X]"
    if n3 == 2:
        n3 = "[O]"

    print(n1, n2, n3)

    if from_input and done:
        check_win(impossible, medium)
        print("")
        print("")
        print("")
        comp_move(impossible, medium)

def again():
    print("")

    i = input("Again? (y/n) ")

    if i == "y" or i == "yes" or i == "Y":
        print(" ")
        main()
    else:
        quit()

if __name__ == "__main__":
    main()