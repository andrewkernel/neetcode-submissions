class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        prefix[0] = 1
        postfix[len(nums)-1] = 1

        p1 = 1
        p2 = 1

        for i in range(1, len(nums)):
            p1 = p1 * nums[i-1]
            prefix[i] = p1
        
        for i in range(len(nums)-2, -1, -1):
            p2 = p2 * nums[i+1]
            postfix[i] = p2
        
        res = []
        for i in range(0, len(nums)):
            res.append(prefix[i]*postfix[i])
        return res

