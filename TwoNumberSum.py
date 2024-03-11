class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictSum = {}
        for i, num in enumerate(nums):
            # see if the complient already exist in the dict
            if num in dictSum:
                # the dictSum[num] actually stores the position of the first sum
                # the current position is the position of the complient
                return dictSum[num], i
            else:
                # if the complient doesn't exist in the dict yet,
                # store the complient and the first sum's position
                dictSum[target - num] = i
        return []
