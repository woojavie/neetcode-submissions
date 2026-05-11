class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+", "-", "*", "/"]
        stack = []
        for c in tokens: # loop through tokens
            if c in operands:
                result = 0
                num1 = stack.pop()
                num2 = stack.pop()
                if c == "+":
                    result = num2 + num1
                elif c == "-":
                    result = num2 - num1
                elif c == "*":
                    result = num2 * num1
                else:
                    result = num2 / num1
                stack.append(int(result))
            else:
                stack.append(int(c))
        return stack[-1]
