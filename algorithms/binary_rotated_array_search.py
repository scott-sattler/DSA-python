# time: O(log n)
# space: O(log n) (recursive call stack)
def find_index_rec(array: list, lo, hi):
    """ finds zero index of rotated, sorted array """
    if len(array) < 2:
        return 0

    mid = lo + (hi - lo) // 2

    if (hi - lo) <= 2:
        if array[mid] > array[hi]:
            return hi
        if array[lo] < array[mid]:
            return lo
        return mid

    if array[mid] < array[hi]:
        hi = mid
    else:  # array[lo] > array[mid]
        lo = mid

    return find_index_rec(array, lo, hi)


# time: O(log n)
# space: O(1) auxiliary space
def find_index_iter(array: list):
    """ finds zero index of rotated, sorted array """
    if len(array) < 2:
        return 0

    lo = 0
    hi = len(array) - 1

    while (hi - lo) > 2:
        mid = lo + (hi - lo) // 2

        if array[mid] < array[hi]:
            hi = mid
        else:  # array[lo] > array[mid]
            lo = mid

    if array[lo+1] > array[hi]:
        return hi
    if array[lo] < array[lo+1]:
        return lo
    return lo+1


# time: O(n)
# space: O(1)
def remove_rotation(array: list, zero_index):
    if zero_index == 0:
        return array

    i = 0
    j = zero_index
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        if j < len(array) - 1:
            j += 1
    return array

# todo: write tests for remove_rotation

import pytest

test_cases = {
    # positive
    (1,): 0,
    (1, 2): 0,
    (2, 1): 1,
    (1, 2, 3, 4, 5): 0,
    (4, 5, 1, 2, 3): 2,
    (5, 1, 2, 3, 4): 1,
    (2, 3, 4, 5, 1): 4,
    (1, 2, 3, 4, 5, 6): 0,
    (6, 1, 2, 3, 4, 5): 1,
    (2, 3, 4, 5, 6, 1): 5,

    # about zero boundary
    (-1, 0, 1): 0,
    (-3, -2, -1, 0, 1): 0,
    (-4, -3, -2, -1, 0, 1): 0,
    (1, -4, -3, -2, -1, 0): 1,
    (-3, -2, -1, 0, 1, -4): 5,

    # negative
    (-1,): 0,
    (-2, -1): 0,
    (-1, -2): 1,
    (-5, -4, -3, -2, -1): 0,
    (-2, -1, -5, -4, -3): 2,
    (-1, -5, -4, -3, -2): 1,
    (-4, -3, -2, -1, -5): 4,
    (-6 -5, -4, -3, -2, -1): 0,
    (-1, -6 -5, -4, -3, -2): 1,
    (-5, -4, -3, -2, -1, -6): 5,
}
test_cases = [(k, v) for k, v in test_cases.items()]

@pytest.mark.parametrize("input_array, expected_value", test_cases)
def test_rec_rotated_index_search(input_array: list, expected_value: int):
    test_fn = find_index_rec
    rot_index = test_fn(input_array, 0, len(input_array) - 1)
    assert rot_index == expected_value

@pytest.mark.parametrize("input_array, expected_value", test_cases)
def test_iter_rotated_index_search(input_array: list, expected_value: int):
    test_fn = find_index_iter
    rot_index = test_fn(input_array)
    assert rot_index == expected_value
