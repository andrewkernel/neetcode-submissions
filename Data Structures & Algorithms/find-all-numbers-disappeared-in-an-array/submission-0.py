class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        sortedArr = []
        res = []


        for i in range(1, len(nums)+1):
            sortedArr.append(i)

        for i in range(len(sortedArr)):
            if sortedArr[i] not in nums:
                res.append(i+1)
        return res
                    