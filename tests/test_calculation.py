from calculator.calculation import Add, Subtract, Calculation


def test_add_positive_numbers():
    calculation = Add(10, 5)
    assert calculation.get_result() == 15


def test_add_negative_numbers():
    calculation = Add(-10, -5)
    assert calculation.get_result() == -15


def test_add_mixed_numbers():
    calculation = Add(-10, 5)
    assert calculation.get_result() == -5


def test_add_zero():
    calculation = Add(10, 0)
    assert calculation.get_result() == 10


def test_add_keeps_operands_unchanged():
    calculation = Add(8, -3)
    result = calculation.get_result()

    assert result == 5
    assert calculation.a == 8
    assert calculation.b == -3


def test_subtract_positive_numbers():
    calculation = Subtract(20, 7)
    assert calculation.get_result() == 13


def test_subtract_negative_numbers():
    calculation = Subtract(-10, -5)
    assert calculation.get_result() == -5


def test_calculation_is_abstract():
    import pytest

    with pytest.raises(TypeError):
        Calculation(10, 5)


def test_polymorphic_calculations():
    calculations = [Add(10, 5), Subtract(20, 7)]
    results = [calculation.get_result() for calculation in calculations]

    assert results == [15, 13]


def test_polymorphism_with_own_numbers():
    calculations = [Add(7, 3), Subtract(4, 9), Add(-2, 6)]
    results = []

    for calculation in calculations:
        results.append(calculation.get_result())

    assert results == [10, -5, 4]
