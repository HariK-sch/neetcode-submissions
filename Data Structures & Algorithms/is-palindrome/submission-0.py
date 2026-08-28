class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = ""

        for char in s:
            if char.isalnum():
                words += char.lower()
            
        return words == ("".join(reversed(words)))
        