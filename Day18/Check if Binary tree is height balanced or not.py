# O(N**2)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
            if root==None:    # base condition
                return True
            
            # for left and right subtree height
            lh=self.height(root.left)
            rh=self.height(root.right)
            return abs(lh-rh)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right) 
                
     # function to find height of binary tree      
    def height(self, root: Optional[TreeNode]) ->int:

            if root==None:   # base condition
                return 0

            return max(self.height(root.left),self.height(root.right))+1
