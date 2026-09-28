import pytest

from calculator.calculation import Add, Subtract
from calculator.history import History


def test_new_history_is_empty():
    history = History()
    assert history.get_history() == []


def test_add_calculation():
    history = History()
    calculation = Add(10, 5)

    history.add(calculation)

    assert history.get_history() == [calculation]


def test_add_multiple_calculations():
    history = History()
    first = Add(10, 5)
    second = Subtract(20, 7)

    history.add(first)
    history.add(second)

    assert history.get_history() == [first, second]


def test_history_returns_copy():
    history = History()
    history.add(Add(10, 5))

    snapshot = history.get_history()
    snapshot.clear()

    assert len(history.get_history()) == 1


def test_history_rejects_non_calculation():
    history = History()

    with pytest.raises(TypeError):
        history.add("not a calculation")

    assert history.get_history() == []


def test_remove_calculation():
    history = History()
    first = Add(10, 5)
    second = Subtract(20, 7)
    history.add(first)
    history.add(second)

    removed = history.remove(0)

    assert removed is first
    assert history.get_history() == [second]


def test_remove_invalid_index():
    history = History()
    calculation = Add(10, 5)
    history.add(calculation)

    with pytest.raises(IndexError):
        history.remove(-1)

    assert history.get_history() == [calculation]


def test_remove_from_empty_history():
    history = History()

    with pytest.raises(IndexError):
        history.remove(0)

    assert history.get_history() == []
