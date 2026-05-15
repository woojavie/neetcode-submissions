# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next == None:
            return head
        curr = head
        prev = None
        while curr:
            if curr.next == None:
                curr.next = prev
                head = curr
                break
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next 
        return head