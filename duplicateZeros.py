"""
Runtime: 69 ms (77.1%), Memory: 17.1 MB (7.90%)
"""

class Solution:
    def duplicateZeros(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.insert(i+1,nums[i])
                nums.pop()
                i += 2
            else:
                i +=1
