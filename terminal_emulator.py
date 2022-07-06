#Author: Ben-Edwards44


import os
import curses
import psutil
from platform import uname


SEPERATOR = "\\"
SPECIAL_COMMANDS = ("vim ", "nano ")
OS_NAMES = {"nt" : "windows", "posix" : "linux"}

stored_directory = os.getcwd()
prev_commands = []
prev_directory = "/users/benje"


def startup(stdscr):
    init_curses()

    os.chdir(prev_directory)

    stdscr.addstr("-" * 88)
    stdscr.addstr("\n ______                __             __                           __                __")
    stdscr.addstr("\n|   __ \.-----..-----.|  |.-----.    |  |_ .-----..----..--------.|__|.-----..---.-.|  |")
    stdscr.addstr("\n|   __ <|  -__||     | |_||__ --|    |   _||  -__||   _||        ||  ||     ||  _  ||  |")
    stdscr.addstr("\n|______/|_____||__|__|    |_____|    |____||_____||__|  |__|__|__||__||__|__||___._||__|\n")
    stdscr.addstr("-" * 88)
    stdscr.addstr("\n")
    
    display_info(stdscr)
    display_path(stdscr)
    main(stdscr)


def init_curses():
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)


def display_info(stdscr):
    def get_size(bytes):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}B"

            bytes /= factor

    stdscr.addstr("CPU: ", curses.color_pair(2))
    stdscr.addstr(f"{uname().processor}\n")
    stdscr.addstr("Cores: ", curses.color_pair(2))
    stdscr.addstr(f"{psutil.cpu_count(True)}\n")
    stdscr.addstr("Usage: ", curses.color_pair(2))
    stdscr.addstr(f"{psutil.cpu_percent()}%\n\n")

    stdscr.addstr("Memory: ", curses.color_pair(2))
    stdscr.addstr(f"{get_size(psutil.virtual_memory().used)} / {get_size(psutil.virtual_memory().total)}\n\n")

    network_info = psutil.net_if_addrs()

    if "WiFi" in network_info:
        stdscr.addstr("IP address: ", curses.color_pair(2))
        stdscr.addstr(f"{network_info['WiFi'][1][1]}\n\n")
    elif "wlan0" in network_info:
        stdscr.addstr("IPv4 address: ", curses.color_pair(2))
        stdscr.addstr(f"{network_info['wlan0'][0][1]}\n")
        stdscr.addstr("IPv6 address: ", curses.color_pair(2))
        stdscr.addstr(f"{network_info['wlan0'][1][1]}\n\n")


def display_path(stdscr):
    stdscr.addstr(f"{os.getlogin()}@{OS_NAMES[os.name]}:", curses.color_pair(1))
    stdscr.addstr(os.getcwd(), curses.color_pair(2))
    stdscr.addstr("\n> ", curses.color_pair(3))


def auto_complete(command):
    og_dir = os.getcwd()
    os.chdir(stored_directory)

    with open("commands.txt", "r") as file:
        raw_data = file.read()

    os.chdir(og_dir)

    commands = raw_data.split("\n")

    for i in commands:
        if i.startswith(command):
            return i

    return False


def display_completion(stdscr, command):
    possible = auto_complete(command)

    if possible and len(command) > 0:
        y, x = stdscr.getyx()
        stdscr.addstr(possible[len(command):], curses.color_pair(4))
        stdscr.move(y, x)


def get_command(stdscr):
    global prev_commands

    command = ""
    cmd_num = 0

    while command[-1:] != "\n":
        key = stdscr.getkey()

        if key == "\b" or key == "KEY_BACKSPACE":
            command = command[:-1]
        elif key == "KEY_UP":
            cmd_num += 1

            if cmd_num > len(prev_commands):
                cmd_num = len(prev_commands)

            if len(prev_commands) > 0:
                command = prev_commands[-cmd_num]
        elif key == "KEY_DOWN":
            cmd_num -= 1

            if cmd_num < 1:
                cmd_num = 1

            if len(prev_commands) > 0:
                command = prev_commands[-cmd_num]
        elif key == "\t":
            command = auto_complete(command)
        else:
            command = f"{command}{key}"

        clear_line(stdscr)
        stdscr.addstr(command)
        display_completion(stdscr, command)
        stdscr.refresh()
        check_size(stdscr)

    prev_commands.append(command[:-1])
    return command[:-1]


def clear_line(stdscr):
    y, x = stdscr.getyx()
    stdscr.move(y, 2)
    stdscr.clrtoeol()


def check_size(stdscr):
    height, width = stdscr.getmaxyx()
    y, x = stdscr.getyx()

    if y >= height - 5:
        stdscr.clear()
    if x >= width - 5:
        curses.resize_term(height, width + 5)

    while len(prev_commands) > 25:
        prev_commands.pop(0)


def execute_command(stdscr, command):
    global prev_directory

    if command[:2] == "cd":
        if command[-1] == "-":
            os.chdir(prev_directory)
        elif len(command) <= 3:
            os.chdir("/home")
            prev_directory = os.getcwd()
        elif not os.system(command):
            prev_directory = os.getcwd()
            os.chdir(f"{os.getcwd()}{SEPERATOR}{command[3:]}")
    elif any(i in command for i in SPECIAL_COMMANDS):
        curses.endwin()
        os.system(command)
    else:
        output = os.popen(command)

        done = False
        while not done:
            try:
                stdscr.addstr(f"{output.read()}", curses.color_pair(3))
                done = True
            except Exception:
                y, x = stdscr.getmaxyx()
                curses.resize_term(y + 1, x)


def main(stdscr):
    command = ""
    while command != "exit":
        command = get_command(stdscr)
        execute_command(stdscr, command)
        display_path(stdscr)
        stdscr.refresh()


curses.wrapper(startup)
