def inOrder(self, root):
        if(root is None):
            return
         #print left,data,right
        self.inOrder(root.left)
        print(root.data, end = " ")
        
        self.inOrder(root.right)
        
        
        
        
#iterative solution        
def inorderTraversal(self, root: TreeNode) -> List[int]:        
        return_list = []
        stack = []
        node = root
        
        while True:
            # Reach the left most Node of the current Node
            if node is not None:
                stack.append(node)
                node = node.left
                
            elif(stack):
                node = stack.pop()
                return_list.append(node.val)
                node = node.right
            else:
                break
        return return_list