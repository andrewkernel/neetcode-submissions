class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = list(zip(heights, names))
        res.sort(reverse=True)
        return [x for height, x in res]