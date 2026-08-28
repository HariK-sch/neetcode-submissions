class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for word in strs:
            code += str(len(word))
            code += "#"
            code += word

        return code

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i < len(s):
            length = ""
            word = ""

            while (s[i] != '#' and i < len(s) - 1):
                length += s[i]
                i += 1

            i += 1
                        
            if (length == ""):
                size = 0
            else:
                size = int(length)

            
            for j in range(i, i + size):
                word += s[j]
            
            i += size

            result.append(word)
                    
        return result
            
