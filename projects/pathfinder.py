# use package called curses, curses => used to control the terminal and colored in the way that you saw and actuall override the current in terminal 
# Linux $ MAC is already installed, therefore, this command for windows guys want to install curses => pip install windows-curses

# nested loop
#  O => start
#  X => end
#  "#" => Obstance
#  " " => where we can Navigate
import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "#", "#", "#", "#", "O", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

# dfn function
# parameter stdscr(standard output screen)
def main(stdscr):
    # init color
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    # USE THE COLOR 
    blue_and_black = curses.color_pair(1)
    stdscr.clear()
    # row & column 0, 0 => top-left-corner = 0 
    # pass the text show on the screen
    stdscr.addstr(0, 0, "hello world", blue_and_black)
    stdscr.refresh()
    # allow user to hit sthg
    stdscr.getch()
    
wrapper(main)
