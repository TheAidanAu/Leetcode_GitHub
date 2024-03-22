class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # check if mid is in the l sorted or r sorted array by comparing to the edge,
        # if target are bounded by the edge and m, limit the search space to there

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
# Time: o(lon N)
# space: O(1)
