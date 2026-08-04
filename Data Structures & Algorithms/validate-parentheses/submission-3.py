class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {"}":"{","]":"[",")":"("}

        for c in s:
            if c in close:
                if not stack:
                    return False
                top = stack.pop()
                if top != close[c]:
                    return False
            else:
                stack.append(c)
        return not stack

        