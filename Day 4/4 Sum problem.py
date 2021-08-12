#O(n**3) time complexity


def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        i=j=k=0
        n=len(nums)
        l=0
        r=0
        foursums=[]
        #sort the array
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                l=j+1
                r=n-1
                while l<r:
                    if nums[i]+nums[j]+nums[l]+nums[r]==target:
                        foursums.append([nums[i],nums[j],nums[l],nums[r]])
                        
                    elif nums[i]+nums[j]+nums[l]+nums[r]<target:
                        l+=1
                    elif nums[i]+nums[j]+nums[l]+nums[r]>target:
                        r-=1
                        
        return foursums