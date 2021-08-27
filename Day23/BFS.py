# Time complexity:  O(N+E)===O(N) time to treaverse through each node +time to traverse through a nodes adjacent nodes

# Space complexity:  approxx  O(N) (for queue and set)


def bfs(graph,root):
    visited=set()
    queue=[]
    queue.add(root) #put root element in the queue
    while queue:
        vertex=queue.pop()   #pop the first element from the queue
        visited.add(vertex)   #add this element in the visited set
                    
        for i in graph(vertex):   #check for adjacent nodes of the vertex 
            if i not in visited:  #if they are not present in the visited set add them in queue
                queue.add(i)
                
    return visited