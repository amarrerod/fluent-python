from .frenchdeck import FrenchDeck
from .frenchdeck_abc import FrenchDeck2
from random import shuffle

from .tombola import Tombola
from .bingo import Bingo
from .lotto import Lotto
from .tombolist import Tombo

from .randompick import RandomPicker
import random
from typing import Any, Iterable, TYPE_CHECKING


class SimplePicker:
    def __init__(self, items: Iterable):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self) -> Any:
        return self._items.pop()


def test_isisntance():
    p = SimplePicker([1])
    assert isinstance(p, RandomPicker)
    return True


def test_item_type():
    items = list(range(10))
    p = SimplePicker(items)
    item = p.pick()
    assert item in items
    assert isinstance(item, int)
    return True


def set_card(self, key, value):
    self._cards[key] = value


def main():
    # Monkey Patching the __setitem__ method in FrenchDeck
    FrenchDeck.__setitem__ = set_card
    deck = FrenchDeck()
    print(f"The initial deck looks like: {deck[:5]}")
    shuffle(deck)
    print(f"Now, the shuffled deck: {deck[:5]}")

    deck_abc = FrenchDeck2()
    print(f"The initial deck looks like: {deck_abc[:5]}")
    shuffle(deck_abc)
    print(f"Now, the shuffled deck: {deck_abc[:5]}")

    bingo = Bingo(list(range(100)))
    print(f"Does the bingo contain items: {bingo.loaded()} ")
    print(f"Bingo items: {bingo.inspect()} ")

    lotto = Lotto(tuple(range(100)))
    print(f"Does the lotto contain items: {lotto.loaded()} ")
    print(f"Lotto items: {lotto.inspect()} ")

    tombo = Tombo(list(range(100)))
    print(f"Does the tombo contain items: {tombo.loaded()} ")
    print(f"Tombo items: {tombo.inspect()} ")
    print(issubclass(Tombo, Tombola))
    print(isinstance(tombo, Tombola))

    test_isisntance()
    test_item_type()


if __name__ == "__main__":
    main()
