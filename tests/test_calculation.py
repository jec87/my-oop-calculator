from calculator.calculation import Add


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
