# graph traversal
def river_sizes(matrix):
    # for each element in matrix
    # check for visited (closed set)
    # check for correct value (1)
    # graph traversal (dfs/stack) until no additional connected nodes are found
    # track grouped nodes
    # add traversed nodes to closed set (visited)
    # >return count, not grouping

    closed_set = []  # visited
    connected_node_list = []
    # for each element in matrix
    for i, each_row in enumerate(matrix):
        for j, each_index in enumerate(each_row):

            # exclude visited and incorrect value (0)
            if (j, i) not in closed_set and matrix[i][j] == 1:
                dfs_stack = [(j, i)]  # seed
                connected_nodes = [(j, i)]  # seed

                # find all connected nodes
                while len(dfs_stack) > 0:
                    current_node = dfs_stack.pop(-1)
                    closed_set.append(current_node)
                    found_nodes = find_nodes(current_node, matrix)

                    if found_nodes:
                        for each_node in found_nodes:
                            # add new nodes to stack
                            if each_node not in closed_set:
                                dfs_stack.append(each_node)
                            # group adjacent nodes
                            if each_node not in connected_nodes:
                                connected_nodes.append(each_node)

                # add grouped nodes to return list
                connected_node_list.append(connected_nodes)

    # if len(connected_node_list) == 0:
    #     connected_node_list.append([])
    return sorted(list(map(lambda x: len(x), connected_node_list)))


# bounds check AND value check
def find_nodes(element: tuple[int, int], matrix):
    """ element: tuple(x, y) """
    # cardinal direction order
    found_nodes = []
    # north
    if element[1] > 0 and matrix[element[1] - 1][element[0]] == 1:
        found_nodes.append((element[0], element[1] - 1))
    # south
    if element[1] + 1 < len(matrix) and matrix[element[1] + 1][element[0]] == 1:
        found_nodes.append((element[0], element[1] + 1))
    # east
    if element[0] + 1 < len(matrix[0]) and matrix[element[1]][element[0] + 1] == 1:
        found_nodes.append((element[0] + 1, element[1]))
    # west
    if element[0] > 0 and matrix[element[1]][element[0] - 1] == 1:
        found_nodes.append((element[0] - 1, element[1]))

    if len(found_nodes) > 0:
        return found_nodes
    else:
        return None


# TESTS

matrix_test_0 = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

matrix_test_0_answer = [1, 2, 2, 2, 5]

# all 0s
matrix_test_1 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

matrix_test_1_answer = []

# all 1s
matrix_test_2 = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

matrix_test_2_answer = [len(matrix_test_2)*len(matrix_test_2[0])]

# checkerboard
matrix_test_3 = [
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1]
]

matrix_test_3_answer = [1]*13

# spiral
matrix_test_4 = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

matrix_test_4_answer = [17]

# snake
matrix_test_5 = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

matrix_test_5_answer = [17]

# empty
matrix_test_6 = [
    [0]
]

matrix_test_6_answer = []

# one
matrix_test_7 = [
    [1]
]

matrix_test_7_answer = [1]

# 1x11
matrix_test_8 = [
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]
]

matrix_test_8_answer = [1, 2, 3]

# rect misc
matrix_test_9 = [
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
]

matrix_test_9_answer = [1, 1, 2, 2, 5, 21]

# rect misc
matrix_test_10 = [
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 0],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 1]
]

matrix_test_10_answer = [1, 1, 2, 6, 10]


test_dict = {}
answer_dict = {}
for each_global in globals().copy().items():
    if "_answer" in each_global[0]:
        answer_dict[each_global[0]] = each_global[1]
    elif "matrix_test_" in each_global[0]:
        test_dict[each_global[0]] = each_global[1]

# print(test_dict)
# print(answer_dict)

for each_test in test_dict.items():
    output = river_sizes(each_test[1])
    expected = answer_dict[each_test[0] + "_answer"]
    print(each_test[0] + f"\n\toutput:   {output}\n\texpected: {expected}", )
    assert output == expected
    print("\tPASS")
