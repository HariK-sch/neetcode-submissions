class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        left = 1
        right = 1
        lr = [1] * len(nums)
        rl = [1] * len(nums)

        for i in range(len(nums)):
            lr[i] = left
            left *= nums[i]
            
            rl[len(nums) - i - 1] = right  
            right *= nums[len(nums) - i - 1]
            

        for i in range(len(nums)):
            result[i] = lr[i] * rl[i]

        return result