class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use l, r pointers, find the mid point
        # if the mid point val is too small, shift the l pointer to the mid
        # if the mid point val is too big, shift the r pointer to the mid
        l, r = 0, len(nums) - 1

        # it's possible that both pointers meet as they converge
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1  # because we alread looked at m
            elif nums[m] < target:
                l = m + 1  # because we alread looked at m
            else:
                return m
        return -1
    # time: O(logN) search space is halved at each iteration
    # space: O(1)

