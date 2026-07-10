class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1

        while start <= end: 
            midpoint = (start + end) // 2

            if nums[midpoint] > target:
                end -= 1
            else:
                start += 1
            
            if nums[midpoint] == target: 
                return midpoint
        return -1