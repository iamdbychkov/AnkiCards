import dataclasses
import random


@dataclasses.dataclass
class Card: 

    word: str
    translation: str


class Anki:
    
    cards: list[Card]

    def __init__(self):
        self.cards = []

    def add_card(self, word: str, translation: str):
        self.cards.append(Card(word, translation))

    def get_cards(self) -> list[Card]:
        return self.cards

    def get_card(self, word: str) -> Card:
        for card in self.cards:
            if card.word == word:
                return card
        raise ValueError("Unknown Word")
    
    def get_random_card(self) -> Card:
        return random.choice(self.cards)
    

if __name__ == "__main__":
    anki = Anki()

    anki.add_card("gato", "кот")

    card = anki.get_card("gato")

    assert card.word == "gato", "Ошибка 1"
    assert card.word == "кот", "Ошибка 2"

