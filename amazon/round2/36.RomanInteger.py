from typing import List

# 
# Tags: 
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

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def romanToInt(self, s: str) -> int:
        l = len(s)
        total = 0

        i = 0
        while i < l - 1:
            sub_val = self.subtractive_values.get(s[i] + s[i + 1])
            if sub_val:
                print("sub: " + str(sub_val))
                total += sub_val
                i += 1
            else:
                print("norm: " + str(self.values[s[i]]))
                total += self.values[s[i]]
            i += 1

        total += self.values[s[-1]] if i < l else 0
        return total


        
solution = Solution()
answer = solution.romanToInt("MCMXCIV")
print(answer)