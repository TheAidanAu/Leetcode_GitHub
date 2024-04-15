class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Initialize a has map to store character counts for the sliding window of s and string p
        # Iterate through the first window of length len(p) in s to populate sCount and pCount.
        # Then, slide the window along s, updating counts and checking for anagram matches.
        # Append the starting index of each valid anagram window to the result list res,
        # using comparisons between sCount and pCount to determine anagram matches.
        if len(p) > len(s):
            return []

        pCount, sCount = {}, {}

        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        res = [0] if sCount == pCount else []
        left = 0

        for right in range(len(p), len(s)):
            sCount[s[right]] = 1 + sCount.get(s[right], 0)
            sCount[s[left]] -= 1

            if sCount[s[left]] == 0:
                sCount.pop(s[left])
            left += 1

            if sCount == pCount:
                res.append(left)

        return res

# Time: O(max(s,p)) longer or shorter
# Space: O(s)

