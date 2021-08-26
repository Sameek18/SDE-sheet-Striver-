# Naive solution

# run 2 loops

def maxLen(n, arr):
    maxlen=0
    for i in range(len(arr)):
        csum=0
        for j in range(i,len(arr)):
            csum+=arr[j]
            if csum==0:
                maxlen=max(maxlen,(j-i+1))
            
    return maxlen




#Optimized solution using hashing


def maxLen(n, arr):
    hmap={}
    mlen=0
    csum=0
    for i in range(len(arr)):
        
        csum+=arr[i]   #add current element to the sum
        
        if arr[i]==0 and mlen==0:
            mlen=1
            
        if csum==0:   #whenever 0 sum is encountered update mlen
            mlen=i+1
            
        
        if csum in hmap:  #check if csum is present in hmap
            mlen=max(mlen,i-hmap[csum]) #update the value of mlen to max diff of (current index and index in the hmap) and max_len.
            
        else:
            hmap[csum]=i  #put the csum in hmap, with the index as a key-value pair
            
            
    return mlen
        