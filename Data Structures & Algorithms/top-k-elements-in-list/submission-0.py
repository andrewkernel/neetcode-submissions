class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res[num] += 1
            
        sorted_nums = sorted(res, key=res.get, reverse=True)

        return sorted_nums[:k]
        