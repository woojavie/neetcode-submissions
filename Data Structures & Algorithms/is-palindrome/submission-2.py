class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char for char in s if char.isalnum())
        cleaned = cleaned.lower()
        i = 0
        j = len(cleaned) - 1
        while i <= j:
            if cleaned[i] != cleaned[j]:
                return False
            else:
                i += 1
                j -= 1
        return True