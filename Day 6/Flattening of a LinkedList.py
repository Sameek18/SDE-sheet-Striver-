#merge function
#merge sort on LL, 2 lists at a time
def merge(a,b):
    #initialize a dummy node
    res=Node(0)
    temp=res
    #check if either of the list is empty
    if a==None:
        return b
    if b==None:
        return a
    #temp.bottom points to the smaller element in the two LL    
    while a!=None and b!=None:
        if a.data<b.data:
            temp.bottom=a
            temp=temp.bottom
            a=a.bottom
        else:
            temp.bottom=b
            temp=temp.bottom
            b=b.bottom
    #check for remaining elements in the LL        
    if a!=None:
        temp.bottom=a
    elif b!=None:
        temp.bottom=b
        
    return res.bottom


def flatten(root):
    #check if LL is empty or consists of 1 root
    if root==None or root.next==None:
        return root
    
    root.next=flatten(root.next)
    root=merge(root,root.next)
    
    return root


