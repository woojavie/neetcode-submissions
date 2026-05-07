class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorteds = "".join(sorted(s))
        sortedt = "".join(sorted(t))
        return sorteds == sortedt