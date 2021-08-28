# ineficient solution
def maxSubArray(self, nums: List[int]) -> int:
        max_sum=0
        for i in range(len(nums)):
            sum1=0
            for j in range(i,len(nums)):
                sum1+=nums[j]
                if sum1>max_sum:
                    max_sum=sum1
                    
        return max_sum





nums=list(map(int,input().split()))
csum=0  #maintain currentsum
msum=0   #maintain maxsum
for i in range(len(nums)):
    csum+=nums[i]        #store the sum of elements in csum
    if csum<0:
        csum=0
    elif csum>msum:      
        msum=csum
print(msum)




#when most of the numbers are negative
#DP approach
def maxSubArraySum(a,size):
     
    max_so_far =a[0]
    curr_max = a[0]
     
    for i in range(1,size):
        # we will check if value of curr sum will increse after adding i'th element or not
        curr_max = max(a[i], curr_max + a[i]) 
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far
