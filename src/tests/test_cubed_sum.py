import pytest

from src.cubed_sum import get_sum_of_nat, get_sum_of_cube



def test_sum_of_nat_up_to_5():
    expected = 15
    actual = get_sum_of_nat(5)
    assert expected == actual

def test_sum_of_nat_up_to_0():
    expected = 0
    actual = get_sum_of_nat(0)
    assert expected == actual

def test_sum_of_nat_cubed_up_to_3():
    expected = 36
    actual = get_sum_of_cube(3)
    assert expected == actual

def test_sum_of_nat_cubed_up_to_4():
    expected = 100
    actual = get_sum_of_cube(4)
    assert expected == actual

def test_negative_input():
    with pytest.raises(ValueError):
        get_sum_of_nat(-5)
    with pytest.raises(ValueError):
        get_sum_of_cube(-5)
