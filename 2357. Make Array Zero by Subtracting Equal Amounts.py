class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # progressively zero the smallest non-zero elements
        # choose the smallest valid x at each step to minimize the number of operations.
        # Sorting helps in identifying the smallest non-zero elements
        nums.sort()
        count = 0
        cur = 0
        for x in nums:
            x -= cur

            if x > 0:
                cur += x
                count += 1
        return count

# Time: O(nlogn) + O(N) = O(nlogn)
# Space: O(1) Sorting the array in-place doesn't incur additional space complexity.

