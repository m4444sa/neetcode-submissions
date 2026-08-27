from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Store prefix products:
        # output[i] = product of all elements before i
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Multiply by suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output