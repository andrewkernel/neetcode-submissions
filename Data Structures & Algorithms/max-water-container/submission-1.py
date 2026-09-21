class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        totalVal = 0

        while l < r:
            width = r - l
            smaller = min(heights[l], heights[r])
            totalVal = max(smaller * width, totalVal)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return totalVal

        