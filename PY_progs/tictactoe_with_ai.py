# main.py
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import subprocess
import sys
from ai import TicTacToeAI

# Game states
MENU = 0
PLAYING = 1
DIFFICULTY = 2
GAME_OVER = 3


class TicTacToe(Entity):
    def __init__(self):
        super().__init__()
        self.current_player = "X"
        self.game_mode = None
        self.difficulty = None
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.ai = TicTacToeAI()
        self.cells = []
        self.state = MENU

        self.setup_menu()

    def setup_menu(self):
        self.menu = Entity(parent=self)
        Text("TIC TAC TOE 3D", origin=(0, 0), scale=2, y=0.3)
        Button("Player vs Player", color=color.azure, y=0, on_click=self.start_pvp)
        Button(
            "Player vs Computer",
            color=color.azure,
            y=-0.2,
            on_click=self.show_difficulty,
        )
        Button("Quit", color=color.red, y=-0.4, on_click=application.quit)

    def show_difficulty(self):
        self.state = DIFFICULTY
        self.menu.disable()
        self.difficulty_menu = Entity(parent=self)
        Text("Select Difficulty", origin=(0, 0), scale=2, y=0.3)
        Button(
            "Normal", color=color.green, y=0, on_click=lambda: self.start_pvc("normal")
        )
        Button(
            "Hard", color=color.orange, y=-0.2, on_click=lambda: self.start_pvc("hard")
        )
        Button("Back", color=color.gray, y=-0.4, on_click=self.back_to_menu)

    def start_pvp(self):
        self.game_mode = "pvp"
        self.start_game()

    def start_pvc(self, difficulty):
        self.game_mode = "pvc"
        self.difficulty = difficulty
        self.start_game()

    def back_to_menu(self):
        self.state = MENU
        self.difficulty_menu.disable()
        self.menu.enable()

    def start_game(self):
        self.state = PLAYING
        if hasattr(self, "menu"):
            self.menu.disable()
        if hasattr(self, "difficulty_menu"):
            self.difficulty_menu.disable()
        self.setup_board()

    def setup_board(self):
        self.cells = []
        for y in range(3):
            for x in range(3):
                cell = Button(
                    parent=self,
                    model="cube",
                    color=color.white33,
                    position=(x - 1, y - 1, 0),
                    scale=0.8,
                    on_click=Func(self.make_move, x, y),
                )
                self.cells.append(cell)

    def make_move(self, x, y):
        if self.board[y][x] == "" and self.current_player == "X":
            self.board[y][x] = "X"
            self.cells[y * 3 + x].color = color.blue
            self.check_winner()

            if self.game_mode == "pvc":
                self.current_player = "O"
                invoke(self.ai_move, delay=0.5)

    def ai_move(self):
        if self.difficulty == "normal":
            x, y = self.ai.random_move(self.board)
        else:
            x, y = self.ai.best_move(self.board)

        self.board[y][x] = "O"
        self.cells[y * 3 + x].color = color.red
        self.check_winner()
        self.current_player = "X"

    def check_winner(self):
        # Win checking logic
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                self.end_game(row[0])
                return

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                self.end_game(self.board[0][col])
                return

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            self.end_game(self.board[0][0])
            return

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.end_game(self.board[0][2])
            return

        if all(cell != "" for row in self.board for cell in row):
            self.end_game(None)

    def end_game(self, winner):
        self.state = GAME_OVER
        for cell in self.cells:
            cell.collision = False

        if winner:
            subprocess.Popen([sys.executable, "celebration.py", winner])
        else:
            print("It's a draw!")

        invoke(self.reset_game, delay=3)

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for cell in self.cells:
            cell.color = color.white33
        self.cells = []
        self.state = MENU
        self.setup_menu()


app = Ursina()
window.fullscreen = True
game = TicTacToe()
Sky()
EditorCamera()
app.run()
