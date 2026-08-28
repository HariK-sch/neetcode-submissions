class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0

        i = 0
        j = len(heights) - 1

        while i < j:
            taller = min(heights[i], heights[j])
            largest = max(largest,taller * (j - i))

            if heights[i] < heights[j]:
                i += 1
            
            elif heights[i] > heights[j]:
                j -=1
            
            else:
                i += 1
                j -= 1

        return largest
            