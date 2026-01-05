# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        #get recursively left and right sub tree max depths
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        #count the current node and add max depths of subtrees
        return max(l,r) + 1