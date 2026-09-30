class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        
        for word in strs:
            k = "".join(sorted(word))

            if k not in seen:
                seen[k] = []
            seen[k].append(word)
        return list(seen.values())