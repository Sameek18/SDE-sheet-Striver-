#recursive
def preOrder(self, root):                                                                                                                 :
        if(root is None):
            return
        #print data,left,right
        print(root.data, end = " ")
        self.preOrder(root.left)
        self.preOrder(root.right)
        
        
#iterative
def preOrder(self,root):
    stack=[]
    l=[]#initialize empty list
    stack.append(root)
    while len(stack)>0:
        node=stack.pop()  
        # Pop all items one by one. Do following for every popped item
        # a) append to l
        # b) push its right child
        # c) push its left child
        l.append(node)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
            
    return l
        