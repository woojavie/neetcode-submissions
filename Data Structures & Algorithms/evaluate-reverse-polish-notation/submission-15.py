class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack
        # 1, 2 
        # pop off stack and calculate, push res back onto stack
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num1) + int(num2)
                stack.append(res)
            elif tokens[i] == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                res = int(num1) - int(num2)
                stack.append(res)
            elif tokens[i] == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                res = int(num1) / int(num2)
                stack.append(res)
            elif tokens[i] == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                res = int(num1) * int(num2)
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return int(stack.pop())
            