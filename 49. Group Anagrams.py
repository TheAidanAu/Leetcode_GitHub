class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a dictionary, the key is the frequency of each unique character in each string
        # the values are a list of anagrams
        # be careful, a dictionary key has to be immuatable, so use a tuple
        # then return these grouped anagrams
        res = defaultdict(list)  # initialize a list for a non-existing key

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()

# Time O(n*m*26) = O(n*m), 26 is from the count array, n is the # of elements in the array, m is the average length of each element
# Space O(n*m)
