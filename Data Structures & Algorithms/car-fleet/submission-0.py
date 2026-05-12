class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = list(zip(position, speed))
        res = len(position)
        cars.sort(reverse=True)

        for c in range(len(cars)):
            time = (target - cars[c][0]) / cars[c][1]
            if stack and time <= stack[-1]:
                res -= 1
            else:    
                stack.append(time)
        return res
