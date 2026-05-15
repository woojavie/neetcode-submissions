# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        index = -1

        curr = head

        while curr:
            if curr not in visited:
                visited.add(curr)
            else:
                return True
            curr = curr.next
        return False