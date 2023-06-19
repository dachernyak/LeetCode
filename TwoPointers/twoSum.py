class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(enumerate(nums), key=lambda i: i[1])
        i = 0
        j = len(nums) - 1
        while i < j:
            sum = nums[i][1] + nums[j][1]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                return [nums[i][0], nums[j][0]]