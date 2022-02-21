# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        
        if not subRoot and not root: return False
        if not subRoot or not root: return False
        
        def compare(q,p):
            if not q and not p : return True
            if not q or not p : return False
            
            if q.val != p.val:
                return False
            left = compare(q.left,p.left) 
            right = compare(q.right,p.right)
            
            return left and right
        if compare(root,subRoot):
            return True
        left = self.isSubtree(root.left,subRoot) 
        right = self.isSubtree(root.right,subRoot)
        
        
        return left or right
        
        