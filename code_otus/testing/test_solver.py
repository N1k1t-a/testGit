from code_otus.testing.main import Solver, dev
import pytest
from unittest.mock import patch


@pytest.fixture()
def get_solver():
    return Solver(1, 2)


@pytest.fixture()
def get_other_solver():
    return Solver(4, 2)


@pytest.fixture()
def solver_mix(request):
    a, b = request.param
    return Solver(a, b)


class TestSolver:

    @pytest.mark.parametrize(
        'params, result',
        (
                ((1, 3), 4),
                ((2, 4), 6),
                ((12, 2), 14),
        )
    )
    def test_add(self, params, result):
        solver = Solver(*params)
        assert solver.add() == result


    @pytest.mark.parametrize(  # более сложный вариант, но практичнее, потому что функция из вне класса работает
        'solver_mix, result',
            (
                ((12, 2), 14),
                ((12, 2), 14),
                ((12, 2), 14),
                ((12, 2), 14)
        ),
        indirect=['solver_mix']
    )
    def test_add_many(self, solver_mix, result):
        assert solver_mix.add() == result

    def test_mul(self, get_solver):
        assert get_solver.mul() == 2

    def test_mul_other(self, get_other_solver):
        assert get_other_solver.mul() == 8


    def test_add_random_value(self, get_solver):
        value = get_solver.add_random_value()
        assert  value <= 103 and value >= 50


    # Тут мы тестим рандомные значения путем замены рандомного значения на то, которое мы подставили с помощью patch
    # Этот процесс назыввается мокать
    def test_add_random_value(self, get_solver):
        with patch('code_otus.testing.main.random.randint', return_value=66):
            result = get_solver.add_random_value()
            assert result == 69

    # В этом примере мы будем делать мок в виде декоратора
    # @patch("code_otus.testing.main.random.randint", return_value=66)
    # def test_add_random_value_other(self, get_solver):
    #     assert get_solver.add_random_value() == 69
    # в процессе я осознал, что с декоратором в этом примере ничего не работает (мб в других норм будет)
    # так что пользуемся первым примером


# Но вне класса будет работать
@patch("code_otus.testing.main.random.randint", return_value=66)
def test_add_random_value_mocked(mock_randint):
    solver = Solver(1, 2)
    assert solver.add_random_value() == 69
    mock_randint.assert_called_once_with(1, 100)  # проверка, что randint вызвали правильно


@pytest.mark.parametrize(  # более простой способ, все прокдивается напрямую
    'a, b, result',
    (
        (4, 2, 2),
        (8, 2, 4),
        (100, 4, 25)
    )
)
def test_dev(a, b, result):
    assert dev(a, b) == result


def test_dev_exception():
    with pytest.raises(ZeroDivisionError):
        dev(10, 0)
