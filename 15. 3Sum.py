class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort input, for each first element, left pointer is followed by the current element
        # remember the main constrint: l < r
        # Skip Duplicates: Avoid duplicate triplets by skipping identical numbers
        # during iteration and appending triplets,
        # Use Two Pointers: Iterate through each number in the sorted list.
        # For each number, use two pointers left/right on the remaining list

        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
# Time: O(NlonN) + o(N^2) for sorting and finding complients for each num = O(N^2)
# Space: O(N) because we're filling up the res array




