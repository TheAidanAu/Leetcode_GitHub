class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                # because bigger values are on the left side after rotation
                # if nums[m] is bigger than nums[r] then we know that we are in subarray with bigger values
                # then we should search on the right half to find the min
                l = m + 1
            else:
                # if we shift left, we don't want to shift too left that we may skip the min
                r = m

        # as l & r converages to 2 values only, l will be pointing at the min
        return nums[l]
    # time: O(logN)
    # space: O(1)  1


