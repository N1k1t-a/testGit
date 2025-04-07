from dataclasses import dataclass, asdict, astuple


@dataclass  # это декоратор
class User:
    id: int
    name: str
    email: str = None


@dataclass
class Point:
    x: int
    y: int
    z: int


@dataclass
class Person:
    age: int
    weight: int
    fat: int


def main():
    john = User(id=10, name='даун', email="john@example.com")
    print(john)
    person = Person(30, 95, 42)
    point = Point(30, 95, 42)
    print(point)
    print(person)
    print(asdict(person))
    print(astuple(person))


if __name__ == "__main__":
    main()
