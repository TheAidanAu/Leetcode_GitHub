class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check if the length of each string is the same
        if len(s) != len(t):
            return False

        dictS = {}
        for char in s:
            if char not in dictS:
                dictS[char] = 1
            else:
                dictS[char] += 1
        for char in t:
            if char not in dictS:
                return False
            else:
                dictS[char] -= 1
        for v in dictS.values():
            if v != 0:
                return False
        return True

# Time: O(2N+M) = O(N), where M<=N, M is the number unique character in a string
# Space: O(M), where M<=N, M is the number unique character in a string