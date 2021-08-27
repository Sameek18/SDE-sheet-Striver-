def LeftView(root):
    ans=[]
    
    # base condition if there is no root return empty list
    if root is None:
        return ans
    
    # append the first element in the queue
    queue=deque([])
    queue.append(root)
    while len(queue)!=0:
        level=len(queue)
        
        for i in range(level):
            #pop thi first element 
            current=queue.popleft()
            #append only if the index of this element is 0 ie it is the first element of that particular level 
            
            if i==0:
                ans.append(current.data)
                
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
                
            
        
    return ans