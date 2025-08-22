# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        #if its null then return 0, our base case for backtracking
        if root == None:
            return 0
        
        #each call in stack has its own sum, no problem with resetting
        sm = 0

        #if its left node, and it has no children -> left leaf
        if root.left and not root.left.left and not root.left.right:
            sm = sm + root.left.val
        
        #DFS check both subtrees -> 
        sm = sm + self.sumOfLeftLeaves(root.left)
        sm = sm + self.sumOfLeftLeaves(root.right)

        return sm