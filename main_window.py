from PySide6.QtWidgets import QMainWindow, QApplication
from GeneralGameLayout import Ui_MainWindow
from game import Game

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def update_graphics(self, game : Game):
        self.update_cards(game)
        self.update_tokens(game)
        self.update_players(game)
        self.update_nobles(game)

    def update_cards(self, game : Game):
        board = game.board

    def update_tokens(self, game: Game):
        board = game.board

    def update_players(self, game: Game):
        board = game.board

    def update_nobles(self, game: Game):
        board = game.board

