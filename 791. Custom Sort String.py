class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Use a lookup hash map to map char in the input order string based on the position
        # Sort the string s using the custom key lambda function,
        # Characters not present in order are sorted after the ordered char
        lookup = defaultdict(int)
        orderIdx = 0
        for c in order:
            lookup[c] = orderIdx
            orderIdx += 1

        return "".join(sorted(s, key= lambda x:lookup.get(x, len(s)-1)) )

    # time: O(NlogN) n is the number of chracters in s
    # space: O(M+N) for the new string built from a list and the dict

