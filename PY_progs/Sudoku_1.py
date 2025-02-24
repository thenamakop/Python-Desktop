import tkinter as tk
from tkinter import messagebox
import random


class SudokuGenerator:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.solved_grid = self.generate_solved_sudoku()
        self.puzzle_grid = self.create_puzzle()

    def generate_solved_sudoku(self):
        """Generate a valid solved Sudoku grid using backtracking"""
        grid = [[0 for _ in range(9)] for _ in range(9)]
        self.fill_diagonal(grid)
        self.solve(grid)
        return grid

    def fill_diagonal(self, grid):
        """Fill diagonal 3x3 boxes with random numbers"""
        for i in range(0, 9, 3):
            nums = list(range(1, 10))
            random.shuffle(nums)
            for row in range(3):
                for col in range(3):
                    grid[i + row][i + col] = nums.pop()

    def solve(self, grid):
        """Solve the Sudoku using backtracking"""
        find = self.find_empty(grid)
        if not find:
            return True
        row, col = find

        for num in random.sample(range(1, 10), 9):
            if self.is_valid(grid, row, col, num):
                grid[row][col] = num
                if self.solve(grid):
                    return True
                grid[row][col] = 0
        return False

    def find_empty(self, grid):
        """Find next empty cell"""
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(self, grid, row, col, num):
        """Check if number placement is valid"""
        if num in grid[row]:
            return False
        if num in [grid[i][col] for i in range(9)]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def create_puzzle(self):
        """Create puzzle based on difficulty level"""
        puzzle = [row.copy() for row in self.solved_grid]
        difficulty_settings = {"easy": (35, 45), "medium": (46, 55), "hard": (56, 64)}
        min_empty, max_empty = difficulty_settings[self.difficulty]
        empty_cells = random.randint(min_empty, max_empty)

        for _ in range(empty_cells):
            row, col = random.randint(0, 8), random.randint(0, 8)
            while puzzle[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            puzzle[row][col] = 0
        return puzzle


class DifficultySelector:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Difficulty")
        self.create_widgets()

    def create_widgets(self):
        """Create difficulty selection buttons"""
        frame = tk.Frame(self.master, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Choose Difficulty", font=("Arial", 16)).pack(pady=10)

        difficulties = [("Easy", "easy"), ("Medium", "medium"), ("Hard", "hard")]

        for text, difficulty in difficulties:
            btn = tk.Button(
                frame,
                text=text,
                width=15,
                command=lambda d=difficulty: self.start_game(d),
                font=("Arial", 12),
                padx=10,
                pady=5,
            )
            btn.pack(pady=5)

    def start_game(self, difficulty):
        """Start the game with selected difficulty"""
        self.master.destroy()
        root = tk.Tk()
        SudokuGUI(root, difficulty)
        root.mainloop()


class SudokuGUI:
    def __init__(self, master, difficulty):
        self.master = master
        self.master.title("Sudoku Solver")
        self.difficulty = difficulty
        self.game = SudokuGenerator(difficulty)
        self.cells = []
        self.create_grid()
        self.create_controls()

    def create_grid(self):
        """Create 9x9 grid of Entry widgets"""
        frame = tk.Frame(self.master)
        frame.pack(padx=10, pady=10)

        for i in range(9):
            row = []
            for j in range(9):
                entry = tk.Entry(
                    frame,
                    width=2,
                    font=("Arial", 24),
                    justify="center",
                    validate="key",
                    validatecommand=(self.master.register(self.validate_input), "%P"),
                )
                entry.grid(row=i, column=j, padx=1, pady=1, ipady=5)

                if i % 3 == 0 and i != 0:
                    entry.grid(pady=(3, 0))
                if j % 3 == 0 and j != 0:
                    entry.grid(padx=(3, 0))

                value = self.game.puzzle_grid[i][j]
                if value != 0:
                    entry.insert(0, str(value))
                    entry.config(state="disabled", disabledbackground="#f0f0f0")
                row.append(entry)
            self.cells.append(row)

    def create_controls(self):
        """Create control buttons"""
        control_frame = tk.Frame(self.master)
        control_frame.pack(pady=10)

        tk.Button(
            control_frame,
            text="Check Solution",
            command=self.check_solution,
            padx=20,
            pady=10,
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            control_frame,
            text="Solve Puzzle",
            command=self.solve_puzzle,
            padx=20,
            pady=10,
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            control_frame, text="New Puzzle", command=self.new_puzzle, padx=20, pady=10
        ).pack(side=tk.LEFT, padx=5)

    def validate_input(self, value):
        """Validate cell input (1-9 or empty)"""
        return value == "" or (
            len(value) == 1 and value.isdigit() and 1 <= int(value) <= 9
        )

    def check_solution(self):
        """Verify user's solution against solved grid"""
        for i in range(9):
            for j in range(9):
                cell_value = self.cells[i][j].get()
                if cell_value == "":
                    messagebox.showwarning("Incomplete", "Please fill all cells!")
                    return
                if int(cell_value) != self.game.solved_grid[i][j]:
                    self.cells[i][j].config(bg="#ff9999")
                else:
                    self.cells[i][j].config(bg="white")

        all_correct = all(
            self.cells[i][j].get() == str(self.game.solved_grid[i][j])
            for i in range(9)
            for j in range(9)
        )

        if all_correct:
            messagebox.showinfo("Success!", "Congratulations! Puzzle solved correctly!")
        else:
            messagebox.showerror("Errors Found", "Some cells contain incorrect values")

    def solve_puzzle(self):
        """Fill in the complete solution"""
        for i in range(9):
            for j in range(9):
                if self.game.puzzle_grid[i][j] == 0:
                    self.cells[i][j].delete(0, tk.END)
                    self.cells[i][j].insert(0, str(self.game.solved_grid[i][j]))
                    self.cells[i][j].config(bg="#d0f0d0", state="disabled")

    def new_puzzle(self):
        """Generate and display a new puzzle"""
        self.master.destroy()
        root = tk.Tk()
        DifficultySelector(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    DifficultySelector(root)
    root.mainloop()
