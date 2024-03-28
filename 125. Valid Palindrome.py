class Solution:
    def isPalindrome(self, s: str) -> bool:

        # remove non-alphanumeric characters
        # convert to lower cases
        # use indexing to check if the reverse is the same as the original

        converted = []

        for char in s:
            if char.isalnum():
                converted.append(char.lower())

        # join all char in the array with an empty delineator
        converted = "".join(converted)

        if len(converted) == 0 or len(converted) == 1:
            return True

        return converted == converted[:: -1]

# Time:  O(N)
# Space: O(n), n<=N , n=N if all characters are alphabets
