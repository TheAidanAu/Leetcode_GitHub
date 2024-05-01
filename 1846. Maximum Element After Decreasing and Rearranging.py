class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # make sure the array satisfies the absolute difference condition
        # while maximizing the elements.
        # Sort the array first so that we can incrementally update the elements
        # such that each element is as close to its previous element as possible
        # Taking the minimum between prev + 1 and the current element guarantees that we meet the condition while maximizing the elements.

        arr.sort()
        # because the first element hast to start wtih 1
        prev = 0
        for n in arr:
            prev = min(prev + 1, n)
        return prev

# time: O(NlogN)
# Space: O(1)