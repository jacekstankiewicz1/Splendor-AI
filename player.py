import cards
import board
from collections import Counter

class Player:
    def __init__(self, name: str):
        self.name = name
        self.tokens = {cards.Color.GREEN: 0, cards.Color.WHITE: 0, cards.Color.BLUE: 0, cards.Color.BLACK: 0, cards.Color.RED: 0, cards.Color.GOLD: 0}
        self.card_bonuses = {cards.Color.GREEN: 0, cards.Color.WHITE: 0, cards.Color.BLUE: 0, cards.Color.BLACK: 0, cards.Color.RED: 0, cards.Color.GOLD: 0}
        self.purchased_cards = []
        self.reserved_cards = []

    def purchase_card(self, game_board : board.Board, tier: int, index: int):
        player_purchasing_power = Counter(self.tokens) + Counter(self.card_bonuses)
        if tier >= len(game_board.visible_cards) or index >= len(game_board.visible_cards[index]):
            raise IndexError(f"Tier {tier} or index {index} out of range.")
        if not game_board.visible_cards[tier][index].can_afford(player_purchasing_power):
            raise ValueError("Card cannot be afforded.")
        token_deduction = Counter({color: max(0, count) for color, count in (Counter(self.tokens)- Counter(self.card_bonuses))})
        self.purchased_cards.append(game_board.draw_visible_card(tier, index))
        self.move_tokens_player_to_board(game_board, token_deduction)
        self.card_bonuses[self.purchased_cards[-1].color] += 1

    def reserve_card(self, card: cards.Card):
        if len(self.reserved_cards) >= 3:
            raise ValueError("Player already has 3 cards reserved.")
        self.reserved_cards.append(card)
        self.tokens[cards.Color.GOLD] += 1

    def move_tokens_player_to_board(self, game_board : board.Board, returned_tokens: dict[cards.Color, int]):
        for color, count in returned_tokens.items():
            if self.tokens[color] < count:
                raise ValueError(f"Player does not have enough {color} tokens to return.")
            self.tokens[color] -= count
        game_board.increase_token_amount(returned_tokens)

    def move_tokens_board_to_player(self, game_board : board.Board,  requested_tokens: dict[cards.Color, int]):
        if sum(requested_tokens.values()) + sum(self.tokens.values()) > 10:
            raise ValueError("The request would exceed the maximum number of 10 tokens per player.")
        if not game_board.can_draw_tokens(requested_tokens):
            raise ValueError("Illegal token request.")
        for color, count in requested_tokens.items():
            self.tokens[color] += count
        game_board.decrease_token_amount(requested_tokens)

    def count_points(self) -> int:
        return sum(card.value for card in self.purchased_cards)
