def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


def first_class_example():
    fact = factorial
    print(f"Fact is a function:  {fact}")
    print(f"Calling factorial through fact: {fact(5)}")
    # Passing the function as an argument
    print(f"Passing factorial as an argument for map {map(factorial, range(11))}")
    r = list(map(factorial, range(11)))
    print(f"The result of map is: {r}")


def main():
    print(f"42! = {factorial(42)}")
    print(f"The documentation of factorial(n) is: {factorial.__doc__}")
    print(f"The type of factorial is: {type(factorial)}")

    first_class_example()

    fruits = ["strawberry", "fig", "apple", "cherry", "raspberry", "banana"]
    sorted_fruits = sorted(fruits, key=lambda word: word[::-1])
    print(f"Original list: {fruits} vs Sorted list: {sorted_fruits}")


if __name__ == "__main__":
    main()
