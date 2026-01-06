# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        #global value that will be updated
        d = 0
        
        def max_dfs(node):

            nonlocal d

            if not node:
                return 0
            
            left = max_dfs(node.left)
            right = max_dfs(node.right)

            #we still just find max depth between left and right subtrees given
            #so one parent higher we can get local nodes diameter

            d = max(d, left + right)

            return 1 + max(left, right)

        
        max_dfs(root)


        return d

