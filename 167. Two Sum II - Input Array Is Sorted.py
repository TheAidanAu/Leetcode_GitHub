class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use 2 pointers pointing at the start and end
        # compute the current sum and compare with the target,
        # since the input array is sorted, if the current sum is greater than the target,
        # we need a smaller number by shifting the end point to left
        # if the current sum is smaller than the target,
        # we need a bigger number by shifting the left pointer

        l, r = 0, len(numbers) - 1

        while l < r:
            currentSum = numbers[l] + numbers[r]
            if currentSum == target:
                return l + 1, r + 1
            elif currentSum > target:
                r -= 1
            elif currentSum < target:
                l += 1

    # Time: O(N)
    # Space: O(1)







