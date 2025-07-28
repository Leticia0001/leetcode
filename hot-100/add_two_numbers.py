# Time Complexity: O(max(n, m))
# - n and m are the lengths of the two linked lists l1 and l2.
# - We traverse both lists once, digit by digit.
#
# Space Complexity: O(max(n, m))
# - We construct a new linked list for the result.
# - The length of the result list is at most max(n, m) + 1 (in case of final carry).
#
# Idea:
# Simulate elementary school addition:
# - Use two pointers to traverse both linked lists digit by digit.
# - At each step, add the two digits along with any carry from the previous step.
# - Create a new node for the digit in the sum (total % 10).
# - Track carry using integer division (carry = total // 10).
# - Use a dummy head to simplify appending new nodes.
# - Continue the loop until both lists are exhausted and carry is 0.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


#build linked list
def build_linked_list(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# print linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Test Case
l1 = build_linked_list([2, 4, 3])  # 代表數字 342
l2 = build_linked_list([5, 6, 4])  # 代表數字 465

sol = Solution()
result = sol.addTwoNumbers(l1, l2)

# 預期結果：7 -> 0 -> 8 -> None（因為 342 + 465 = 807）
print_linked_list(result)
