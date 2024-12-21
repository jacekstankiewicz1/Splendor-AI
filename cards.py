from enum import Enum, auto
from typing import NamedTuple, Dict
import pandas as pd
import random


class Color(Enum):
    GREEN = auto()
    WHITE = auto()
    BLUE = auto()
    BLACK = auto()
    RED = auto()
    GOLD = auto()

class Card(NamedTuple):
    value: int
    color: Color
    cost: Dict[Color, int]

class Deck:
    def __init__(self, csv_file):
        self.deck = self.load_deck_from_csv(csv_file)
        random.shuffle(self.deck)  # Shuffles the deck after it has been loaded.

    def load_deck_from_csv(self, csv_file):
        df = pd.read_csv(csv_file)
        return [Card(*row) for row in df.itertuples(index=False, name=None)]

    def draw_card_from_deck(self):
        if len(self.deck) == 0:
            raise ValueError("The deck is empty.")
        else:
            return self.deck.pop(0)
