from .card_deck import Card, FrenchDeck, spades_high

from random import choice


def main():
    delimiter = "=" * 120
    print(delimiter)
    print(f"Running Chapter 1 examples")
    print(delimiter)

    beer_card = Card("7", "diamonds")
    print(beer_card)

    deck = FrenchDeck()
    print(f"The len of the French deck is: {len(deck)}")
    print(f"The first item on the deck is: {deck[0]}")
    print(f"The last item on the deck is: {deck[-1]}")

    random_cards = [choice(deck) for _ in range(3)]
    print(f"Three random cards from the deck are: {random_cards}")

    # Benefits from __getitem__ --> using slicing
    print(f"The 3 first cards of the deck are: {deck[:3]}")

    aces = deck[12::13]
    print(f"Only aces: {aces}")

    print("__getitem__ allows to iterate the deck")
    for card in deck:
        print(card)

    print("__getitem__ allows to iterate the deck, also in reverse")
    for card in reversed(deck):
        print(card)

    q_hearts = Card("Q", "hearts")
    false_card = Card("7", "beasts")
    print(f"Is {q_hearts} in deck?: {q_hearts in deck}")
    print(f"Is {false_card} in deck?: {false_card in deck}")

    print(f"Deck sorted in order of increasing rank")
    for card in sorted(deck, key=spades_high):
        print(card)


if __name__ == "__main__":
    main()
