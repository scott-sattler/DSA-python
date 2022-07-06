from __future__ import annotations
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    # Provided
    def __init__(self, val=0, next=None):  # noqa (next shadows built-in name)
        self.val = val
        self.next = next


# nested implies recursion
def create_linked_list(number: list | tuple) -> ListNode | None:  # 3.11 -> Self
    if not isinstance(number, list):
        number = list(number)

    node = ListNode()
    if len(number) == 0:
        return None

    node.val = number.pop(0)
    node.next = create_linked_list(number)
    return node


def print_linked_list(linked_list: ListNode) -> None:
    node = linked_list
    print_list = ['reversed order']
    while node is not None:
        print_list.append(node.val)
        node = node.next
    print(print_list)


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
