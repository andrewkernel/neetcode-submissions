class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = nums[0]
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] < nums[right]:
                first = min(first, nums[left])
            
            m = (left + right) // 2
            first = min(first, nums[m])

            if nums[m] >= nums[left]:
                left = m + 1
            else:
                right = m - 1
        return first
