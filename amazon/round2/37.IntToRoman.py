from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        roman_digits = []
        # Loop through each symbol.
        for value, symbol in digits:
            print("value: " + str(value))
            # We don't want to continue looping if we're done.
            if num == 0:
                break

            count = num // value
            print("count: " + str(count))
            num -= count * value

            # Append "count" copies of "symbol" to roman_digits.
            roman_digits.append(symbol * count)
        return "".join(roman_digits)

        
solution = Solution()
answer = solution.intToRoman(1994)
print(answer)