from .bus import Bus, HauntedBus
import copy


def aliasing():
    charles = {"name": "Charles L. Dogson", "born": 1832}
    lewis = charles
    print(lewis == charles)
    print(id(charles), id(lewis))
    lewis["balance"] = 950
    print(charles)

    alex = {"name": "Charles L. Dogson", "born": 1832, "balance": 950}
    print(alex == charles)
    print(alex is not charles)


def relative_tuple_immutability():
    t1 = (1, 2, [30, 40])
    t2 = (1, 2, [30, 40])
    print(t1 == t2)
    print(id(t1) != id(t2))
    print(id(t1[-1]))
    t1[-1].append(99)
    print(id(t1[-1]))
    print(t1 == t2)


def shallow_vs_deep_copies():
    bus1 = Bus(["Alice", "Bill", "Claire", "David"])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    print(id(bus1), id(bus2), id(bus3))

    bus1.drop("Bill")
    print(bus2.passengers)
    print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
    print(bus3.passengers)


def mutable_defaults_trouble():
    bus1 = HauntedBus(["Alice", "Bill"])
    print(bus1.passengers)

    bus1.pick("Charlie")
    bus1.drop("Alice")
    print(bus1.passengers)

    bus2 = HauntedBus()
    bus2.pick("Carrie")
    print(bus2.passengers)

    bus3 = HauntedBus()
    print(bus3.passengers)
    bus3.pick("Dave")

    print(bus2.passengers)
    print(bus2.passengers is bus3.passengers)
    print(bus1.passengers)


def main():
    aliasing()
    relative_tuple_immutability()
    shallow_vs_deep_copies()
    mutable_defaults_trouble()


if __name__ == "__main__":
    main()
