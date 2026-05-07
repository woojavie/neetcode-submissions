class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} # sorted string: list of strings
        for n in range(len(strs)):
            sortedstr = sorted(strs[n])
            if tuple(sortedstr) in hashmap:
                hashmap[tuple(sortedstr)].append(strs[n])
            else:
                hashmap[tuple(sortedstr)] = [strs[n]]
        return list(hashmap.values())