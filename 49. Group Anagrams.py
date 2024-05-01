class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a dictionary, keys would be the freq. of the unique characters in each string
        # values are a list of groupped anaagrams
        # immutable, array then make it a tuple
        res = defaultdict(list)  # initialize a list for a non-existing key

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()

# Time O(n*m*26) = O(n*m), 26 is from the count array, n is the # of elements in the array, m is the average length of each element
# Space O(n*m)
