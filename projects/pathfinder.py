# use package called curses, curses => used to control the terminal and colored in the way that you saw and actuall override the current in terminal 

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
    stdscr.clear()
    # row & column 0, 0 => top-left-corner = 0 
    # pass the text show on the screen
    stdscr.addstr(0, 0, "hello world")
    stdscr.refresh()
    # allow user to hit sthg
    stdscr.getch()
    
wrapper(main)
