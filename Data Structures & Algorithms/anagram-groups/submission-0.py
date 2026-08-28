class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        for word in strs:
            chars = [0] * 26
            for c in word:
                chars[ord(c) - ord('a')] += 1

            chars = tuple(chars)

            anags = result.get(chars)

            if anags == None:
                tmp = list()
                tmp.append(word)
                result[chars] = tmp
            else:
                anags.append(word)
        
        return list(result.values())
