class Solution:
    def intToRoman(self, num: int) -> str:
        # use a hashmap and add the extra spacical roman cases
        # iterate through the symbols in descending values,
        # construct the Roman numerals by taking using as large Roman as possible
        #
        lookup = {
            "I": 1, "IV": 4, "V": 5, "IX": 9,
            "X": 10, "XL": 40, "L": 50, "XC": 90,
            "C": 100, "CD": 400, "D": 500, "CM": 900,
            "M": 1000,
        }
        output = []
        for k, v in reversed(lookup.items()):
            while num > 0:
                # If v <= num, it means that the current Roman numeral symbol k can be used in the representation.
                # subtracts v from num to continue the conversion process.
                # else just move to the next symbol in the lookup table.
                if v <= num:
                    output.append(k)
                    num -= v
                else:
                    break
        return "".join(output)

# time: O(N) number of elements in the hash map
# Space: O(N) because of the output       