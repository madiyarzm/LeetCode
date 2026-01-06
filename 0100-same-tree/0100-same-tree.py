# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        #both of them doesnt exist -> good
        if not p and not q:
            return True
        
        #acting like XOR, if one of them exist other not -> not same
        if not p or not q:
            return False
        
        #if they exist, but values dont match -> not same
        if p.val != q.val:
            return False
        
        #spread this for every other node
        return (
            self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        )
