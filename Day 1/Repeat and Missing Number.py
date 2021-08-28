def findTwoElement( self,arr, n):
        d={}  # hmap
        repeat=0
        missing=0
        for i in arr:  
            if i not in d:
                d[i]=True
            else:       # if i is already present in d then it is repeating
                repeat=i
                
        for i in range(1,n+1):
            if i not in d:
                missing=i
        
                
        return (repeat, missing)


class Solution:
    def missing(self, nums):
        n=len(nums)
        x=0
        for i in range(n):
            x=x^nums[i]^(i+1)
        a,b=0,0
        x=x& ~(x-1)
        for i in range(n):
            if x&nums[i]:
                a=a^nums[i]
            else:
                b=b^nums[i]
            if x&(i+1):
                a=a^(i+1)
            else:
                b=b^(i+1)
        print(a,b)
        

