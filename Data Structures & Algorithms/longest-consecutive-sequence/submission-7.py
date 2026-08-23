class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        lowest = 1

        nums.sort()

        if len(nums) == 0:
            return 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                count += 1
            else:
                count = 1
            
            lowest = max(count, lowest)
        return lowest