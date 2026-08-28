class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = [0] * 26
        s2 = [0] * 26

        for char in s:
            s1[ord(char) - ord('a')] += 1
        
        for char in t:
            s2[ord(char) - ord('a')] += 1

        return s1 == s2
        