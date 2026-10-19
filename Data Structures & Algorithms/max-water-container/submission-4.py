class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftMax, rightMax = 0, 0
        resMax = 0

        l, r = 0, len(heights)-1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
            resMax = max(resMax, area)
        return resMax
        