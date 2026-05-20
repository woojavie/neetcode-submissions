# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        tail = head
        while l1 or l2:
            if not l1:
                if l2.val + carry > 9:
                    res = ListNode(l2.val + carry - 10)
                    carry = 1
                else: 
                    res = ListNode(l2.val + carry)
                    carry = 0
                tail.next = res
                tail = res
                l2 = l2.next
            elif not l2: 
                if l1.val + carry > 9:
                    res = ListNode(l1.val + carry - 10)
                    carry = 1
                else: 
                    res = ListNode(l1.val + carry)
                    carry = 0
                tail.next = res
                tail = res
                l1 = l1.next
            elif l1.val + l2.val + carry > 9:
                res = ListNode(l1.val + l2.val + carry - 10)
                carry = 1
                tail.next = res
                tail = res
                l1 = l1.next
                l2 = l2.next
            else:
                res = ListNode(l1.val + l2.val + carry)
                carry = 0
                tail.next = res
                tail = res
                l1 = l1.next
                l2 = l2.next
        if carry > 0:
            res = ListNode(1)
            tail.next = res
        return head.next
        
            