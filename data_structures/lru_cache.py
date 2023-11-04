# from collections import deque

class Node:
    def __init__(self, key=None, value=None, next_node=None, prev_node=None):
        self.key = key  # todo consider removing
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class Deque:
    def __init__(self):
        # the head and tail are dummy nodes
        self.head = Node()
        self.tail = Node()
        self.head.next_node = self.tail
        self.tail.prev_node = self.head

    def pop(self):
        if self.head.next_node is self.tail:
            raise Exception
        self.delete(self.tail.prev_node)

    def insert_leftmost(self, node: Node):
        shifted_node = self.head.next_node
        self.head.next_node = node
        node.prev_node = self.head
        node.next_node = shifted_node
        shifted_node.prev_node = node

    def popleft(self):
        raise NotImplementedError

    def append(self):
        raise NotImplementedError

    @staticmethod
    def delete(to_delete: Node):
        prev = to_delete.prev_node
        prev.next_node = to_delete.next_node
        to_delete.next_node.prev_node = prev

    def _check(self, node: Node):
        # todo doesn't check if node is in the deque
        conditions = list()
        conditions.append(self.head.next_node is self.tail)
        # conditions.append(node.next_node is None)
        # conditions.append(node.prev_node is None)
        if any(conditions):
            raise Exception


class LRU:
    def __bool__(self):
        return True if self.capacity > 0 else False

    def __repr__(self):
        deq = list()
        head = self.deque.head
        while head:
            if head is not None:
                deq.append((head.key, head.value))
            head = head.next_node
        return str(deq)

    def __init__(self, capacity: int = 0):
        self.capacity = capacity
        self.node_map = dict()
        self.deque = Deque()

    def get(self, key: int):
        if key not in self.node_map:
            raise Exception

        # get node from map
        # delete from deque then insert leftmost
        node = self.node_map[key]
        self.deque.delete(node)
        self.deque.insert_leftmost(node)
        return node.value

    def put(self, key: int, value: int):
        if key not in self.node_map:
            self.node_map[key] = Node(key, value)  # todo consider removing key
        self.deque.insert_leftmost(self.node_map[key])

        if len(self.node_map) > self.capacity:
            pop_node = self.deque.tail.prev_node
            pop_node_key = pop_node.key
            self.deque.pop()
            del self.node_map[pop_node_key]


if __name__ == '__main__':
    lru = LRU(int(input('size: ')))
    while True:
        usr_inp = input('command: ')
        command = usr_inp.split()[0]
        if command == 'put':
            lru.put(int(usr_inp.split()[1]), int(usr_inp.split()[2]))
        elif command == 'get':
            foo = lru.get(int(usr_inp.split()[1]))
            print(foo)

        print(lru)

