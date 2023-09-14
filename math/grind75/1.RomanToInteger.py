# https://leetcode.com/problems/roman-to-integer/
# Tags: math, roman numerals, string parsing
class Solution:

    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    subtractive_values = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 32:00
    def romanToInt(self, s: str) -> int:
        total = 0
        l = len(s)

        # loop through roman numerals
        i = 0
        while (i < l - 1):
            # if roman numeral is I, X, or C, immediately check the next
            # numeral to see if its V, L, D, or M. The following are valid:
            # IV, IX, XL, XC, CD, or CM and nothing else
            val = self.subtractive_values.get(s[i] + s[i + 1])
            if val:
                total += val

                # skip the next iteration because subtractive numerals are two
                # digits
                i += 2
                continue

            total += self.values.get(s[i])
            i += 1

        # we want to avoid an out of index error in the loop, so we add the
        # last value here
        if i < l:
            total += self.values.get(s[i])

        return total
        
solution = Solution()
#5answer = solution.romanToInt('III')
answer = solution.romanToInt('MCMXCIV') # Returns 1994
print(answer)