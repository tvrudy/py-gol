#!/usr/bin/python3

""" Conway's Game of Life Implementation in Python 3.12 """

# Created: 6/16/2024, 8:10 PM IST 

import os
import time as T
from sys import argv

def console_clear() -> None | OSError:
    os.system("clear")

class Board:
    
    GOLBoard:[[str]] = []
    new_Board:[[str]] = []

    ROWS = 0
    COLUMNS = 0

    # Ticks Per Second
    TPS = 30
    GENERATIONS = 200

    def __init__(self, board: [[str]], rows: int, column: int) -> None:

        self.ROWS = rows
        self.COLUMNS = column
        self.GOLBoard = board
        self.new_Board = [["."]*self.COLUMNS for _ in range(self.ROWS)]

    def get_nebr(self, row_0: int, col_0: int) -> int:
        nebr: int = 0
        row: int = 0
        col: int = 0

        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if (dr != 0 or dc != 0):
                    row = (row_0 + dr) % self.ROWS
                    col = (col_0 + dc) % self.COLUMNS
        
                    if (self.GOLBoard[row][col] == "#"):
                        nebr += 1

        return nebr

    def next_gen(self, gen: int) -> None:
        N: int = 0

        for r in range(self.ROWS):
            for c in range(self.COLUMNS):
                N = self.get_nebr(r, c)                
                if (N < 2 or N > 3):
                    self.new_Board[r][c] = "."
                elif (N == 3 and self.GOLBoard[r][c] == "."):
                    self.new_Board[r][c] = "#"
                else:
                    self.new_Board[r][c] = self.GOLBoard[r][c]
            
        self.GOLBoard, self.new_Board = self.new_Board, self.GOLBoard
        self.render_board(gen)

    def render_board(self, gen: int) -> None:
        console_clear()

        print(f"---- {gen} Gen ----")
        for r in range(self.ROWS):
            for c in range(self.COLUMNS):
                print(self.GOLBoard[r][c], end=' ')
            print()
        

# Seed Configuration
b: [[str]] = [
    ['.', '.', '#', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
]

B = Board(b, len(b), len(b[0]))

# Set TPS and GENERATIONS via cmdline args
if (len(argv) == 3):
    B.TPS = int(argv[1])
    B.GENERATIONS = int(argv[2])
elif (len(argv) == 2):
    B.TPS = int(argv[1])

for g in range(1, B.GENERATIONS + 1):
    B.next_gen(g)
    T.sleep(1 / B.TPS)
