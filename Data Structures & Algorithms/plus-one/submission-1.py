class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        one = True
        i = 0
        digits.reverse()

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = False
            else:
                digits.append(1)
                one = False
            i += 1
        digits.reverse()
        return digits


        