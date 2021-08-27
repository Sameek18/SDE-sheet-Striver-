

visited=set()
def dfs(visited,graph,root):
    
    if root not in visited:    # Mark the current node as visited
                               # and print it
        print(root)
        visited.add(root)
    
    for i in graph(root):    # Recur for all the vertices
                             # adjacent to this vertex
        dfs(visited,graph,i)