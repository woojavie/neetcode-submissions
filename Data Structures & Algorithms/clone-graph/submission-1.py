"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloneMap = {}
        def dfs(node):
            if node in cloneMap:
                return
            cloneMap[node] = Node(node.val, [])
            for n in node.neighbors:
                dfs(n)
                cloneMap[node].neighbors.append(cloneMap[n])
            return cloneMap[node]
        return dfs(node)

