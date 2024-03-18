class Solution:
    def maxArea(self, height: List[int]) -> int:
        # shrinking window, left/right initially at endpoints,
        # shift the pointer with shorter height;
        # (because shorter height is the bottle neck/limiting factor)
        l = 0
        r = len(height) - 1
        maxV = 0
        while l < r:
            length = r - l
            ht = min(height[l], height[r])
            vol = length * ht
            maxV = max(maxV, vol)
            # shift the pointer with min height;
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxV
# Time: O(N)
# Space: O(1)



