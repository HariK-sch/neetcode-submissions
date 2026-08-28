class Solution:
    def trap(self, height: List[int]) -> int:

        tallestLeft = [0] * len(height)
        tallestRight = [0] * len(height)

        l = 0
        r = 0

        for i in range(len(height)):
            l = max(l, height[i])
            r = max(r, height[len(height) - i - 1])

            tallestLeft[i] = l
            tallestRight[len(height) - i - 1] = r


        total = 0

        i = 0

        for j in range(len(height)):
            total += min(tallestLeft[j], tallestRight[j]) - height[j]

        return total

            
            








            
            
        