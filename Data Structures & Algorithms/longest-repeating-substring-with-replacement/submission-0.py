class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        alpha = [0] * 26

        largest = 0

        frequent = "A"
        
        i = 0
        j = 0

        for j in range(len(s)):
            letter = s[j]

            alpha[ord(letter) - ord("A")] += 1

            count = alpha[ord(letter) - ord("A")]
            
            if count > alpha[ord(frequent) - ord("A")]:
                frequent = letter

            mostFreq = alpha[ord(frequent) - ord("A")]

            if (j - i - mostFreq + 1) > k:
                alpha[ord(s[i]) - ord("A")] -= 1
                i += 1
            
            else:
                largest = max(j - i + 1, largest)

        return largest




        