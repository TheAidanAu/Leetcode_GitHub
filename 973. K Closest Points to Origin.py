class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calculate the sq distance
        # build a minHeap list to store the sq distance and the coordindates
        # heapq.heaptify the minHeap
        # then pop however many k times

        res = []
        minHeap = []
        for x, y in points:
            sqDist = x * x + y * y
            minHeap.append([sqDist, x, y])

        heapq.heapify(minHeap)

        for i in range(k):
            sqDist, x, y = heapq.heappop(minHeap)
            res.append([x, y])

        return res
    # Time: O(N) to heapify


