import cards

class Board:
    def __init__(self):
        self.all_decks = [cards.Deck("tier1deck.json"), cards.Deck("tier2deck.json"), cards.Deck("tier3deck.json")]
        self.visible_cards = [[],[],[]]
        self.available_tokens = {
            cards.Color.GREEN: 6,
            cards.Color.WHITE: 6,
            cards.Color.BLUE: 6,
            cards.Color.BLACK: 6,
            cards.Color.RED: 6,
            cards.Color.GOLD: 2}

    def lay_out_cards(self):
        for deck, visible_cards in zip(self.all_decks, self.visible_cards):
            while len(visible_cards)<4 and len(deck.deck) != 0:
                visible_cards.append(deck.draw_card_from_deck())

    def draw_visible_card(self, tier: int, index: int) -> cards.Card:
        if tier >= len(self.visible_cards) or index >= len(self.visible_cards[tier]):
            raise IndexError(f"Tier {tier} or index {index} out of range.")
        return self.visible_cards[tier].pop(index)

    def can_draw_tokens(self, requested_tokens: dict[cards.Color, int]) -> bool:
        """
        Checks if the player can draw tokens based on the game rules.
        - Player may only draw a gold if it is the only token being drawn, in which case the player may simultaneously reserve a card.
        - Player may draw 2 tokens of the same color but only if there are at least 4 tokens available of that color.
        - Player may draw up to 3 tokens of different colors.
        """
        if cards.Color.GOLD in requested_tokens and len(requested_tokens) > 1:
            return False

        if len(requested_tokens) == 1:
            color = next(iter(requested_tokens))
            if color in self.available_tokens and self.available_tokens.get(color, 0) >= 4:
                return True
            return False

        elif 1 <= len(requested_tokens) <= 3:
            for color, count in requested_tokens.items():
                if count != 1 or self.available_tokens.get(color, 0) < count:
                    return False
            return True

        else:
            return False

    def decrease_token_amount(self, requested_tokens: dict[cards.Color, int]):
        for color, count in requested_tokens.items():
            self.available_tokens[color] -= count

    def increase_token_amount(self, player_tokens: dict[cards.Color, int]):
        for color, count in player_tokens.items():
            self.available_tokens[color] += count

