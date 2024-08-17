class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Recursive DFS with a pointer at a current element
        # have a decision to include the current element,
        # also have a decision to exclude the current element,
        # recursively call the next element
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # Decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)                                                              
        return res                                    
#time: O(2^n) 2 times more choice at each level                                                                              