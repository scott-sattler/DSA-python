import pytest

'''
123456
234561
456123
612345


4 5 6 1 2 3
^   |     ^

2 3 4 5 6 1
^   |     ^

6 1 2 3 4 5
^   |     ^

look for increasing
move that side

if mid < hi:
    move hi
else:
    move lo
 
will this properly converge?

->  looking for decreasing adjacent elements?

or distance of 1?


1 2 3 4 5 6
^   |     ^
^ | ^
^ ^

4 5 6 1 2 3
^   |     ^
4 5 6 1 2 3
    ^ |   ^

2 3 4 5 6 1
^   |     ^

6 1 2 3 4 5
^   |     ^

'''

def find_index(array: list, lo, hi):
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

    return find_index(array, lo, hi)


def test_min():
    test_case = [1]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 0

def test_two_no_rot():
    test_case = [1, 2]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 0

def test_two():
    test_case = [2, 1]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 1

def test_five_no_rot():
    test_case = [1, 2, 3, 4, 5]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 0

def test_five():
    test_case = [4, 5, 1, 2, 3]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 2

def test_five_leftmost():
    test_case = [5, 1, 2, 3, 4]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 1

def test_five_rightmost():
    test_case = [2, 3, 4, 5, 1]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 4

def test_six_no_rot():
    test_case = [1, 2, 3, 4, 5, 6]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 0

def test_size_six_leftmost():
    test_case = [6, 1, 2, 3, 4, 5]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 1

def test_size_six_rightmost():
    test_case = [2, 3, 4, 5, 6, 1]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 5

# zero boundary

def test_0_boundary_three_no_rot():
    test_case = [-1, 0, 1]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 0

def test_0_boundary_five_no_rot():
    test_case = [-3, -2, -1, 0, 1]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 0

def test_0_boundary_six_no_rot():
    test_case = [-4, -3, -2, -1, 0, 1]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 0

def test_0_boundary_six_leftmost():
    test_case = [1, -4, -3, -2, -1, 0]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 1

def test_0_boundary_six_rightmost():
    test_case = [-3, -2, -1, 0, 1, -4]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 5

# all negative

def test_negative_min():
    test_case = [-1]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 0

def test_negative_two_no_rot():
    test_case = [-2 -1]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 0

def test_negative_two():
    test_case = [-1, -2]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 1

def test_negative_five_no_rot():
    test_case = [-5, -4, -3, -2, -1]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 0

def test_negative_five():
    test_case = [-1, -2, -5, -4, -3]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 2

def test_negative_five_leftmost():
    test_case = [-1, -5, -4, -3, -2]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 1

def test_negative_five_rightmost():
    test_case = [-4, -3, -2, -1, -5]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 4

def test_negative_six_no_rot():
    test_case = [-6 -5, -4, -3, -2, -1]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 0

def test_negative_size_six_leftmost():
    test_case = [-1, -6 -5, -4, -3, -2]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 1

def test_negative_size_six_rightmost():
    test_case = [-5, -4, -3, -2, -1, -6]
    rot_index = find_index(test_case, 0, len(test_case) - 1)
    assert rot_index == 5
