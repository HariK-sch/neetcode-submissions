class Solution:
    def search(self, nums: List[int], target: int) -> int:
        longest = math.floor(math.log2(len(nums)))        

        upper = len(nums) - 1
        lower = 0

        index = math.floor(upper / 2)

        for i in range(longest + 1):

            if nums[index] < target:
                lower = index + 1
            elif nums[index] > target:
                upper = index
            else:
                return index
            
            index = math.floor((upper + lower) / 2)

        return -1