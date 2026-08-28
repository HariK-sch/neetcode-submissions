class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = [[] for i in nums]

        freqs = dict()

        for num in nums:
            count = freqs.get(num)
            if count == None:
                freqs[num] = 1
            else:
                freqs[num] = count + 1
            
        for item in freqs.items():
            result[item[1] - 1].append(item[0])

        ans = list()

        count = 0

        for i in range(len(nums) - 1, -1, -1):
            if len(result[i]) > 0:
                for num in result[i]:
                    if count >= k:
                        break
                        
                    ans.append(num)
                    count += 1
            
                    

        return ans
            
        
        