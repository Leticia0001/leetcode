from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list_recursively(nums):
    if not nums:
        return None
    node = ListNode(nums[0])
    node.next = build_linked_list_recursively(nums[1:])
    return node

def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

head = build_linked_list_recursively([1, 2, 3])
print_linked_list(head)