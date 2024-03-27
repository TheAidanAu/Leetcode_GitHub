class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a dict to count the occurance of each num in the input array
        # use an array to store the freq as a list of num(s)
        # create a res array for the top k frequent with the exact length of k
        # trick: iternate through the freq array from the most freq and iterate through it's value list

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

    # time: O(N+N+N+k)= O(N) 
    # space: O(N+N+k)= O(N)












