def inOrder(self, root):
        if(root is None):
            return
         #print left,data,right
        self.inOrder(root.left)
        print(root.data, end = " ")
        
        self.inOrder(root.right)