import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [""] * 9

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(
                    self.window,
                    text="",
                    font=("Arial", 20),
                    width=5,
                    height=2,
                    command=lambda i=i, j=j: self.on_click(i, j),
                )
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

        self.status_label = tk.Label(
            self.window, text=f"Player {self.current_player}'s turn", font=("Arial", 14)
        )
        self.status_label.grid(row=3, column=0, columnspan=3)

        reset_btn = tk.Button(self.window, text="Reset Game", command=self.reset_game)
        reset_btn.grid(row=4, column=0, columnspan=3)

        self.window.mainloop()

    def on_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        win_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],  # rows
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],  # columns
            [0, 4, 8],
            [2, 4, 6],  # diagonals
        ]

        for combo in win_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        for row in self.buttons:
            for btn in row:
                btn.config(text="")
        self.status_label.config(text=f"Player {self.current_player}'s turn")


if __name__ == "__main__":
    TicTacToe()
