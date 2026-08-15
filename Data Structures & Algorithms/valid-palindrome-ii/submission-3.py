class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                left = l + 1
                right = r

                while left < right:
                    if s[left] != s[right]:
                        break
                    left += 1 
                    right -= 1
                else:
                    return True
                
                
                left = l
                right = r - 1

                while left < right:
                    if s[left] != s[right]:
                        return False
                    left += 1 
                    right -= 1
                else:
                    return True
            l += 1
            r -= 1
        return True