 def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #condition if both trees are empty
        if not p and not q:
            return True
        #condition if one of the trees are empty
        if not p or not q:
            return False
        #check if current nodes of both tress are equal
        if p.val!=q.val:
            return False
        #check for left and right subtrees
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
        