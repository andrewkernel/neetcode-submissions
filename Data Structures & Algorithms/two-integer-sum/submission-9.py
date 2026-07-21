class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, val in enumerate(nums):
            current = target - val

            if current in seen:
                return [seen[current], i]
            seen[val] = i
        return 0 
        