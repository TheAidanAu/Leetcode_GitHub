class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # have a curSum initialized as 0 and maxSum as the first integer
        # if curSum is -ve, reset to zero and continue to add numbers again
        # sum as many input numbers as possible and update on maxSum
        curSum = 0
        maxSum = nums[0]

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum)

        return maxSum

# time: O(N)
# Space: O(1)


