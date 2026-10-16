class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            l, r = i+1, len(nums)-1

            while l < r: 
                curr = nums[i] + nums[l] + nums[r]

                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        return [list(x) for x in res]