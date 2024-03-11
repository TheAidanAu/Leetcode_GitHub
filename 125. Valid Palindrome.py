class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted = ""
        for char in s:
            if char.isalnum():
                converted += char.lower()

        if len(converted) == 0 or len(converted) == 1:
            return True

        start = 0
        end = len(converted) - 1
        while start < end:
            if converted[start] == converted[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

# Time:  O(N+N/2) = N(N)
# Space: O(n), n<=N , n=N if all characters are alphabets
