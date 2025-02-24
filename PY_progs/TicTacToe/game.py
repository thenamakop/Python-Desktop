from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random


class TicTacToeAI:
    def __init__(self):
        self.human = "X"
        self.ai = "O"

    def random_move(self, board):
        empty = [(x, y) for y in range(3) for x in range(3) if board[y][x] == ""]
        return random.choice(empty) if empty else (None, None)

    def best_move(self, board):
        best_score = -float("inf")
        best_move = None

        for y in range(3):
            for x in range(3):
                if board[y][x] == "":
                    board[y][x] = self.ai
                    score = self.minimax(board, False)
                    board[y][x] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (x, y)
        return best_move

    def minimax(self, board, is_maximizing):
        result = self.check_winner(board)
        if result is not None:
            if result == self.ai:
                return 1
            elif result == self.human:
                return -1
            else:
                return 0

        if is_maximizing:
            best_score = -float("inf")
            for y in range(3):
                for x in range(3):
                    if board[y][x] == "":
                        board[y][x] = self.ai
                        score = self.minimax(board, False)
                        board[y][x] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for y in range(3):
                for x in range(3):
                    if board[y][x] == "":
                        board[y][x] = self.human
                        score = self.minimax(board, True)
                        board[y][x] = ""
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, board):
        # Check rows
        for row in board:
            if row[0] == row[1] == row[2] != "":
                return row[0]

        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != "":
                return board[0][col]

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != "":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != "":
            return board[0][2]

        # Check tie
        if all(cell != "" for row in board for cell in row):
            return "tie"

        return None


class TicTacToeGame(Entity):
    def __init__(self):
        super().__init__()
        self.state = "menu"
        self.game_mode = None
        self.difficulty = None
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.ai = TicTacToeAI()
        self.setup_menu()
        self.winner_text = None

    def setup_menu(self):
        self.menu = Entity(parent=self)
        Text("3D TIC TAC TOE", scale=2, y=0.4)
        Button("Player vs Player", color=color.green, y=0.1, on_click=self.start_pvp)
        Button(
            "Player vs AI", color=color.orange, y=-0.1, on_click=self.show_difficulty
        )
        Button("Quit", color=color.red, y=-0.3, on_click=application.quit)

    def show_difficulty(self):
        self.menu.disable()
        self.difficulty_menu = Entity(parent=self)
        Text("Select Difficulty", scale=2, y=0.4)
        Button(
            "Normal", color=color.blue, y=0.1, on_click=lambda: self.start_pvc("normal")
        )
        Button(
            "Hard", color=color.yellow, y=-0.1, on_click=lambda: self.start_pvc("hard")
        )
        Button("Back", color=color.gray, y=-0.3, on_click=self.back_to_menu)

    def start_pvp(self):
        self.game_mode = "pvp"
        self.start_game()

    def start_pvc(self, difficulty):
        self.game_mode = "pvc"
        self.difficulty = difficulty
        self.start_game()

    def back_to_menu(self):
        self.difficulty_menu.disable()
        self.menu.enable()

    def start_game(self):
        self.menu.disable()
        if hasattr(self, "difficulty_menu"):
            self.difficulty_menu.disable()
        self.setup_board()

    def setup_board(self):
        self.cubes = []
        for y in range(3):
            for x in range(3):
                cube = Button(
                    parent=self,
                    model="cube",
                    color=color.white33,
                    position=(x - 1, y - 1, 0),
                    scale=0.9,
                    on_click=Func(self.make_move, x, y),
                )
                self.cubes.append(cube)

    def make_move(self, x, y):
        if self.board[y][x] == "" and self.current_player == "X":
            self.board[y][x] = "X"
            self.cubes[y * 3 + x].color = color.blue
            self.check_game_state()

            if self.game_mode == "pvc":
                self.current_player = "O"
                invoke(self.ai_move, delay=0.5)

    def ai_move(self):
        if self.difficulty == "normal":
            x, y = self.ai.random_move(self.board)
        else:
            x, y = self.ai.best_move(self.board)

        if x is not None and y is not None:
            self.board[y][x] = "O"
            self.cubes[y * 3 + x].color = color.red
            self.check_game_state()
            self.current_player = "X"

    def check_game_state(self):
        winner = self.ai.check_winner(self.board)
        if winner:
            self.show_result(winner)

    def show_result(self, result):
        for cube in self.cubes:
            cube.collision = False

        if self.winner_text:
            destroy(self.winner_text)

        if result == "tie":
            self.winner_text = Text("It's a tie!", scale=2, y=0.5)
        else:
            self.winner_text = Text(f"Player {result} wins!", scale=2, y=0.5)

        invoke(self.reset_game, delay=2)

    def reset_game(self):
        if self.winner_text:
            destroy(self.winner_text)
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for cube in self.cubes:
            cube.color = color.white33
            cube.collision = True
        self.cubes = []
        self.state = "menu"
        self.setup_menu()


app = Ursina()
window.fullscreen = False
window.title = "3D Tic Tac Toe"
game = TicTacToeGame()
Sky()
EditorCamera()
app.run()
