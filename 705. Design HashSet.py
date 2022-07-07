"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:
    void add(key) Inserts the value key into the HashSet.
    bool contains(key) Returns whether the value key exists in the HashSet or not.
    void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Example 1:
    Input
    ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
    [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    Output
    [null, null, null, true, false, null, true, null, false]

Explanation
    MyHashSet myHashSet = new MyHashSet();
    myHashSet.add(1);      // set = [1]
    myHashSet.add(2);      // set = [1, 2]
    myHashSet.contains(1); // return True
    myHashSet.contains(3); // return False, (not found)
    myHashSet.add(2);      // set = [1, 2]
    myHashSet.contains(2); // return True
    myHashSet.remove(2);   // set = [1]
    myHashSet.contains(2); // return False, (already removed)

Constraints:
    0 <= key <= 10^6
    At most 104 calls will be made to add, remove, and contains.
"""

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# third attempt (optimized)
class MyHashSet:

    def __init__(self):
        # sets are immutable
        self.hash_set: {int: bool} = {}

    def add(self, key: int) -> None:
        self.hash_set[key] = True

    def remove(self, key: int) -> None:
        self.hash_set[key] = False

    def contains(self, key: int) -> bool:
        return self.hash_set.get(key, False)


# second attempt
class second_attempt_MyHashSet:  # noqa

    def __init__(self):
        # sets are immutable
        self.hash_set = {k: False for k in range(10 ** 6 + 1)}

    def add(self, key: int) -> None:
        self.hash_set[key] = True

    def remove(self, key: int) -> None:
        self.hash_set[key] = False

    def contains(self, key: int) -> bool:
        return self.hash_set[key]


# first attempt (referenced discussion)
class first_attempt_MyHashSet:  # noqa

    def __init__(self):
        self.hash_set = [None] * (10 ** 6)

    def add(self, key: int) -> None:
        self.hash_set[key] = key

    def remove(self, key: int) -> None:
        self.hash_set[key] = None

    def contains(self, key: int) -> bool:
        return bool(self.hash_set[key])
