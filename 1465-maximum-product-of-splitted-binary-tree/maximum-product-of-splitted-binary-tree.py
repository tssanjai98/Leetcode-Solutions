# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        modulo = (10 ** 9) + 7

        def treeSum(node):
            if not node:
                return 0
            
            return node.val + treeSum(node.left) + treeSum(node.right)
        
        sumVal = treeSum(root)

        maxVal = 0

        def subTreeSum(node):
            nonlocal maxVal
            if not node:
                return 0

            left = subTreeSum(node.left)
            right = subTreeSum(node.right)

            tmp = node.val + left + right

            maxVal = max(maxVal, tmp * (sumVal - tmp))

            return tmp
        
        subTreeSum(root)
        
        return maxVal % modulo

        