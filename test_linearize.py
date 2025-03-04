import pytest

from linearization import linearize_iter, linearize_rec


@pytest.mark.parametrize("func", [linearize_iter, linearize_rec])
def test_empty_list(func):
    assert func([]) == []

@pytest.mark.parametrize("func", [linearize_iter, linearize_rec])
def test_flat_list(func):
    assert func([1, 2, 3, 4]) == [1, 2, 3, 4]

@pytest.mark.parametrize("func", [linearize_iter, linearize_rec])
def test_nested_list(func):
    assert func([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6]

@pytest.mark.parametrize("func", [linearize_iter, linearize_rec])
def test_deeply_nested_list(func):
    assert func([[[1]], [[2, [3, [4, 5]]]]]) == [1, 2, 3, 4, 5]

@pytest.mark.parametrize("func", [linearize_iter, linearize_rec])
def test_list_with_empty_lists(func):
    assert func([1, [], [2, [], [3, []]]]) == [1, 2, 3]

@pytest.mark.parametrize("func", [linearize_iter, linearize_rec])
def test_list_with_different_types(func):
    assert func(["a", ["b", ["c", 1]], 2]) == ["a", "b", "c", 1, 2]

if __name__ == "__main__":
    pytest.main()