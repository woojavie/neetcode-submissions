class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = {}
        for s in strs:
            letters = [0] * 26  # each index representing the frequency of a letter
            for letter in s:
                index = ord(letter.lower()) - 97
                letters[index] += 1
            if tuple(letters) in wordMap:
                wordMap[tuple(letters)].append(s)
            else:
                wordMap[tuple(letters)] = [s]
        return list(wordMap.values())
