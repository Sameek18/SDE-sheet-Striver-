class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def val(root,low,high):
            if not root: return True
            if root.val<high and root.val>low:
                return val(root.left,low,root.val) and val(root.right,root.val,high)
            
            return False
        return val(root,-sys.maxsize,sys.maxsize)
    
