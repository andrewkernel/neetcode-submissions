class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listed = {}

        for word in strs:
            s = "".join(sorted(word))

            if s not in listed:
                listed[s] = []
            listed[s].append(word)
        return list(listed.values())


        