class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in range(len(nums)): 
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        sorted_nums = sorted(freq, key=freq.get, reverse=True)
        return sorted_nums[:k]