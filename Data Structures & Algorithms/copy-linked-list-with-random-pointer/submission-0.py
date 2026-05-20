"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        nodeMap = {}
        if not head:
            return None
        while curr:
            nodeMap[curr] = Node(curr.val)
            curr = curr.next
        for key in nodeMap:
            nodeMap[key].next = nodeMap.get(key.next)
            nodeMap[key].random = nodeMap.get(key.random)
        return nodeMap[head]