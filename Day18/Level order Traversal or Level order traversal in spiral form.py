

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        bfs=[]  #initialise empty list
        if root is None:  #base condition if tree is empty
            return bfs
        queue=deque([])   #initialize a queue
        queue.append(root)  #add first element in the queue
        
        while len(queue)!=0:  #the len of queue will indicate the number of elements in that particular tree level
            level=len(queue)
            current_level=[]  #this will contain nodes at each level
            
            for i in range(level):   #for each elemnt in the queue
                
                current=queue.popleft()
                current_level.append(current.val)
                
                # if current node has any children add it in the queue
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
                    
                  #all nodes of one level are appended in the final list bfs 
            bfs.append(current_level)
            
        return bfs
        