import tkinter as tk
from tkinter import messagebox, ttk
import random


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x500")
        self.window.configure(bg="#2C3E50")

        self.current_player = "X"
        self.board = [""] * 9
        self.game_mode = None  # 'pvp' or 'pvc'
        self.player_symbol = None
        self.computer_symbol = None

        self.create_welcome_screen()

        self.window.mainloop()

    def create_welcome_screen(self):
        self.clear_window()

        title = tk.Label(
            self.window,
            text="Tic Tac Toe",
            font=("Arial", 24, "bold"),
            bg="#2C3E50",
            fg="#ECF0F1",
        )
        title.pack(pady=20)

        vs_player_btn = ttk.Button(
            self.window,
            text="Player vs Player",
            command=lambda: self.set_game_mode("pvp"),
        )
        vs_player_btn.pack(pady=10, ipadx=20, ipady=10)

        vs_computer_btn = ttk.Button(
            self.window, text="Player vs Computer", command=self.create_symbol_selection
        )
        vs_computer_btn.pack(pady=10, ipadx=20, ipady=10)

    def create_symbol_selection(self):
        self.clear_window()

        title = tk.Label(
            self.window,
            text="Choose Your Symbol",
            font=("Arial", 18),
            bg="#2C3E50",
            fg="#ECF0F1",
        )
        title.pack(pady=20)

        x_btn = ttk.Button(self.window, text="X", command=lambda: self.set_symbols("X"))
        x_btn.pack(pady=10, ipadx=20, ipady=10)

        o_btn = ttk.Button(self.window, text="O", command=lambda: self.set_symbols("O"))
        o_btn.pack(pady=10, ipadx=20, ipady=10)

    def set_symbols(self, symbol):
        self.player_symbol = symbol
        self.computer_symbol = "O" if symbol == "X" else "X"
        self.set_game_mode("pvc")

    def set_game_mode(self, mode):
        self.game_mode = mode
        self.start_game()

    def start_game(self):
        self.clear_window()
        self.current_player = "X"
        self.board = [""] * 9

        # Game Board
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(
                    self.window,
                    text="",
                    font=("Arial", 24),
                    width=4,
                    height=2,
                    relief="flat",
                    bg="#34495E",
                    activebackground="#2C3E50",
                    fg="#ECF0F1",
                )
                btn.config(command=lambda i=i, j=j: self.on_click(i, j))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

        # Status Label
        self.status_label = tk.Label(
            self.window,
            text=f"Player {self.current_player}'s turn",
            font=("Arial", 14),
            bg="#2C3E50",
            fg="#ECF0F1",
        )
        self.status_label.grid(row=3, column=0, columnspan=3, pady=20)

        # Control Buttons
        reset_btn = ttk.Button(self.window, text="Reset Game", command=self.reset_game)
        reset_btn.grid(row=4, column=0, columnspan=3, pady=10)

        # If computer starts first
        if self.game_mode == "pvc" and self.current_player == self.computer_symbol:
            self.computer_move()

    def animate_button(self, button, symbol):
        colors = {"X": "#E74C3C", "O": "#3498DB"}
        button.config(fg=colors[symbol])
        for i in range(0, 255, 5):
            if symbol == "X":
                color = "#%02x%02x%02x" % (231, 76 + i, 60 + i)
            else:
                color = "#%02x%02x%02x" % (52 + i, 152 + i, 219)
            button.config(bg=color)
            self.window.update()
            self.window.after(5)
        button.config(bg="#34495E")

    def on_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == "" and (
            self.game_mode == "pvp"
            or (self.game_mode == "pvc" and self.current_player == self.player_symbol)
        ):
            self.board[index] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            self.animate_button(self.buttons[row][col], self.current_player)

            if self.check_winner():
                self.highlight_winning_combination()
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

                if (
                    self.game_mode == "pvc"
                    and self.current_player == self.computer_symbol
                ):
                    self.window.after(500, self.computer_move)

    def computer_move(self):
        available_moves = [i for i, val in enumerate(self.board) if val == ""]
        if available_moves:
            move = random.choice(available_moves)
            row = move // 3
            col = move % 3
            self.board[move] = self.computer_symbol
            self.buttons[row][col].config(text=self.computer_symbol)
            self.animate_button(self.buttons[row][col], self.computer_symbol)

            if self.check_winner():
                self.highlight_winning_combination()
                messagebox.showinfo("Game Over", "Computer wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = self.player_symbol
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
                self.winning_combo = combo
                return True
        return False

    def highlight_winning_combination(self):
        for index in self.winning_combo:
            row = index // 3
            col = index % 3
            self.buttons[row][col].config(bg="#27AE60")

    def reset_game(self):
        self.board = [""] * 9
        for row in self.buttons:
            for btn in row:
                btn.config(text="", bg="#34495E")
        if self.game_mode == "pvc":
            self.current_player = self.player_symbol
            if self.player_symbol == "O":
                self.window.after(500, self.computer_move)
        else:
            self.current_player = "X"
        self.status_label.config(text=f"Player {self.current_player}'s turn")

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    TicTacToe()
