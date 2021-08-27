# O(N)

def maxDepth(self, root: Optional[TreeNode]) -> int:  
    # check if there is no node
    if root==None:
        return 0
    
    # check if there is 1 node only
    elif root.right==None and root.left==None:
        return 1
    
    
    # Compute the depth of each subtree
    ltree=self.maxDepth(root.left)
    rtree=self.maxDepth(root.right)
    
    # return max height 
    return (max(ltree,rtree)+1)