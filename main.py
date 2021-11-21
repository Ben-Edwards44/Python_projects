import noughtscrosses2 as two_player
import noughtscrossescomputer as computer

def main():
    player_input = input("2 player or play against computer? (2p/c) ")

    if player_input == "2p" or player_input == "2 player":
        two_player.main()
    elif player_input == "c" or player_input == "computer":
        mode = input("Which difficulty level? (easy/impossible) ")

        if mode == "easy" or mode == "e":
            computer.main(False)
        elif mode == "impossible" or mode == "i":
            computer.main(True)
        else:
            print("Enter valid mode")
            print("")
            main()
    else:
        print("Enter valid mode")
        print("")
        main()


if __name__ == "__main__":
    main()