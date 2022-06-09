import os


def startup():
    if OS_NAME == "nt":
        os.system("cls")
    elif OS_NAME == "posix":
        os.system("clear")

    os.chdir(prev_directory)

    print("-" * 88)
    print(" ______                __             __                           __                __")
    print("|   __ \.-----..-----.|  |.-----.    |  |_ .-----..----..--------.|__|.-----..---.-.|  |")
    print("|   __ <|  -__||     | |_||__ --|    |   _||  -__||   _||        ||  ||     ||  _  ||  |")
    print("|______/|_____||__|__|    |_____|    |____||_____||__|  |__|__|__||__||__|__||___._||__|\n")
    print("-" * 88)


def check_alias(command):
    if command in ALIAS:
        return ALIAS[command]


def display_path():
    cwd = os.getcwd()
    print(f"\033[92m{cwd}\033[0m")


def get_command():
    global prev_directory

    command = input("> ")
    alias = check_alias(command)

    if alias != None:
        command = alias

        if type(command) != str:
            command()
            return

    if command[:2] == "cd" and len(command) > 3:
        if command[-1] == "-":
            os.chdir(prev_directory)
        elif not os.system(command):
            prev_directory = os.getcwd()
            os.chdir(f"{os.getcwd()}{seperator}{command[3:]}")
    elif command == "exit":
        quit()
    else:
        print("\033[96m")
        os.system(command)
        print("\033[96m")


def main():
    while True:
        display_path()
        get_command()


ALIAS = {"startup" : startup}
OS_NAME = os.name


if OS_NAME == "nt":
    prev_directory = "C:\\Users"
    seperator = "\\"
elif OS_NAME == "posix":
    prev_directory = "/home"
    seperator = "/"


startup()
main()