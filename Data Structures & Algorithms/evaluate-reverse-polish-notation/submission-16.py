class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                if token == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(a+b))
                if token == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b-a))
                if token == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(a*b))
                if token == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))
            else:
                stack.append(int(token))
        return sum(stack)
        