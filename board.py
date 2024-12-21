import cards

class Board:
    def __init__(self):
        self.tier_1_deck = cards.Deck("tier1deck.cvs")
        self.tier_2_deck = cards.Deck("tier2deck.cvs")
        self.tier_3_deck = cards.Deck("tier3deck.cvs")
        self.visible_tier_1_cards = []
        self.visible_tier_2_cards = []
        self.visible_tier_3_cards = []
        self.available_tokens = {
            cards.Color.GREEN: 6,
            cards.Color.WHITE: 6,
            cards.Color.BLUE: 6,
            cards.Color.BLACK: 6,
            cards.Color.RED: 6,
            cards.Color.GOLD: 2}
    def lay_out_cards(self):
        while len(self.visible_tier_1_cards) < 3 and len(self.tier_1_deck.deck) != 0:
            self.visible_tier_1_cards.append(self.tier_1_deck.draw_card_from_deck())
        while len(self.visible_tier_2_cards) < 3 and len(self.tier_2_deck.deck) != 0:
            self.visible_tier_2_cards.append(self.tier_2_deck.draw_card_from_deck())
        while len(self.visible_tier_3_cards) < 3 and len(self.tier_3_deck.deck) != 0:
            self.visible_tier_3_cards.append(self.tier_3_deck.draw_card_from_deck())
    def draw_card(self,index,tier):
        if index>
