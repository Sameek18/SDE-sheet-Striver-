class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maximum = 0
        self.diameter(root)
        return self.mx
    
    def diameter(self,root): 
        #base condition
        if root==None:
            return 0
        else:
            #find height of left and right child trees
            t1 = self.diameter(root.left)
            t2 = self.diameter(root.right)
            #check if maximum is greater or current diameter
            self.maximum = max(self.maximum,t1+t2)
            return max(t1,t2)+1