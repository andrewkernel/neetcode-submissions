class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = 0

        s = sorted(s)
        t = sorted(t)

        if s != t:
            return False
        return True