from .vector import Vector


def main():
    v1 = Vector([3, 4, 5, 6, 7])
    print(f"len(v1) = {len(v1)}")
    print(f"v1[0] = {v1[0]}, v1[-1] = {v1[-1]}")
    print(repr(v1))
    v2 = v1[1:4]
    print(f"v2 = {v2}")
    v3 = v1[-1:]
    print(f"v3 = {v3}")
    print(f"v1.x = {v1.x}")
    v4 = Vector([2, 2, 2])
    print(v4)
    print(format(v1, "h"))
    print(format(v1))
    print(format(v4, ".3eh"))


if __name__ == "__main__":
    main()
