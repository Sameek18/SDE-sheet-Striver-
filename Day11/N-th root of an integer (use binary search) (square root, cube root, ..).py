def findnroot(x,n):
    if x>=0 and x<=1:  #check if x lies between 0,1
        l,h=0,1
    else:
        l,h=1,x
        
    eps=0.0000001  #used for approximation
    mid=(l+h)/2
    
    #run binary search
    
    while abs(mid**n-x)>=eps:    #running the loop till we minimise the difference between mid and the nth root
        if x<mid**n:
            h=mid
        elif x>mid:
            l=mid
            
        mid=(l+h)/2
        
    return mid