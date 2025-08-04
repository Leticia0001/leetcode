# Time Complexity: O(L)
# - L is the length of the linked list.
# - We traverse the list at most twice: once to move the fast pointer n steps ahead,
#   and again with both fast and slow until fast reaches the end.
#
# Space Complexity: O(1)
# - We only use a few pointers and do not allocate extra space proportional to input size.
#
# Idea:
# Use the two-pointer (fast/slow) technique:
# - Introduce a dummy node before the head to simplify edge cases (e.g., deleting the head).
# - Move the fast pointer n steps ahead of the slow pointer.
# - Then move both pointers one step at a time until fast reaches the end.
# - At this point, slow is at the node just before the target.
# - Remove the target node by skipping it: slow.next = slow.next.next


#建置Linked List 
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def remove_nth_from_end(head:ListNode,n:int)->ListNode:
    #在Linked list前面再建一個dummy node
    dummy =ListNode(0,head)
    #Pointer:slow,fast
    fast=slow=dummy #一開始都指向dummy虛擬的頭
    
    #先讓fast提前走n步
    for _ in range(n):
        fast=fast.next
       
    #當fast的next存在(==true),則slow and fast同時走
    while fast.next:
        fast=fast.next
        slow=slow.next
        
    #修改當slow的next點要換成下下個點
    slow.next=slow.next.next
    
    return dummy.next

def print_list(head):
    while head:
        print(head.val,end="->")
        head=head.next
    print("None")
    

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

new_head=remove_nth_from_end(head,2)

print_list(new_head)