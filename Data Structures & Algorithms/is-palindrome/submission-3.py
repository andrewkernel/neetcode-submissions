class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = []

        for i in s:
            if i.isalnum():
                p.append(i.lower())

        left, right = 0, len(p) - 1

        while left < right:
            if p[left] != p[right]:
                return False
            left += 1
            right -= 1
        return True