class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                first = min(first, nums[l])
            
            m = (l + r) // 2
            first = min(first,nums[m])

            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        return first