import pytest

from sequence import sequence_iter, sequence_rec


@pytest.mark.parametrize("k, expected", [
    (1, (1, 1)),
    (2, (2, 3)),
    (3, (7, 7)),
    (4, (20, 21)),
    (5, (61, 61)),
])
def test_sequence_iter(k, expected):
    assert sequence_iter(k) == expected

@pytest.mark.parametrize("k, expected", [
    (1, (1, 1)),
    (2, (2, 3)),
    (3, (7, 7)),
    (4, (20, 21)),
    (5, (61, 61)),
])
def test_sequence_rec(k, expected):
    assert sequence_rec(k) == expected