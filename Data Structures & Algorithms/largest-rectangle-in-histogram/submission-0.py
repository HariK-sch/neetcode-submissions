class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        heights.append(0)

        rectangle = 0

        stack = []

        for i in range(len(heights)):

            current = heights[i]


            while stack and current < heights[stack[-1]]:
                popped = stack.pop()

                if stack:
                    start = stack[-1]
                else:
                    start = - 1

                area = (i - start - 1) * heights[popped]
                rectangle = max(rectangle, area)

            stack.append(i)

        return rectangle











