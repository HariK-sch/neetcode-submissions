class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = list()
        check = dict()
        for i in range(len(nums)):
            num = nums[i]
            result = target - num
            if result in check:
                ans.append(i)
                ans.append(check[result])
                return sorted(ans)
            check[num] = i



        