class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use a dict to keep track of the occurrences of each char
        # use sliding window to expand as long we can replace k char
        # iterate through the input, calculate the number of replacement needed
        # (we want to replace the least frequent char)
        # (i.e. windowLen -#occurrence of highest)
        # if the conidition holds, update the length,
        # as long as it doesn't hold, decrement from the dict, and shrink the window
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

# time: O(N*26) = O(N)
# space: O(N) for the dict, if they input contains 26 characters
