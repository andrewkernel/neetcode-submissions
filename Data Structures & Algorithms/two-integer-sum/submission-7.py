class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, value in enumerate(nums):
            current = target - nums[index]

            if current in seen:
                return [seen[current], index]
            
            seen[value] = index
        return False
        