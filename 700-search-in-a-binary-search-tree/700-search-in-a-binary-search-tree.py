# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: return None
        
        if val < root.val:
            if root.left:
                return self.searchBST(root.left,val)
            else:
                return None
        elif val > root.val:
            if root.right:
                return self.searchBST(root.right,val)
            else:
                return None
        else:
            return root
                
            
        