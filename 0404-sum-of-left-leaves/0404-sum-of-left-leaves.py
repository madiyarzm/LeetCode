# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        sm = 0
        if root.left and not root.left.left and not root.left.right:
            sm = sm + root.left.val
        
        sm = sm + self.sumOfLeftLeaves(root.left)
        sm = sm + self.sumOfLeftLeaves(root.right)

        return sm