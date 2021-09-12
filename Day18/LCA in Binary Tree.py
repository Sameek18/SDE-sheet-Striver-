 def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # base condition
        if(root is None): 
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        #Look for keys in left and right subtrees
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are Non-NULL, then one key
        # is present in once subtree and other is present in other,
        # So this node is the LCA
        
        if left is not None and right is not None:
            return root
        
        # if one subtree return null then the other if LCA.
        return left if left is not None else right
        
        