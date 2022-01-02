from sudoku_gui import Gui
from button import Button
import pygame, sys
import time


class Sudoku:

    def __init__(self):
        """ Initialise the sudoku grid, GUI class and some basic Suduko class variables """

        self.board = [
        [6, 0, 0, 5, 0, 0, 0, 0, 0],
        [3, 8, 0, 0, 0, 0, 6, 0, 2],
        [0, 1, 0, 0, 0, 8, 0, 9, 7],
        [8, 0, 1, 0, 6, 2, 3, 7, 4],
        [4, 0, 9, 7, 8, 5, 1, 0, 6],
        [7, 0, 2, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 5, 0, 0, 6, 3],
        [0, 7, 0, 0, 0, 0, 9, 0, 0],
        [1, 0, 0, 0, 9, 6, 0, 0, 0]
        ]

        self.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        # For prepping board
        self.r, self.c = 0, 0

        self.current_entry = ['', 0, 0]
        self.backtracked = False
        self.solved = False
        self.play = False

        self.gui = Gui()
        self.start()



    def start(self):
        self.gui.update_screen(self.board, self.current_entry, self.backtracked, self.solved)
        while True:
            event = self.gui.check_events(self.play)

            if event == 'play':
                self.play = True
                self.gui.update_screen(self.board, self.current_entry, self.backtracked, self.solved, clicked=True)
                time.sleep(0.1)
                self.run()
                return

            elif event:
                if event == 'zero':
                    number = 0
                else:
                    number = event
                self.prep_board(number)
                self.gui.update_screen(self.board, self.current_entry, self.backtracked, self.solved, clicked=False, cell_loc=self.cell_loc)
                

    def prep_board(self, number):
        if self.r == 9:
            return
        self.board[self.r][self.c] = number
        self.c += 1
        if self.c > 8:
            self.c = 0
            self.r += 1

        self.cell_loc = (self.r, self.c)



    def run(self):
        """ Main loop to run the program """
        self.solver()
        while True:
            self.current_entry = ['', 0, 0]
            self.gui.update_screen(self.board, self.current_entry, self.backtracked, self.solved)


    def split_sub_grids(self):
        """ Create a list which holds sublists containing the values in each sub-grid """

        self.sub_grids = []
        for col_n in range(3):
            for row_n in range(3):
                grid = []
                grid += self.board[(row_n*3)][col_n*3:(col_n*3)+3]
                grid += self.board[(row_n*3)+1][col_n*3:(col_n*3)+3]
                grid += self.board[(row_n*3)+2][col_n*3:(col_n*3)+3]
                self.sub_grids.append(grid)
        return self.sub_grids

    def find_unsolved_location(self):
        """ Finds and returns the next unsolved location on the board """

        for row_n, row in enumerate(self.board):
            for col_n, number in enumerate(row):
                if number == 0:
                    return [row_n, col_n]
        return None

    def valid_entries(self, row_n, col_n):
        """ Returns a list of the possible entries for a given square on the board """

        row = self.board[row_n]
        col = [self.board[y][col_n] for y in range(9)]

        sub_grids = self.split_sub_grids()
        sub_grid_x = col_n // 3
        sub_grid_y = row_n // 3
        index = 3*sub_grid_x + sub_grid_y
        sub_grid = sub_grids[index]
        
        invalid_values = row + col + sub_grid
        
        self.possible_entries = [n for n in range(1,10) if n not in invalid_values]

        return self.possible_entries

    def solver(self):
        """ Solves the suduko board using backtracking and recursion """

        self.gui.update_screen(self.board, self.current_entry, self.backtracked, self.solved)
        time.sleep(self.gui.screen_update_speed)

        self.backtracked = False
        zero_loc = self.find_unsolved_location()

        if not zero_loc:
            self.solved = True
            return True

        else:
            valid_entries = self.valid_entries(zero_loc[0], zero_loc[1])
            for entry in valid_entries:
                self.board[zero_loc[0]][zero_loc[1]] = entry
                self.current_entry = [entry, zero_loc[0], zero_loc[1]]

                if self.solver():
                    self.solved = True
                    return True

                self.board[zero_loc[0]][zero_loc[1]] = 0
                self.backtracked = True

        return False



suduko_game = Sudoku()



# Valid Solution
#[
#[5, 3, 4, 6, 7, 8, 9, 1, 2],
#[6, 7, 2, 1, 9, 5, 3, 4, 8],
#[1, 9, 8, 3, 4, 2, 5, 6, 7],
#[8, 5, 9, 7, 6, 1, 4, 2, 3],
#[4, 2, 6, 8, 5, 3, 7, 9, 1],
#[7, 1, 3, 9, 2, 4, 8, 5, 6],
#[9, 6, 1, 5, 3, 7, 2, 8, 4],
#[2, 8, 7, 4, 1, 9, 6, 3, 5],
#[3, 4, 5, 2, 8, 6, 1, 7, 9]
#]