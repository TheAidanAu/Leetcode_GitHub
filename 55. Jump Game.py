class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # goal is set at the end initially and iterate backwards
        # check if we can reach the goal from index i by adding the maximum jump length
        # if yes, move the goal index closer, continue
        # (look at the second last element)
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0

# Time: O(N)
# Space: O(1)

