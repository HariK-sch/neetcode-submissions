class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        asc = sorted(nums)

        triplets = list()

        for k in range(len(nums) - 2):

            if (k > 0) and (asc[k] == asc[k - 1]):
                continue
            
            i = k + 1
            j = len(nums) - 1

            while (i < j):
                if (asc[i] + asc[j]) < -asc[k]:
                    i += 1

                elif (asc[i] + asc[j]) > -asc[k]:
    
                    while (asc[j] == asc[j - 1] and j > 0):
                        j -= 1
                    j -= 1


                else:
                    add = [asc[i], asc[j], asc[k]]
                    triplets.append(add)
                    while (asc[i] == asc[i + 1] and i < len(nums) - 2):
                        i += 1
                    i += 1
                    j -= 1                    
            
        return list(triplets)
