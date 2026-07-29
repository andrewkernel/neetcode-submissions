class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        sol = []


        def backtrack():
            if n == len(sol):
                res.append(sol[:])
                return

            for num in nums:
                if num in sol:
                    continue
                sol.append(num)
                backtrack()
                sol.pop()
            
        backtrack()
        return res
            
            
        