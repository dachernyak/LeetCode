class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxsq = 0
        while left < right:
            sq = min(height[left],height[right]) * (right-left)
            maxsq = max(sq, maxsq)
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return maxsq