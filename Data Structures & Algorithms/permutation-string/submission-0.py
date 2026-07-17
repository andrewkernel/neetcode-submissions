class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1


        seen = 0    
        for i in range(26):
            if count1[i] == count2[i]:
                seen += 1
        
        start = 0
        for end in range(len(s1), len(s2)):
            if seen == 26:
                return True
            
            endIndex = ord(s2[end]) - ord('a')
            count2[endIndex] += 1
            if count1[endIndex] == count2[endIndex]:
                seen += 1
            elif count1[endIndex] + 1 == count2[endIndex]:
                seen -= 1

            startIndex = ord(s2[start]) - ord('a')
            count2[startIndex] -= 1
            if count1[startIndex] == count2[startIndex]:
                seen += 1
            elif count1[startIndex] - 1 == count2[startIndex]:
                seen -= 1            
            start += 1
        return seen == 26
            
            

            


