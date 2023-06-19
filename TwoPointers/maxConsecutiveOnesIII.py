class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # если встречаем 0, то увеличиваем количество нулей + проверяем, если слева был ноль, то свободный слот для ноля освободился
        res = left = right = 0
        count_zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                while count_zeros >= k:
                    if nums[left] == 0:
                        count_zeros -= 1
                    left += 1
                count_zeros += 1
            res = max(res,right-left+1)

        return res