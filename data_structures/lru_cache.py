from dataclasses import dataclass
from typing import Self, Hashable


@dataclass
class Node:
    key: Hashable | None = None
    value: any = None
    left: Self | None = None
    right: Self | None = None


# from collections import deque
class Deque:
    def __init__(self):
        # head and tail are dummy nodes
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head

    # behavior approximately matches collections.deque.pop()
    def pop(self) -> Node:
        if self.head.right is self.tail:
            raise IndexError("IndexError: pop from empty list")
        last_node = self.tail.left
        last_node.left.right = self.tail  # or ... = last_node.right
        self.tail.left = last_node.left
        return last_node

    # noinspection SpellCheckingInspection
    def appendleft(self, node: Node) -> None:
        shifted_node = self.head.right
        self.head.right = node
        node.left = self.head
        node.right = shifted_node
        shifted_node.left = node

    def popleft(self):
        raise NotImplementedError

    def append(self):
        raise NotImplementedError

    @staticmethod
    def delete(to_delete: Node):
        left_of_delete = to_delete.left
        left_of_delete.right = to_delete.right
        to_delete.right.left = left_of_delete


class LRU:
    def __init__(self, capacity: int = 0):
        self.capacity = capacity
        self.node_map = dict()
        self.deque = Deque()

    def __bool__(self):
        return True if self.capacity > 0 else False

    def __repr__(self):
        node = self.deque.head
        return str([tuple([node := node.right, node.key, node.value][1:]) for _ in range(len(self.node_map))])

    def get(self, key: int) -> Node.value:
        if key not in self.node_map:
            return None
        node = self.node_map[key]    # get node from map
        self.deque.delete(node)      # delete from deque
        self.deque.appendleft(node)  # then insert leftmost
        return node.value

    def put(self, key: Node.key, value: Node.value) -> None:
        # check for key, add if not present
        if key not in self.node_map:
            self.node_map[key] = Node(key, value)
        else:  # update existing key and remove outdated entry
            self.node_map[key].value = value
            self.deque.delete(self.node_map[key])
        # update deque
        self.deque.appendleft(self.node_map[key])
        # impose size constraint
        if len(self.node_map) > self.capacity:
            pop_node = self.deque.tail.left
            pop_node_key = pop_node.key
            self.deque.pop()
            del self.node_map[pop_node_key]


if __name__ == '__main__':
    # format: <command> <id/key> <value>
    # limited to integer keys/values
    lru = LRU(int(input('size: ')))
    while True:
        usr_inp = input('command: ').split()
        if usr_inp[0] == 'put':
            lru.put(int(usr_inp[1]), int(usr_inp[2]))  # noqa
        elif usr_inp[0] == 'get':
            print(lru.get(int(usr_inp[1])))
        print(lru)
