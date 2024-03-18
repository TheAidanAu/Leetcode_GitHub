class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window, use a set to keep track of unique char
        # expand the window , as long as we see a dup char within curr window,
        # shrink the window until there's no dup in the curr window
        # (shift the start pointer by 1
        # remove that correspending char from the set so)
        # add unique char to the set and keep track of length (of the longest substring)
        # (when you see a dup, the dup isn't necessarily be the one on the left most,
        # you need to keep shrinking the window)

        charSet = set()
        maxLength = 0
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLength = max(maxLength, len(charSet))

        return maxLength

        # Time: O(N)
    # Space: O(N) because of the set 