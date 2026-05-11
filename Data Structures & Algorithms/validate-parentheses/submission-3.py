class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            '[' : ']',
            '(' : ')',
            '{' : '}'
        }
        stack = []
        for c in s:
            if c in valid:
                stack.append(c)
            else:
                if stack:
                    if valid[stack[-1]] != c:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        if stack:
            return False
        return True

