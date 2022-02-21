# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
       
        result = []
        def inOrder(root,arr):
            if not root: return None

            if root.left:
                inOrder(root.left,arr)
            result.append(root.val)

            if root.right:
                inOrder(root.right,arr)

        inOrder(root,result)
        if k <= len(result) and k > 0:
            return result[k-1]
        return None

      
        
        
        
        