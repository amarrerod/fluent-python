from .vector2d_v0 import Vector2d


def positional_pattern_demo(v: Vector2d) -> None:
    message = ""
    match v:
        case Vector2d(0, 0):
            message = f"{v!r} is null"
        case Vector2d(0):
            message = f"{v!r} is vertical"
        case Vector2d(_, 0):
            message = f"{v!r} is horizontal"
        case Vector2d(x, y) if x == y:
            message = f"{v!r} is diagonal"
        case _:
            message = f"{v!r} is awesome"
    print(message)


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

    print(f"Regular format: {v1:.2f}")
    print(f"Scientific notation format: {v1:.3e}")

    print(f"Polar Regular format: {v1:.2fp}")
    print(f"Polar Scientific notation format: {v1:.3ep}")

    print(f"Complex representation {complex(v1)}")
    v2 = Vector2d(3, -10)
    print(f"Complex representation of negative vector: {complex(v2)}")

    positional_pattern_demo(Vector2d(0, 0))
    positional_pattern_demo(Vector2d(10, 0))
    positional_pattern_demo(Vector2d(0, 10))
    positional_pattern_demo(Vector2d(10, 10))
    positional_pattern_demo(Vector2d(40, 30))


if __name__ == "__main__":
    main()
