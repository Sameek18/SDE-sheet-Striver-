def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        count=0
        curr=0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+=1
            else:
                curr=max(count,curr)
                count=0
                
        return curr+1
    