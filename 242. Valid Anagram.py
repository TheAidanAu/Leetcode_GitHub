class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Iterate the first string, Use a dict to store each character's frequency
        # Iterate the second string, decrement each character's frequency
        # see if every value in the dict is 0

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

# Time: O(2N) = O(N)
# Space: O(2N) = O(N)