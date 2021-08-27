#sorting
#sort
#check if two consqcutive numbers are equal
def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
            
#hashmap
def findDuplicate(self, nums: List[int]) -> int:
        d={}
        #create dictionary from list
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
         #check if any value in dictinary is greater than 1
        for k,v in d.items():
            if v>1:
                return k

#Cycle method
def findDuplicate(self, nums: List[int]) -> int:
        slow=fast=nums[0]
        
        # function to find intersection point of 2 pointers
        while True:
            slow=nums[slow]  # move 1 at a time
            fast=nums[nums[fast]]   # move 2 at a time
            
            # if both pointers meet break
            
            if s==f:       
                break
                
         # to find entrance to the cycle
        f=nums[0]
        
        while f!=s:
            f=nums[f]
            s=nums[s]
            
        return s

#Visited array
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            c=abs(nums[i])
            if nums[c]>=0:
                nums[c]=-nums[c]
            else:
                return abs(nums[i])
        
