class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        check = [0] * 26

        for c in s1:
            check[ord(c) - ord('a')] += 1

        perm = [0] * 26

        i = 0
        j = len(s1) - 1

        for k in range(len(s1)):
            perm[ord(s2[k]) - ord('a')] += 1

        if perm == check:
            return True

        while j < len(s2) - 1:

            j += 1
            
            perm[ord(s2[j]) - ord('a')] += 1
            perm[ord(s2[i]) - ord('a')] -= 1

            i += 1

            if perm == check:
                return True

            
        
        return False

        