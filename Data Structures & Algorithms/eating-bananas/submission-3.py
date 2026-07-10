
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def findK(k):
            total = 0
            
            for p in piles: 
                total += math.ceil(p/k)
            
            return total <= h
        

        l,r = 1, max(piles)

        while l < r:
            k = (l+r) // 2

            if findK(k):
                r = k
            else:
                l = k + 1
        return l

        



