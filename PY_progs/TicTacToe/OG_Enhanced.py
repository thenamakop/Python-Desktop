import tkinter as tk
from tkinter import messagebox
import random
import winsound


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe - Enhanced")
        self.current_player = "X"
        self.board = [""] * 9
        self.x_wins = 0
        self.o_wins = 0
        self.game_mode = "two"  # 'two' or 'single'
        self.difficulty = "easy"  # 'easy' or 'hard'
        self.player_colors = {"X": "#ff4444", "O": "#4444ff"}
        self.bg_color = "#f0f0f0"
        self.win_color = "#44ff44"

        # Create menu
        self.menu_bar = tk.Menu(self.window)
        self.window.config(menu=self.menu_bar)

        # Game mode menu
        self.mode_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Mode", menu=self.mode_menu)
        self.mode_menu.add_command(
            label="Single Player", command=self.set_single_player
        )
        self.mode_menu.add_command(label="Two Players", command=self.set_two_players)

        # Difficulty menu
        self.diff_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Difficulty", menu=self.diff_menu)
        self.diff_menu.add_command(
            label="Easy", command=lambda: self.set_difficulty("easy")
        )
        self.diff_menu.add_command(
            label="Hard", command=lambda: self.set_difficulty("hard")
        )

        # Game board
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
                    relief="raised",
                    bg=self.bg_color,
                    command=lambda i=i, j=j: self.on_click(i, j),
                )
                btn.grid(row=i, column=j, padx=2, pady=2)
                row.append(btn)
            self.buttons.append(row)

        # Status and controls
        self.status_label = tk.Label(
            self.window,
            text=f"Player {self.current_player}'s turn",
            font=("Arial", 14),
            pady=10,
        )
        self.status_label.grid(row=3, column=0, columnspan=3)

        # Score display
        self.score_frame = tk.Frame(self.window)
        self.score_frame.grid(row=4, column=0, columnspan=3, pady=5)
        self.x_score = tk.Label(
            self.score_frame,
            text="X: 0",
            font=("Arial", 12),
            fg=self.player_colors["X"],
        )
        self.x_score.pack(side=tk.LEFT, padx=10)
        self.o_score = tk.Label(
            self.score_frame,
            text="O: 0",
            font=("Arial", 12),
            fg=self.player_colors["O"],
        )
        self.o_score.pack(side=tk.LEFT, padx=10)

        # Reset button
        self.reset_btn = tk.Button(
            self.window, text="Reset Game", command=self.reset_game, font=("Arial", 12)
        )
        self.reset_btn.grid(row=5, column=0, columnspan=3, pady=5)

        self.window.mainloop()

    def set_single_player(self):
        self.game_mode = "single"
        self.reset_game()

    def set_two_players(self):
        self.game_mode = "two"
        self.reset_game()

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.reset_game()

    def on_click(self, row, col):
        if self.game_mode == "single" and self.current_player == "O":
            return
        self.make_move(row, col)

    def make_move(self, row, col):
        index = row * 3 + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[row][col].config(
                text=self.current_player, fg=self.player_colors[self.current_player]
            )
            self.play_sound("move")

            if self.check_winner():
                self.handle_win()
            elif "" not in self.board:
                self.handle_draw()
            else:
                self.switch_player()
                if self.game_mode == "single" and self.current_player == "O":
                    self.window.after(800, self.ai_move)

    def ai_move(self):
        if self.difficulty == "hard":
            best_move = self.find_best_move()
            choice = best_move
        else:
            empty_cells = [i for i, cell in enumerate(self.board) if cell == ""]
            choice = random.choice(empty_cells) if empty_cells else None

        if choice is not None:
            row, col = divmod(choice, 3)
            self.make_move(row, col)

    def find_best_move(self):
        best_score = -float("inf")
        best_move = None
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                score = self.minimax(self.board, False)
                self.board[i] = ""
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def minimax(self, board, is_maximizing):
        winner = self.check_winner_minimax(board)
        if winner == "O":
            return 1
        elif winner == "X":
            return -1
        elif "" not in board:
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for i in range(9):
                if board[i] == "":
                    board[i] = "O"
                    score = self.minimax(board, False)
                    board[i] = ""
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if board[i] == "":
                    board[i] = "X"
                    score = self.minimax(board, True)
                    board[i] = ""
                    best_score = min(score, best_score)
            return best_score

    def check_winner_minimax(self, board):
        win_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        for combo in win_combinations:
            a, b, c = combo
            if board[a] == board[b] == board[c] != "":
                return board[a]
        return None

    def check_winner(self):
        winner = self.check_winner_minimax(self.board)
        return winner is not None

    def handle_win(self):
        winner = self.current_player
        if winner == "X":
            self.x_wins += 1
        else:
            self.o_wins += 1
        self.update_scores()
        self.highlight_winning_line()
        self.play_sound("win")
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.reset_game()

    def handle_draw(self):
        self.play_sound("draw")
        messagebox.showinfo("Game Over", "It's a tie!")
        self.reset_game()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.config(text=f"Player {self.current_player}'s turn")

    def highlight_winning_line(self):
        win_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        for combo in win_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != "":
                for index in combo:
                    row, col = divmod(index, 3)
                    self.buttons[row][col].config(bg=self.win_color)
                break

    def play_sound(self, sound_type):
        try:
            if sound_type == "move":
                winsound.Beep(440, 200)
            elif sound_type == "win":
                winsound.Beep(880, 500)
            elif sound_type == "draw":
                winsound.Beep(220, 500)
        except:
            pass  # Sound not available on this platform

    def update_scores(self):
        self.x_score.config(text=f"X: {self.x_wins}")
        self.o_score.config(text=f"O: {self.o_wins}")

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        for row in self.buttons:
            for btn in row:
                btn.config(text="", bg=self.bg_color)
        self.status_label.config(text=f"Player {self.current_player}'s turn")
        if self.game_mode == "single" and self.current_player == "O":
            self.ai_move()


if __name__ == "__main__":
    TicTacToe()
