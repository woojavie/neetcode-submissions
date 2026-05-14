class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            mostFreq = max(count.values())
            replacements = r - l + 1 - mostFreq
            while replacements > k:
                count[s[l]] -= 1
                l += 1
                replacements = r - l + 1 - mostFreq
            res = max(res, r - l + 1)
        return res