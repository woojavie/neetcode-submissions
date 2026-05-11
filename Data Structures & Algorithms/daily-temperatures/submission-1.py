class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures) # list of 0s length of temps
        for i in range(len(temperatures)): # check each temperature

            while stack and temperatures[i] > temperatures[stack[-1]]: # while stack is not empty
                res[stack[-1]] = i - stack[-1]                         # and current temp is hotter than top of stack
                stack.pop()                                            # add index diff to result array and pop stack
            else:
                stack.append(i) # if stack is empty or temp is cooler, push index to stack
       # add 0s to the correct indices of the result array
        return res