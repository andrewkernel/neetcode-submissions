class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in range(len(nums)) :
            freq[nums[num]] = freq.get(nums[num], 0) + 1
        sorted_nums = sorted(freq, key=freq.get, reverse=True)
        return sorted_nums[:k]