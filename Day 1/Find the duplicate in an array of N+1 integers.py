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
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x=nums[0]
        y=nums[0]
        while(True):
            x=nums[x]
            y=nums[nums[y]]
            print(x,y)
            if x==y:
                break
        x=nums[0]
        while x!=y:
            x=nums[x]
            y=nums[y]
        else:
            return x

#Visited array
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            c=abs(nums[i])
            if nums[c]>=0:
                nums[c]=-nums[c]
            else:
                return abs(nums[i])
        
