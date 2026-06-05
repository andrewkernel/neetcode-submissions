class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        i = 0
        count = 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                count += 1
                i += 1
            j += 1
        return i == len(s)


                


        