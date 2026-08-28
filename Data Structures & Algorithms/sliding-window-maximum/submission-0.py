class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq = deque()

        result = list()

        for j in range(len(nums)):

            while (dq) and (nums[j] > nums[dq[-1]]):
                dq.pop()

            dq.append(j)

            if dq[0] == j - k:
                dq.popleft()

            if j >= k - 1:
                result.append(nums[dq[0]])
    
        return result
                
            






