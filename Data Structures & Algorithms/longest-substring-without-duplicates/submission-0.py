class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        i = 0
        j = 0

        letters = set()

        while j < len(s):
            if s[j] in letters:
                while s[i] != s[j]:
                    letters.discard(s[i])
                    i += 1
                letters.discard(s[i])
                i += 1
            
            letters.add(s[j])

            j += 1

            longest = max(longest, j - i)

        return longest
        