# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = head, head
        count = 0
        while count != n:
            first = first.next
            count += 1
        while first and first.next:
            first = first.next
            second = second.next
        if first == None:
            head = head.next
            return head
        elif second.next:
            second.next = second.next.next
        else:
            return None
        
        return head
