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
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
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
            if (i, j) in path:  
                stdscr.addstr(i, j*2, "X", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)


# find the co-ordinates
def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j 
    return None



def find_path(maze, stdscr):
    # dfn variables
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    # keep track of visited nodes
    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        # return that find the path
        if maze[row][col] == end:
            return path
        
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            # check if there is obstace
            if maze[r][c] == "#":
                continue


            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)
 

def find_neighbors(maze, row, col):
    neighbours = []

    if row > 0: #UPPER
        neighbours.append((row - 1, col))
    if row + 1 < len(maze): #Down 
        neighbours.append((row + 1, col))
    if col > 0: #LEFT 
        neighbours.append((row, col - 1))
    if col + 1 > len(maze[0]): #RIGHT
        neighbours.append((row, col + 1))
    
    return neighbours
        
# dfn function
# parameter stdscr(standard output screen)
def main(stdscr):
    # init color
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    # allow user to hit sthg
    stdscr.getch()
    
wrapper(main)

