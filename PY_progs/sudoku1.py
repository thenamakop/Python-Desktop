import tkinter as tk
import random


class SudokuGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku")
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.cells = [
            [
                tk.Entry(self.frame, width=2, font=("Arial", 18), justify="center")
                for _ in range(9)
            ]
            for _ in range(9)
        ]
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                cell.grid(row=i, column=j)
        self.generate_puzzle()

    def generate_puzzle(self):
        puzzle = self.create_sudoku_puzzle()
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] != 0:
                    self.cells[i][j].insert(0, puzzle[i][j])
                    self.cells[i][j].config(state="disabled")

    def create_sudoku_puzzle(self):
        # Simplified puzzle generation logic
        base = 3
        side = base * base

        def pattern(r, c):
            return (base * (r % base) + r // base + c) % side

        def shuffle(s):
            return random.sample(s, len(s))

        rBase = range(base)
        rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums = shuffle(range(1, base * base + 1))
        board = [[nums[pattern(r, c)] for c in cols] for r in rows]

        # Remove elements to create the puzzle
        squares = side * side
        no_of_clues = random.randint(20, 30)
        for _ in range(squares - no_of_clues):
            x, y = divmod(random.randint(0, squares - 1), side)
            board[x][y] = 0

        return board


if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()
