class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictNum = {}
        for num in nums:
            if num in dictNum:
                return True
            else:
                dictNum[num] = 1
        return False

# Time: O(N)
# Space: O(N)