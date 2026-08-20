class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = float('-inf')

        nums3 = nums1 + nums2
        nums3.sort()

        m = len(nums3) // 2
        if len(nums3) % 2 == 0:
            res = (nums3[m-1] + nums3[m]) / 2
        else:
            res = nums3[m]
        return res
        