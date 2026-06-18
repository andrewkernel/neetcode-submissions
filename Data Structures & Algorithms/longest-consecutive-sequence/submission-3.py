class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        lowest = 1
        count = 1


        for num in range(1, len(nums)):
            if nums[num] == nums[num - 1]:
                continue
            if nums[num] == nums[num-1] + 1:
                count += 1
            else:
                count = 1
            
            lowest = max(lowest, count)
        return lowest



            
        