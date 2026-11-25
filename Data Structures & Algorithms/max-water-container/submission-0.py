class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ma = 0
        i = 0
        n = len(heights)
        j = n-1
        while i <= j:
            a = 0
            if heights[i] < heights[j]:
                a = (j-i)*heights[i]
                ma = max(a, ma)
                i += 1
            elif heights[i] > heights[j]:
                a = (j-i)*heights[j]
                ma = max(a, ma)
                j -= 1
            else:
                ma = max(ma, (j-i)*heights[j])
                i += 1
                j -= 1
        return ma

        