import cards
import board
import player

class Game:
    def __init__(self, *names):
        self.players = [player.Player(name) for name in names]
        self.board = board.Board()
'''
    def play(self):
        while not any(p.count_points() > 15 for p in self.players):
            for p in self.players:
                action =

    def do_action(self, p: player.Player):
        action = take_action_from_user()
        switch action = something:
            do something
        
'''