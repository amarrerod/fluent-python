from .vector2d_v0 import Vector2d


def main():
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)
    x, y = v1
    print(f"X: {x}, Y: {y}")
    print(f"Vector {v1}")

    octets = bytes(v1)
    print(octets)
    v2 = Vector2d.frombytes(octets)
    print(v2)
    print(v1 == v2)


if __name__ == "__main__":
    main()
