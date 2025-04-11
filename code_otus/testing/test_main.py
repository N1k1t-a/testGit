from code_otus.testing.main import Solver, dev
import unittest


class TestSolver(unittest.TestCase):

    def setUp(self) -> None:
        print("выполняется при каждом новом начатом тесте")
        self.solver = Solver(1, 2)

    def test_add(self):
        self.assertEqual(self.solver.add(), 3)

    def test_mul(self):
        solver = Solver(21, 2)
        self.assertEqual(solver.mul(), 42)
        self.assertEqual(self.solver.mul(), 2)


class TestDev(unittest.TestCase):

    def test_dev(self):
        self.assertEqual(dev(4, 2), 2)

    def test_dev_by_zero(self):
        with self.assertRaises(ZeroDivisionError):  # тут мы тестим на содержание ошибки
            dev(10,0)