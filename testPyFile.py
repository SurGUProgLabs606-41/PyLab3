import pytest

from linearization import linearize_iter, linearize_rec
from sequence import sequence_iter, sequence_rec


@pytest.mark.parametrize("k, expected", [
    (1, (1, 1)),
    (2, (2, 3)),
    (3, (6, 7)),
    (4, (14, 19)),
    (5, (34, 47))
])
def test_sequence_iter(k, expected):
    assert sequence_iter(k) == expected

@pytest.mark.parametrize("k, expected", [
    (1, (1, 1)),
    (2, (2, 3)),
    (3, (6, 7)),
    (4, (14, 19)),
    (5, (34, 47))
])
def test_sequence_rec(k, expected):
    assert sequence_rec(k) == expected

@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, [3, 4, [5, [6, []]]]], [1, 2, 3, 4, 5, 6]),
    ([], []),
    ([1, [2, [3, [4]]]], [1, 2, 3, 4]),
    ([[[1]], 2, [[3, 4], 5]], [1, 2, 3, 4, 5])
])
def test_linearize_iter(input_list, expected):
    assert linearize_iter(input_list) == expected

@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, [3, 4, [5, [6, []]]]], [1, 2, 3, 4, 5, 6]),
    ([], []),
    ([1, [2, [3, [4]]]], [1, 2, 3, 4]),
    ([[[1]], 2, [[3, 4], 5]], [1, 2, 3, 4, 5])
])
def test_linearize_rec(input_list, expected):
    assert linearize_rec(input_list) == expected
