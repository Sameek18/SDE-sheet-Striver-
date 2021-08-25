#using hashing

#O(n)

def singleNonDuplicate(self, nums: List[int]) -> int:
    d={}
    #create dictionary
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    #print key,whose value is less than 2       
    for k,v in d.items():
        if v<2:
            return k
        
            
#Efficient approach           
#Using Binary Search
#O(log(n))


#before single element:
# 1st occ:even  ,2nd occ:odd

#after single element:
#1st occ:odd  ,2nd occ:even

def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        while l<h:
            mid=(l+h)//2
            if mid%2==0:
                if nums[mid]==nums[mid-1]:
                    h=mid
                else:
                    l=mid
            else:
                if nums[mid]==nums[mid-1]:
                    l=mid+1
                else:
                    h=mid-1
                    
        return nums[l]
        


