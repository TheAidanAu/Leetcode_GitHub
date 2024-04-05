class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Explore all possible combinations with and without including the candidate.

        # Decision tree, base case is curSum = or > target,
        # decision to include the current candidate
        # explore combinations including the current candidate.

        # decision to exclude the current candidate
        # After exploring combinations with the current candidate,
        # remove it from the combination cur to backtrack, and move to the next candidate by incrementing i.

        res = []
        cur = []

        def dfs(i, cur, total):
            if total == target:
                # append a copy of the current combination cur to the result res.
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

                # decision to include the current candidate
            cur.append(candidates[i])
            #  explore combinations including the current candidate.
            dfs(i, cur, total + candidates[i])

            # decision to exclude the current candidate
            # After exploring combinations with the current candidate,
            # remove it from the combination cur to backtrack, and move to the next candidate by incrementing i.
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, comb, 0)
        return res

# Time: 2^target, at most 2 decision branches at each level