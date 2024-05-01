class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers i, m, and n at the end of the merged array, nums1, and nums2 respectively.
        # Compare elements from the end of both arrays,
        # place the larger element at the end of nums1,
        # and decrementing corresponding pointers (m or n) accordingly.

        i = m + n - 1
        m = m - 1
        n = n - 1

        while n >= 0:
            # we only care about iterating n, the fill is completed when n == 0,
            # we no longer consider m in our fill if m is completed.
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1
    # Time: O(M+N) iterate through both arrays exactly once
    # Space: O(1)

