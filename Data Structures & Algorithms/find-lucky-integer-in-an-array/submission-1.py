class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        res = -1

        for i in range(len(arr)):
            freq[arr[i]] = freq.get(arr[i], 0) + 1
        
        for key, value in freq.items():
            if key == value:
                res = max(res, key)

        return res
