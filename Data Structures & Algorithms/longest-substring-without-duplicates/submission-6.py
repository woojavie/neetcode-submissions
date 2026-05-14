class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        maxL = 1
        res = 1
        if len(s) > 0:
            sub = s[0]
        else:
            return 0
        while r < len(s):
            if s[r] not in sub:
                sub += s[r]
                maxL += 1
                r += 1
                res = max(res, maxL)
            else:
                res = max(res, maxL)
                l += 1
                r = l + 1
                sub = s[l]
                maxL = 1
        return res