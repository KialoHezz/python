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

def print_maze(maze, stdscr, path=[]):
    # DRAW MAZE AS BLUE
    BLUE = curses.color_pair(1)
    # THE PATH AS RED
    RED = curses.color_pair(2)

    # LOOP THROUGH
    #  i => it's row while j => it's row
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            stdscr.addstr(i, j*2, value, BLUE)




# dfn function
# parameter stdscr(standard output screen)
def main(stdscr):
    # init color
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)


    # # USE THE COLOR 
    # blue_and_black = curses.color_pair(1)

    stdscr.clear()
    # row & column 0, 0 => top-left-corner = 0 
    # pass the text show on the screen
    print_maze(maze, stdscr)
    stdscr.refresh()
    # allow user to hit sthg
    stdscr.getch()
    
wrapper(main)
