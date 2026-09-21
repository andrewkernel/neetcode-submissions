class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = [] 
        seen = {}

        for s in strs:
            n = "".join(sorted(s))

            if n not in seen:
                seen[n] = []
            seen[n].append(s)
        return list(seen.values())

        