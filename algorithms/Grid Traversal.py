
matrix = [[0, 1, 0, 0],
          [1, 0, 1, 0],
          [0, 1, 0, 1],
          [0, 0, 1, 0]]

matrix2 = [[0, 1, 0, 0],
           [0, 0, 0, 0],
           [0, 1, 0, 1],
           [0, 0, 1, 0]]


def bfs_iter(arr: list[list]) -> None:
    from collections import deque

    if not arr:
        return

    visited = set()
    unvisited = deque()
    unvisited.append((0, 0))

    while unvisited:
        curr = unvisited.popleft()
        print('current:', curr)
        if curr in visited:
            continue
        visited.add(curr)

        directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
        for direction in directions:
            i = direction[0] + curr[0]
            j = direction[1] + curr[1]
            if len(arr) > i > -1 and len(arr[0]) > j > -1:
                if (i, j) not in visited:
                    unvisited.append((i, j))
                    print('seen:', (i, j))

    print(sorted(visited))


def dfs_rec(arr: list[list]) -> int:
    if not arr:
        return 0
    visited = set()
    count = [0]
    # _dfs_rec(arr, (0, 0), visited, count)
    return _dfs_rec(arr, (0, 0), visited, count)


def _dfs_rec(arr: list[list], loc, visited, count) -> int:
    if loc in visited:
        return count
    visited.add(loc)

    if arr[loc[0]][loc[1]] == 1:
        count[0] += 1

    directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
    for direction in directions:
        i = direction[0] + loc[0]
        j = direction[1] + loc[1]
        if len(arr) > i > -1 and len(arr[0]) > j > -1:
            _dfs_rec(arr, (i, j), visited, count)

    return count


count = dfs_rec(matrix)
print(count)
