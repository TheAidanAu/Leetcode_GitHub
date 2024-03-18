class Solution:

    def encode(self, strs: List[str]) -> str:
        # store length of str before each string and delimiter like '#';
        # During decoding, we iterate through the encoded string,
        # identifying the length (can be a double digit, so use two pointers) of each string by locating the # delimiter.
        # Once we have the length, we extract the corresponding string.
        res = ""
        for s in strs:
            wordLength = str(len(s))
            res = res + wordLength + "#" + s
            print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1: j+length+1]
            res.append(word)
            i = j+length+1
        return res

# for the decode function
# Time: O(N)
# Space: O(N)


