class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #initialize empty dictionary
        store=dict()
        diff=0
        for i in range(len(nums)):
            #find pair forming in nums[u]
            diff=target-nums[i]
            #store that number in dict if not already there
            if diff not in store:
                store[nums[i]]=i
            #if that element is found return position of both elements
            else:
                return [store[diff],i]
