from __future__ import annotations

from typing import Optional
import warnings


# Definition for singly-linked list.
class ListNode:
    # Provided
    def __init__(self, val=0, next=None):  # noqa (next shadows built-in name)
        self.val = val
        self.next = next


# todo deprecate
def create_linked_list(number: list | tuple) -> ListNode | None:  # 3.11 -> Self
    """ warning: destructively consumes list """
    warnings.WarningMessage("deprecated: use create_ll")

    if not isinstance(number, list):
        number = list(number)

    node = ListNode()
    if len(number) == 0:
        return None

    node.val = number.pop(0)
    node.next = create_linked_list(number)
    return node


def create_ll(list_of_things: list | tuple) -> ListNode | None:
    node = ListNode()
    head = node
    for each_element in list_of_things:
        node.next = ListNode()
        node = node.next
        node.val = each_element
    return head.next


# creates looping linked list from the last node to the specified node
def create_looped_ll(list_of_things: list | tuple, loops_at: int = -1) -> ListNode | None:
    loop_reference: ListNode | None = None
    node = ListNode()
    head = node
    for i, each_element in enumerate(list_of_things):
        node.next = ListNode()
        node = node.next
        node.val = each_element
        if -1 < loops_at == i:
            loop_reference = node
    else:
        node.next = loop_reference

    return head.next


def get_depth_of_ll_node(linked_list: ListNode, find_this_node: ListNode) -> int | None:
    """ Given a node, find its index (or depth) within the provided linked list """
    index = 0
    node = linked_list
    while node:
        if node == find_this_node:
            return index
        node = node.next
        index += 1
    return None


def get_ll_node_at_depth(linked_list: ListNode, node_depth: int) -> ListNode | None:
    """ Given a node depth, return the node at the given depth """
    index = 0
    node = linked_list
    while node:
        if index == node_depth:
            return node
        node = node.next
        index += 1
    return None


def print_linked_list(linked_list: ListNode) -> None:
    node = linked_list
    print_list = ['reversed order']
    while node is not None:
        print_list.append(node.val)
        node = node.next
    print(print_list)


# beautified
def print_verbose_ll(linked_list: ListNode, get_string: bool = False) -> None | str:
    """ reference format: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: None}}}"""
    node = linked_list
    print_string = '\n'

    print_list = []
    while node is not None:
        print_list.append(node.val)
        node = node.next

    for each_node in print_list:
        print_string += 'ListNode{val: ' + f'{each_node}, next: \n'
    else:
        print_string = print_string[0:-1] + 'None' + '}' * len(print_list)

    if get_string:
        return print_string
    print(print_string)


# beautified
def get_verbose_ll_string(linked_list: ListNode) -> None:
    """ reference format: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: None}}}"""
    node = linked_list
    print_string = '\n'

    backwards_list = []
    while node is not None:
        backwards_list.append(node.val)
        node = node.next
    forwards_list = backwards_list[::-1]

    for each_node in forwards_list:
        print_string += 'ListNode{val: ' + f'{each_node}, next: \n'
    else:
        print_string = print_string[0:-1] + 'None' + '}' * len(forwards_list)

    return print_string


def ll_to_non_ll(linked_list: ListNode) -> list:
    node = linked_list
    normal_list = []
    while node is not None:
        normal_list.append(node.val)
        node = node.next
    return normal_list


def list_to_dict_key(key: list, selector: Optional[str] = None) -> tuple[tuple, tuple]:
    is_nested = False
    for each_element in key:
        if isinstance(key, list):
            is_nested = True

    if selector == "two-nested":
        return tuple(key[0]), tuple(key[1])
