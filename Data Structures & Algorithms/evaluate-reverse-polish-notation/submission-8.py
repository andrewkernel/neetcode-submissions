class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
    
        for toke in tokens:
            if toke in operators:
                if toke == "+":
                    b = stack.pop()
                    a = stack.pop()

                    stack.append(b+a)
                if toke == "-":
                    b = stack.pop()
                    a = stack.pop()

                    stack.append(a-b)
                if toke == "*":
                    b = stack.pop()
                    a = stack.pop()

                    stack.append(b * a)
                if toke == "/":
                    b = stack.pop()
                    a = stack.pop()

                    stack.append(int(a/b))
            else:
                stack.append(int(toke))
        return sum(stack) 
        