class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        
        chars = set()

        freqt = dict()

        for c in t:
            chars.add(c)
            if c in freqt:
                freqt[c] += 1
            else:
                freqt[c] = 1

        smallest = math.inf
        shortest = (0, 0)

        count = 0
            
        i = 0
        j = 0

        for j in range(len(s)):

            letter = s[j]

            if letter in chars:
                if freqt[letter] > 0:
                    count += 1
                freqt[letter] -= 1
            
            while count == len(t):
                if smallest > j - i:
                    smallest = j - i
                    shortest = (i, j)

                letter = s[i]

                if letter in chars:
                    freqt[letter] += 1

                    if freqt[letter] > 0:
                        count -= 1
                
                i += 1

            result = ""

            for k in range(shortest[0], shortest[1] + 1):
                result += s[k]

        if smallest == math.inf:
            return ""

        return result
                

                

                

        













                

            