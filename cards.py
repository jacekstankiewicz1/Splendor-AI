from enum import Enum, auto
from typing import NamedTuple, Dict
import pandas as pd
import random
import json


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

    def can_afford(self, tokens: Dict[Color, int]) -> bool:
        for color, cost in self.cost.items():
            if tokens.get(color, 0) < cost:
                return False
        return True

class Deck:
    def __init__(self, json_file: str):
        self.deck = self.load_deck_from_json(json_file)
        random.shuffle(self.deck)

    def load_deck_from_json(self, json_file: str) -> list[Card]:
        with open(json_file, 'r') as file:
            data = json.load(file)

        deck = []
        for entry in data:
            # Convert color string to Color enum
            color_str = entry['color']
            try:
                color = Color[color_str.split('.')[1]]
            except (IndexError, KeyError) as e:
                raise ValueError(f"Invalid color format: {color_str}") from e

            # Extract value
            value = entry['value']

            # Convert cost dictionary keys from strings to Color enums
            cost_dict = {}
            for cost_color_str, cost_value in entry['cost'].items():
                try:
                    cost_color = Color[cost_color_str.split('.')[1]]
                except (IndexError, KeyError) as e:
                    raise ValueError(f"Invalid cost color format: {cost_color_str}") from e
                cost_dict[cost_color] = cost_value

            # Create Card instance
            card = Card(value=value, color=color, cost=cost_dict)
            deck.append(card)

        return deck

    def draw_card_from_deck(self) -> Card:
        if len(self.deck) == 0:
            raise ValueError("The deck is empty.")
        else:
            return self.deck.pop(0)
