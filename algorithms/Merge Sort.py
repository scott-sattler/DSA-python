

def mergesort_td(arr: list):
    """
    stability untested
    """
    if len(arr) < 2:
        return arr

    mid_p = len(arr) // 2

    left = mergesort_td(arr[0:mid_p])
    right = mergesort_td(arr[mid_p:len(arr)])

    i, j = 0, 0
    merged = list()
    while i < len(left) or j < len(right):
        left_el = float('inf')
        right_el = float('inf')
        if i < len(left):
            left_el = left[i]
        if j < len(right):
            right_el = right[j]

        if left_el < right_el:
            merged.append(left_el)
            i += 1
        else:  # right_el < left_el:
            merged.append(right_el)
            j += 1

    return merged


if __name__ == '__main__':
    def run_test():
        test_cases = [
            [1, 2, 1, -1, -2, -3],
            [5, 3, 1, 4, 2],
            [0],
            [-1],
            [1],
            [-4, -2, -6, 1, -1, 0, 4, 2, 6, -8]
        ]

        for test in test_cases:
            print(mergesort_td(test))
            assert mergesort_td(test) == sorted(test)

    run_test()
