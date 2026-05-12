class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif s == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num2 - num1
                stack.append(res)
            elif s == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif s == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num2 / num1
                stack.append(int(res))
            else:
                stack.append(int(s))
        return stack[-1]
            

