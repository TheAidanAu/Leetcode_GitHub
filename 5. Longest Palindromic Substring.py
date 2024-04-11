class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Write a helper function takes the center index/indices and attempt to expands around them
        # iternate through each character and expanmd around it to check for palindromes with odd and even lengths.
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
            # remember that l has to start at zero

        res = ""
        for i in range(len(s)):
            word = helper(i, i)
            if len(word) > len(res):
                res = word
        # handle even-length palindromes centered between i and i + 1
            word = helper(i, i + 1)
            if len(word) > len(res):
                res = word
        return res
# Time:O(N^2) for each character, we traverse to get a palamdrom with at most n length
# Space: O(1) because of the output word
