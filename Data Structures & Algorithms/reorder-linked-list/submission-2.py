# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # calculate midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        first = slow
        second = slow.next
        first.next = None
        # reverse second portion
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # merge two lists
        while prev:
            tmp1 = head.next
            tmp2 = prev.next
            head.next = prev
            prev.next = tmp1
            head = tmp1
            prev = tmp2
        
