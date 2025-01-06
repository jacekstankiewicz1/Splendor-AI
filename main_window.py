from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsView, QLabel, QGraphicsDropShadowEffect, QWidget, QListWidgetItem
from PySide6.QtGui import QPainter, QColor, QFont
from game_window import Ui_MainWindow
from game import Game
from PySide6.QtCore import Qt
from cards import Color
from card_widget import Ui_CardWidget
from cards import Card



card_stylesheets = {
    Color.BLUE: [
        "border-radius: 10px;\nbackground: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #7eb3ff, stop:1 #446fad);\npadding: 20px;\n",
        "border-radius: 25px;\nbackground: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #59b9ff, stop:1 #004aad);\npadding: 12px;\n"
    ],
    Color.RED: [
        "border-radius: 10px;\nbackground: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #ff7a7a, stop:1 #b54646);\npadding: 20px;\n",
        "border-radius: 25px;\nbackground: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #ff9999, stop:1 #8c2a2a);\npadding: 12px;\n"
    ],
    Color.BLACK: [
        "border-radius: 10px;\nbackground: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #333333, stop:1 #000000);\npadding: 20px;\n",
        "border-radius: 25px;\nbackground: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #4d4d4d, stop:1 #1a1a1a);\npadding: 12px;\n"
    ],
    Color.WHITE: [
        "border-radius: 10px;\nbackground: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #f0f0f0, stop:1 #d9d9d9);\npadding: 20px;\n",
        "border-radius: 25px;\nbackground: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #ffffff, stop:1 #cccccc);\npadding: 12px;\n"
    ],
    Color.GREEN: [
        "border-radius: 10px;\nbackground: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #7aff70, stop:1 #4ca64c);\npadding: 20px;\n",
        "border-radius: 25px;\nbackground: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #99ff99, stop:1 #2a8c31);\npadding: 12px;\n"
    ]
}


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

    def render_card(self, card : Card) -> QWidget:
        card_widget = QWidget()
        ui = Ui_CardWidget()
        ui.setupUi(card_widget)

        general_stylesheet, specific_stylesheet = card_stylesheets.get(card.color, ("", ""))

        card_widget.setStyleSheet(general_stylesheet)

        ui.label.setStyleSheet(specific_stylesheet)
        ui.listWidget.setStyleSheet(specific_stylesheet)

        ui.label.setText(str(card.value))

        ui.listWidget.clear()
        for color, cost in card.cost.items():
            # Create a QLabel for each cost
            cost_label = QLabel()
            cost_label.setFixedSize(30, 30)
            cost_label.setAlignment(Qt.AlignCenter)
            cost_label.setText(str(cost))
            cost_label.setStyleSheet(f"""
                background-color: {color.name.lower()};
                color: white;
                border: 1px solid black;
                border-radius: 15px;
                font-weight: bold;
            """)
            # Add the QLabel as a QListWidgetItem
            item = QListWidgetItem()
            item.setSizeHint(cost_label.size())
            ui.listWidget.addItem(item)
            ui.listWidget.setItemWidget(item, cost_label)

        return card_widget


    def update_cards(self, game : Game):
        board = game.board
        # Renders the visible cards
        for i in range(self.ui.cardLayout.count()):
            widget = self.ui.cardLayout.itemAt(i).widget()
            if isinstance(widget, QLabel):
                #  This assumes that the names of the widgets in Qt designer follow "txy", where x is the tier of the card and y is the index from the left (starting at 1).
                tier = int(widget.objectName()[1])-1
                index = int(widget.objectName()[2])-1
                try:
                    card = board.visible_cards[tier][index]
                    rendered_card_widget = self.render_card(card)
                    self.ui.cardLayout.addWidget(rendered_card_widget, tier, index)
                except IndexError:
                    widget.setText("Empty")
                    widget.setStyleSheet("background-color: gray; border: 1px solid black;")
        # Renders the decks
        for i in range(self.ui.deckLayout.count()):
            widget = self.ui.deckLayout.itemAt(i).widget()
            if isinstance(widget, QLabel):
                tier = int(widget.objectName()[1])-1
                try:
                    cards_left = len(board.all_decks[tier].deck)
                    widget.setText(f"Cards left: {cards_left}")
                    widget.setStyleSheet("background-color: gray; border: 1px solid black;")
                except IndexError:
                    widget.setText("Cards left: 0")
                    widget.setStyleSheet("background-color: gray; border: 1px solid black;")

    def update_tokens(self, game: Game):
        board = game.board
        color_to_str = {
            Color.BLACK: "black",
            Color.WHITE: "white",
            Color.RED: "red",
            Color.GREEN: "green",
            Color.BLUE: "blue",
            Color.GOLD: "yellow"
        }
        for i, color in enumerate(Color):
            if i >= self.ui.tokenLayout.count():
                break
            widget = self.ui.tokenLayout.itemAt(i).widget()
            if isinstance(widget, QLabel):
                tokens_left = board.available_tokens.get(color,0)
                widget.setFixedSize(50, 50)
                widget.setStyleSheet(
                    f"""
                        background-color: {color_to_str[color]};
                        border: 1px solid black;
                        border-radius: {50 // 2}px;
                        """
                )
                widget.setText(f"{tokens_left}")

    def update_players(self, game: Game):
        board = game.board
        for i in range(self.ui.playerLayout.count()):
            widget = self.ui.playerLayout.itemAt(i).widget()
            if isinstance(widget, QLabel):
                try:
                    # Get the corresponding player
                    player = game.players[i]

                    # Calculate the player's total card values
                    card_values = {color: player.card_bonuses.get(color, 0) for color in Color if
                                   color != Color.GOLD}

                    # Prepare display string
                    info = f"Player: {player.name}\n" \
                           f"Tokens: {', '.join([f'{color.name}: {count}' for color, count in player.tokens.items() if count > 0])}\n" \
                           f"Cards: {', '.join([f'{color.name}: {count}' for color, count in card_values.items() if count > 0])}\n" \
                           f"Total Points: {player.count_points()}"

                    # Update QLabel
                    widget.setText(info)

                except IndexError:
                    widget.setText("No player")

    def update_nobles(self, game: Game):
        board = game.board


if __name__ == "__main__":
    game = Game("bob", "bill")
    game.board.lay_out_cards()
    game.board.lay_out_cards()
    app = QApplication([])
    window = MainWindow()
    window.update_cards(game)
    window.update_tokens(game)
    window.update_players(game)

    window.show()
    app.exec()