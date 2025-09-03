"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if not node:
                return None

            if node in oldToNew:
                return oldToNew[node]

            newNode = Node(val=node.val)
            oldToNew[node] = newNode

            for n in node.neighbors:
                oldToNew[node].neighbors.append(dfs(n))
            
            return newNode

        return dfs(node)
