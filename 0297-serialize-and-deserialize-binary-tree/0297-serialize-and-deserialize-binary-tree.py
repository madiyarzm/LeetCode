# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""

        lst = []
        q = deque()
        q.append(root)

        while q:
            root = q.popleft()

            if root is None:
                lst.append("null")
                continue

            lst.append(str(root.val))
            q.append(root.left)
            q.append(root.right)
        
        return ' '.join(lst)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None


        vals = deque(data.split())
        root = TreeNode(int(vals.popleft()))
        q = deque([root])

        while q and vals:
            node = q.popleft()

            left_val = vals.popleft()
            if left_val != "null":
                node.left = TreeNode(int(left_val))
                q.append(node.left)
            
            right_val = vals.popleft()
            if right_val != "null":
                node.right = TreeNode(int(right_val))
                q.append(node.right)

        return root
            


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))