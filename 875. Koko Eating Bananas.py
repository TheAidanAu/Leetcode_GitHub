class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # define binary serach search space
        # compute hours neededd to finish all piles
        # if hours is < h, update the res variable and search for a lower k
        # otherwise search for a higher k
        # (use binary search to search for the minimum eating speed k,
        # narrow down the search space update the speed k that
        # satisfies the given condition of eating all bananas within h hours)
            l, r = 1, max(piles)
            res = r
            while l <= r:
                k = (l + r) // 2
                hours = 0
                for p in piles:
                    hours += math.ceil(p / k)
                if hours <= h:
                    res = min(res, k)
                    r = k - 1
                else:
                    l = k + 1
            return res
        # time:  O(N log M),  N is the # of piles and M is the max eating speed/# of banans in a pile
        # space: O(1)