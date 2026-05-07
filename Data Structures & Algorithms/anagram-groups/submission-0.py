class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # list of count : list of strings
        for s in strs:
            count = [0] * 26 # a ... z
            for c in s:
                count[ord(c) - ord("a")] += 1
            if tuple(count) in res:
                res[tuple(count)].append(s)
            else:
                res[tuple(count)] = [s]
        return list(res.values())