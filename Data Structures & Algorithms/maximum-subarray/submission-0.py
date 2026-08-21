class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        cur = nums[0]

        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            maxSub = max(maxSub, cur)
        return maxSub

        