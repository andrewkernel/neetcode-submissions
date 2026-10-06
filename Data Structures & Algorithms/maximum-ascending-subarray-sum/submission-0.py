class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l, r = 0, 1

        res = 0

        # 10 20 30
        while l < len(nums):
            cur = nums[l]
            while r < len(nums) and nums[r - 1] < nums[r]:
                cur += nums[r]
                r += 1
            l = r
            r = l+1 

            res = max(res, cur)
        return res

        