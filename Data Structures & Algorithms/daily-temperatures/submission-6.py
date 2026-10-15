class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        monotonic = []

        for i in range(len(temperatures)):
            while monotonic and temperatures[i] > temperatures[monotonic[-1]]:
                prev = monotonic.pop()
                res[prev] = abs(prev - i)
            monotonic.append(i)
        return res