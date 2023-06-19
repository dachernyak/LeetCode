class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        currmulty = 1
        res = 0

        for right in range(len(nums)):
            currmulty *= nums[right]
            while currmulty >= k and left <= right:
                currmulty /= nums[left]
                left += 1
            res += right - left + 1
        return res