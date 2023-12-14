

def mergesort_td(arr: list):
    """
    stability not tested
    """
    if len(arr) < 2:
        return arr

    mid_p = len(arr) // 2

    left = mergesort_td(arr[0:mid_p])
    right = mergesort_td(arr[mid_p:len(arr)])

    i, j = 0, 0
    merged = list()
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:  # right[j] < left[i]:
            merged.append(right[j])
            j += 1

    if j < len(right):
        left = right
        i = j
    while i < len(left):
        merged.append(left[i])
        i += 1

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
