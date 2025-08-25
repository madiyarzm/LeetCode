# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        seen = set()

        def dfs(node):
            
            #didnt find pair here
            if node is None:
                return False
            
            if k - node.val in seen:
                return True
            
            seen.add(node.val)
        
        #acts as Boolean OR, if at least one path finds it, returns TRUE
            return dfs(node.left) or dfs(node.right)
    
        return dfs(root)