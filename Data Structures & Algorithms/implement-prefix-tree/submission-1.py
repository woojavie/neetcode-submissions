class TrieNode:

    def __init__(self):
        self.letters = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.letters:
                cur.letters[word[i]] = TrieNode()
            cur = cur.letters[word[i]]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.letters:
                return False
            cur = cur.letters[c]
        return cur.endOfWord
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.letters:
                return False
            cur = cur.letters[c]
        return True
        