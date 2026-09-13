class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        base = len(heights)-1
        maxH = 0
        start = 0
        end = len(heights)-1
        while (start < end):
            if (heights[start] < heights[end]):
                maxH = heights[start]
                start += 1
            else:
                maxH = heights[end]
                end -= 1
            if (ans < maxH*base):
                ans = maxH*base
            base -= 1
        return ans