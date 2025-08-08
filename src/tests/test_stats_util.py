import numpy as np
import pytest
from math import isclose

from src.stats_util import (
    rec_moy,
    rec_variance,
    rec_ecart_type
)

sample = [9, 10, 11, 20.5, 0, 12.0, -5, -8.3]

def test_rec_moy():
    expected = np.mean(sample)
    assert isclose(rec_moy(sample), expected, rel_tol=1e-9)

def test_rec_variance():
    expected = np.var(sample)
    assert isclose(rec_variance(sample), expected, rel_tol=1e-9)

def test_rec_ecart_type():
    expected = np.std(sample)
    assert isclose(rec_ecart_type(sample), expected, rel_tol=1e-9)

@pytest.mark.parametrize("data", [
    ([1, 2, 3]),
    ([0]),
    ([-1, -2, -3]),
    ([1.5, 2.5, 3.5]),
])
def test_consistency(data):
    mean = rec_moy(data)
    var = rec_variance(data)
    std = rec_ecart_type(data)
    assert isclose(var, np.var(data), rel_tol=1e-9)
    assert isclose(std, np.std(data), rel_tol=1e-9)
    assert isclose(mean, np.mean(data), rel_tol=1e-9)