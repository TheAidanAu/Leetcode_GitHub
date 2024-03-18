class Solution:
    # make two passes, first in-order with a prefix,
    # second in-reverse with a postfix, to compute products
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            prod[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            prod[i] *= postfix
            postfix *= nums[i]

        return prod

# Time O(3n) = O(n)
# Space O(1) if The output array does not count as extra space for space complexity analysis.

