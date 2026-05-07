class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l0, r0 = 0, len(numbers) - 1 # copy of initial l and r
        while l0 <= r0: # inner while: left pointer is not past right pointer
            if l0 == r0: # if left and right pointer are same, move left up, and right back to end of list
                    l0 += 1
                    r0 = len(numbers) - 1
            diff = target - numbers[l0]
            if diff == numbers[r0]:
                return [l0 + 1, r0 + 1]
            r0 -= 1