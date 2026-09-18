class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}


        for s in strs: 
            x = "".join(sorted(s))
            if x not in res:
                res[x] = []
            res[x].append(s)
        return list(res.values())