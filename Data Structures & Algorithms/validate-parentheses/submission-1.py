class Solution:
    def isValid(self, s: str) -> bool:
        checkStack = { ")":"(",
        "}":"{",
        "]":"["
        }
        
        stack = []

        for bracket in s:
            if bracket in checkStack:
                if not stack:
                    return False
                top = stack.pop()
                if top != checkStack[bracket]:
                    return False
            else:
                stack.append(bracket)
        return not stack