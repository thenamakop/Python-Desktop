import tkinter as tk
import tkinter.messagebox as messagebox
import random


class SudokuGenerator:
    def _init_(self):
        self.solved_grid = self.generate_sudoku()
        self.puzzle_grid = self.remove_numbers(self.solved_grid)

    def generate_sudoku(self):
        """Generate a valid Sudoku grid using backtracking with diagonal initialization"""
        while True:
            grid = [[0 for _ in range(9)] for _ in range(9)]
            self.fill_diagonal_boxes(grid)
            if self.solve_sudoku(grid):
                return grid

    def fill_diagonal_boxes(self, grid):
        """Fill the three diagonal 3x3 boxes with random numbers"""
        for i in range(0, 9, 3):
            self.fill_box(grid, i, i)

    @staticmethod
    def fill_box(grid, row, col):
        """Fill a 3x3 box starting at (row, col) with random numbers 1-9"""
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        index = 0
        for i in range(3):
            for j in range(3):
                grid[row + i][col + j] = numbers[index]
                index += 1

    def solve_sudoku(self, grid):
        """Solve the Sudoku grid using backtracking with random number selection"""
        find = self.find_empty(grid)
        if not find:
            return True  # Puzzle solved
        row, col = find

        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for num in numbers:
            if self.is_valid(grid, row, col, num):
                grid[row][col] = num
                if self.solve_sudoku(grid):
                    return True
                grid[row][col] = 0  # Backtrack
        return False

    @staticmethod
    def find_empty(grid):
        """Find the next empty cell (0) in the grid"""
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i, j)
        return None

    @staticmethod
    def is_valid(grid, row, col, num):
        """Check if placing 'num' at (row, col) is valid"""
        # Check row
        if num in grid[row]:
            return False

        # Check column
        for i in range(9):
            if grid[i][col] == num:
                return False

        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if grid[box_row + i][box_col + j] == num:
                    return False
        return True

    @staticmethod
    def remove_numbers(grid, count=40):
        """Remove numbers from the solved grid to create the puzzle"""
        puzzle = [row.copy() for row in grid]
        cells = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(cells)

        removed = 0
        for i, j in cells:
            if removed >= count:
                break
            if puzzle[i][j] != 0:
                puzzle[i][j] = 0
                removed += 1
        return puzzle


class SudokuUI:
    def _init_(self, master):
        self.master = master
        self.master.title("Sudoku")
        self.game = SudokuGenerator()
        self.entries = []
        self.create_widgets()

    def create_widgets(self):
        """Create the Sudoku grid and control buttons"""
        # Create 9x9 grid of Entry widgets
        for i in range(9):
            row_entries = []
            for j in range(9):
                entry = tk.Entry(
                    self.master,
                    width=2,
                    font=("Arial", 24),
                    justify="center",
                    bg="white",
                )
                entry.grid(row=i, column=j, padx=1, pady=1)

                # Add thicker borders between 3x3 boxes
                if i % 3 == 0 and i != 0:
                    entry.grid(pady=(3, 0))
                if j % 3 == 0 and j != 0:
                    entry.grid(padx=(3, 0))

                # Initialize with puzzle values
                value = self.game.puzzle_grid[i][j]
                if value != 0:
                    entry.insert(0, str(value))
                    entry.config(state="disabled", disabledbackground="#f0f0f0")
                else:
                    entry.config(
                        validate="key",
                        validatecommand=(
                            self.master.register(self.validate_input),
                            "%P",
                        ),
                    )
                row_entries.append(entry)
            self.entries.append(row_entries)

        # Control buttons
        check_button = tk.Button(
            self.master,
            text="Check Solution",
            command=self.check_solution,
            padx=10,
            pady=5,
        )
        check_button.grid(row=9, column=0, columnspan=4, pady=10)

        new_game_button = tk.Button(
            self.master, text="New Game", command=self.new_game, padx=10, pady=5
        )
        new_game_button.grid(row=9, column=5, columnspan=4, pady=10)

    @staticmethod
    def validate_input(new_value):
        """Validate user input to allow only 1-9 or empty"""
        return new_value == "" or (new_value.isdigit() and 1 <= int(new_value) <= 9)

    def check_solution(self):
        """Validate the current state of the grid against Sudoku rules"""
        # Convert entries to integer grid
        user_grid = []
        has_empty = False
        for i in range(9):
            row = []
            for j in range(9):
                value = self.entries[i][j].get()
                if not value:
                    has_empty = True
                    row.append(0)
                else:
                    row.append(int(value))
            user_grid.append(row)

        if has_empty:
            messagebox.showwarning("Incomplete", "Please fill all cells!")
            return

        # Check rows, columns, and boxes
        valid = True
        error_cells = set()

        # Check rows and columns
        for i in range(9):
            row = user_grid[i]
            col = [user_grid[j][i] for j in range(9)]
            for check, axis in [(row, "row"), (col, "col")]:
                seen = set()
                duplicates = set()
                for idx, num in enumerate(check):
                    if num in seen:
                        valid = False
                        if axis == "row":
                            duplicates.add((i, idx))
                        else:
                            duplicates.add((idx, i))
                    seen.add(num)
                error_cells.update(duplicates)

        # Check 3x3 boxes
        for box_i in range(0, 9, 3):
            for box_j in range(0, 9, 3):
                seen = set()
                duplicates = set()
                for i in range(3):
                    for j in range(3):
                        row = box_i + i
                        col = box_j + j
                        num = user_grid[row][col]
                        if num in seen:
                            valid = False
                            duplicates.add((row, col))
                        seen.add(num)
                error_cells.update(duplicates)

        # Highlight errors
        for i in range(9):
            for j in range(9):
                bg_color = "#ff9999" if (i, j) in error_cells else "white"
                self.entries[i][j].config(bg=bg_color)

        if valid:
            messagebox.showinfo("Congratulations!", "You solved the Sudoku!")
        else:
            messagebox.showerror(
                "Invalid Solution",
                "There are duplicate numbers in rows, columns, or boxes!",
            )

    def new_game(self):
        """Generate a new puzzle and reset the UI"""
        self.game = SudokuGenerator()
        for i in range(9):
            for j in range(9):
                entry = self.entries[i][j]
                entry.config(state="normal", bg="white")
                entry.delete(0, tk.END)
                value = self.game.puzzle_grid[i][j]
                if value != 0:
                    entry.insert(0, str(value))
                    entry.config(state="disabled", disabledbackground="#f0f0f0")
                else:
                    entry.config(state="normal")


if __name__ == "_main_":
    root = tk.Tk()
    SudokuUI()
    root.mainloop()
