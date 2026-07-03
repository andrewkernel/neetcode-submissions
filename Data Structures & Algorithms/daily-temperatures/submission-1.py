class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = (i-stackInd)
            stack.append([v, i])
        return result