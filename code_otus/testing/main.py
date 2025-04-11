import random


class Solver:
    def __init__(self, a, b,):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b


    def add_random_value(self):
            return self.add() + random.randint(1,100)


def dev(a, b) -> int:
    return a / b


def main(a, b) -> int:
        solver = Solver(a, b)

        return solver.add()


if __name__ == "__main__":
    solver = main(4, 12)
    print(solver)

    assert solver == 13, 'ты еблан, не умеешь читать'  # если правильно, то пропускает, иначе выводит текст