class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # remove dup nums with a set
        # iterates over each element in the input list,
        # checking if it's the start of a consecutive sequence (i.e. if num-1 doesn't exist)

        # keep a counter to keep track of the current length and update the longest
        # check if consecutive nums exist, e.g. num, num+1, num+2, num+3 ....
        # so the length counter is useful because you don't want to count just the next +1

        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1

                longest = max(length, longest)

        return longest

# Time: O(N+N) = O(N) we visit each number twice at most
# Space: O(N) we create a set which takes up memory




