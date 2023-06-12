from array import array
from random import random

from collections import deque


def create_10_million_floats():
    floats = array("d", (random() for _ in range(10**7)))
    print(f"Las item: {floats[-1]}")

    with open("floats.bin", "wb") as fp:
        floats.tofile(fp)

    floats2 = array("d")
    with open("floats.bin", "rb") as fp:
        floats2.fromfile(fp, 10**7)

    print(f"Last float value: {floats2[-1]}")


def testing_deques():
    dq = deque(range(10), maxlen=10)
    print(f"Original deque: {dq}")

    dq.rotate(3)
    print(f"Deque rotated 3: {dq}")

    dq.rotate(-4)
    print(f"Deque rotated -4: {dq}")

    dq.appendleft(-1)
    print(f"Deque after appendleft: {dq}")

    dq.extend([11, 22, 33])
    print(f"Deque after extend: {dq}")

    dq.extendleft([10, 20, 30, 40])
    print(f"Deque after extendleft: {dq}")
