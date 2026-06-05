class Solution:
    def scoreOfString(self, s: str) -> int:
        
        total = 0
        for char in range(0, len(s) - 1):
            total += abs(ord(s[char + 1]) - ord(s[char]))
        return total
        