class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        maxLen = 0
        start = 0

        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end],0)+1

            while freq[s[end]] > 1:
                freq[s[start]]-=1
                start +=1
            maxLen = max(maxLen, end-start+1)
        return maxLen
        