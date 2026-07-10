class Solution:
    def findMin(self, nums: List[int]) -> int:
        minV = nums[0] 
        for x in range(len(nums)):
            if minV > nums[x]:
                minV = nums[x]
        return minV