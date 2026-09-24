class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            k = "".join(sorted(s))

            if k not in seen:
                seen[k] = []
            seen[k].append(s)
        return list(seen.values())