class Solution:
    def isPalindrome(self, s: str) -> bool: 
        s2 = "".join(char.lower() for char in s if char.isalnum())
        
        l, r = 0, len(s2)-1

        while l <= r:
            if s2[l] != s2[r]:
                return False
            l += 1
            r -= 1
        return True

        