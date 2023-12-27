from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product, postfix_product, result = 1, 1, [0]*n

        for i in range(len(nums)):
            result[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(n-1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        return result


tmp = Solution()
tmp.productExceptSelf([4, 4, 5])
