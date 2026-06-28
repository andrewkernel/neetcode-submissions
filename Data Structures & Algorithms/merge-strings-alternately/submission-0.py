class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        conjoined = ""

        while l < len(word1) or r < len(word2):
            if l < len(word1):
                conjoined += word1[l]
                l += 1
            if r < len(word2):
                conjoined += word2[r]
                r += 1
        return conjoined
    

        
        