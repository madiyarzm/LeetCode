# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #if its Null, then nothing
        if not root:
            return None

        #swap left with right
        root.left, root.right = root.right, root.left

        #pass same task to right subtree
        self.invertTree(root.right)

        #to the left subtree
        self.invertTree(root.left)

        return root
        
     
        


            
