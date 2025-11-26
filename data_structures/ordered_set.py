from __future__ import annotations
from typing import Any


class Node:
    def __init__(self, data: Any, prev_node: Node = None, next_node: Node = None):
        self.data = data
        self.prev = prev_node
        self.next = next_node

    def __str__(self):
        prev_data = self.prev.data if self.prev else None
        next_data = self.next.data if self.next else None
        return f"Node(data={self.data}, prev={prev_data}, next={next_data})"


class DoublyLinkedList:
    def __init__(self, *args):
        self._head = Node(None)
        self._tail = Node(None)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._length = 0

        for arg in args:
            self.append(arg)

    def __repr__(self):
        return ' <-> '.join(f'Node({node.data})' for node in self)

    def __iter__(self):
        curr = self._head.next
        while curr != self._tail:
            yield curr
            curr = curr.next

    def to_list(self) -> list:
        curr = self._head.next
        doubly_linked_list = []
        while curr != self._tail:
            doubly_linked_list.append(curr)
            curr = curr.next
        return doubly_linked_list

    def get_head(self):
        return self._head

    def insert_after(self, insertion_node: Node, prev_node: Node):
        """ Insert as the successor (i.e. to the right of) `prev_node`. """
        insertion_node.prev = prev_node
        insertion_node.next = prev_node.next
        prev_node.next.prev = insertion_node
        prev_node.next = insertion_node
        self._length += 1

    def insert_before(self, insertion_node: Node, next_node: Node):
        """ Insert as the predecessor (i.e. to the left of) `next_node`. """
        insertion_node.next = next_node
        insertion_node.prev = next_node.prev
        next_node.prev.next = insertion_node
        next_node.prev = insertion_node
        self._length += 1

    def append(self, data):
        """ Insert as the last element of the doubly linked list. """
        new_node = Node(data)
        self.insert_before(new_node, self._tail)
        return new_node

    def prepend(self, data):
        """ Insert as the first element of the doubly linked list. """
        new_node = Node(data)
        self.insert_after(new_node, self._head)
        return new_node

    def remove_node(self, node: Node) -> bool:
        """ Remove `node` from the doubly linked list. """
        if self._length < 1:
            return False
        node.prev.next = node.next
        node.next.prev = node.prev
        self._length -= 1
        return True

    def pop_first(self) -> Node:
        """ Remove and return the first node from the doubly linked list. """
        pop_node = self._head.next
        self.remove_node(pop_node)
        return pop_node

    def pop_last(self) -> Node:
        """ Remove and return the last node from the doubly linked list. """
        pop_node = self._tail.prev
        self.remove_node(pop_node)
        return pop_node

    def clear(self):
        self._head.next = self._tail
        self._tail.prev = self._head
        self._length = 0


class OrderedSet:
    def __init__(self, *args):
        # self._map = {arg: Node(arg) for arg in args}
        # self._dll = DoublyLinkedList(*args)
        self._dll = DoublyLinkedList()
        self._map = {}
        for arg in args:
            node = self._dll.append(arg)
            self._map[arg] = node

    def __repr__(self):
        # return '{' + ', '.join(str(k) for k, v in self._map.items()) + '}'
        return '{' + ', '.join(str(node.data) for node in self._dll) + '}'

    def __len__(self):
        return len(self._map)

    def __iter__(self):
        # for node_data, node in self._map.items():
        #     yield node
        for node in self._dll:
            yield node

    def __contains__(self, item):
        return item in self._map

    def add(self, item) -> bool:
        if item in self._map:
            return False
        new_node = self._dll.append(item)
        self._map[item] = new_node
        return True

    def remove(self, item):
        if item not in self._map:
            return False
        removed_node = self._map.pop(item)
        self._dll.remove_node(removed_node)
        return True

    def update(self, *others):
        """ Add elements from others. """
        ...

    def union(self, *others):
        """ Return a new OrderedSet with combined elements. """
        ...

    def intersection(self, *others):
        """ Return common elements. """
        ...

    def difference(self, *others):
        """ Return elements not in others. """
        ...

    def symmetric_difference(self, other):
        """ Return elements in either but not both. """
        ...


if __name__ == '__main__':
    _set = OrderedSet(5, 1, 2, 3, 4)
    print(_set)

    dll_01 = DoublyLinkedList()
    dll_01.insert_after(Node(2), dll_01.get_head())
    dll_01.insert_after(Node(3), dll_01.get_head())
    dll_01.insert_after(Node(1), dll_01.get_head())
    print(f'{dll_01=}')
    assert str(dll_01) == 'Node(1) <-> Node(3) <-> Node(2)'

    dll_02 = DoublyLinkedList()
    dll_02.append(3)
    dll_02.append(2)
    dll_02.append(4)
    print(f'{dll_02=}')
    assert str(dll_02) == 'Node(3) <-> Node(2) <-> Node(4)'

    dll_01.append(3)
    dll_01.append(2)
    dll_01.append(4)
    print(f'{dll_01=}')
    assert [node.data for node in dll_01.to_list()] == [1, 3, 2, 3, 2, 4]
    assert [node.data for node in dll_01] == [1, 3, 2, 3, 2, 4]

    ordered_set = OrderedSet()
    ordered_set.add(1)
    ordered_set.add(2)
    ordered_set.add(3)
    print(f'{ordered_set=}')
    assert str(ordered_set) == '{1, 2, 3}'

    ordered_set.remove(1)
    ordered_set.add(1)
    print(f'{ordered_set=}')
    assert str(ordered_set) == '{2, 3, 1}'

    for node in ordered_set:
        print(f'{node.__str__()=}')

    assert 3 in ordered_set
    assert 5 not in ordered_set