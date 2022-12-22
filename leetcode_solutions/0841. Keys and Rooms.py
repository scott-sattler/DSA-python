"""
841. Keys and Rooms
Medium

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all
the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it
unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can
visit all the rooms, or false otherwise.

Example 1:
    Input: rooms = [[1],[2],[3],[]]
    Output: true
Explanation:
    We visit room 0 and pick up key 1.
    We then visit room 1 and pick up key 2.
    We then visit room 2 and pick up key 3.
    We then visit room 3.
    Since we were able to visit every room, we return true.

Example 2:
    Input: rooms = [[1,3],[3,0,1],[2],[0]]
    Output: false
Explanation:
    We can not enter room number 2 since the only key that unlocks it is in that room.

Constraints:
    n == rooms.length
    2 <= n <= 1000
    0 <= rooms[i].length <= 1000
    1 <= sum(rooms[i].length) <= 3000
    0 <= rooms[i][j] < n
    All the values of rooms[i] are unique.

"""


class Solution:
    # first attempt:
    # time complexity: O(n)
    # space complexity: O(n)
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:  # noqa: naming convention
        # edge case: first room has no keys
        if len(rooms[0]) < 1:
            return False

        # visited hashmap
        visited = {i: False for i in range(len(rooms))}
        # keys stack
        keys = [0]  # agenda
        # keys set
        key_set = {0}

        while keys:
            next_key = keys.pop()  # get next key from agenda
            visited[next_key] = True  # mark room as seen
            current_room = rooms[next_key]
            for each_key in current_room:  # for each key in current room
                # if the door exists and the key is new
                if each_key in visited and each_key not in key_set:
                    keys.append(each_key)  # add to agenda
                    key_set.add(each_key)  # add to key set

        for room in visited.values():
            if room is False:  # if not room
                return False
        return True


# taken from 0134
class TestCase:
    def __init__(self, rooms: list[list], output: bool) -> None:
        self.rooms = rooms
        self.output = output

    def __repr__(self):
        return f"{self.rooms} {self.output}"


# taken from 0134
class Test:
    # preprocessing (boundaries)
    max_rooms_fail = [[i] for i in range(1000)]
    max_rooms_pass = [[i+1] for i in range(1000)]

    test_cases: list[TestCase] = [
        # provided
        TestCase([[1], [2], [3], []], True),
        TestCase([[1, 3], [3, 0, 1], [2], [0]], False),

        # additional
        TestCase([[], [0]], False),
        TestCase([[0], []], False),
        TestCase([[2], []], False),

        # skipping larger boundary conditions
        TestCase(max_rooms_fail, False),
        TestCase(max_rooms_pass, True),

        # misc
        # skip
        TestCase([[2], [], [3], [1]], True),
        # loops
        TestCase([[2], [3], [0], [1]], False),
        TestCase([[1], [2], [3], [2]], True),
        TestCase([[1], [2], [3], [2], [4]], False),

        # failed

    ]

    def test_all(self, *include):
        """
        :param include: eg .test_all(0, 2, 5); or .test_all()
        :return: None
        """
        tests = self.test_cases
        s = Solution()

        pass_count = 0
        tests_failed = []
        for i, each_test in enumerate(tests):
            if len(include) > 0 and i not in include:
                continue
            test_input = each_test.rooms  # <--- modify as needed
            expected_output = each_test.output  # <--- modify as needed
            actual_output = s.canVisitAllRooms(test_input)  # <--- fn name here
            try:
                assert actual_output == expected_output
                print("PASS", end="")
                pass_count += 1
            except AssertionError:
                print("FAIL", end="")
                tests_failed.append(i)
            finally:

                print(f"  \t test_{i:03d}: {each_test}\n"
                      f"\t\t expd_out: {expected_output}\n"
                      f"\t\t test_out: {actual_output}\n")

        tested = len(include) if len(include) > 0 else len(tests)
        print(f'SUMMARY: TESTED {tested} | PASSED {pass_count} | FAILED {len(tests_failed)}')
        print(f'FAILED TESTS: {[f"test_{i:03d}" for i in tests_failed]}') if len(tests_failed) > 0 else print(end='')


# example usages
# Test().test_all(0, 2, 5); Test().test_all()
Test().test_all()
