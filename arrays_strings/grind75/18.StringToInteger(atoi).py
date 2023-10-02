# https://leetcode.com/problems/string-to-integer-atoi/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 30:00
    #
    # Builds an integer from a string by determining its sign (+/-), trimming whitespace,
    # and then building the integer from the string, one digit at a time. All non-digits
    # after the digits are ignored, and any number outside of a signed integer is clamped
    # to the min or max
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        total = 0

        if len(s) == 0:
            return total

        i = 0

        if s[0] == '+':
            sign = 1
            i += 1
        elif s[0] == '-':
            sign = -1
            i += 1
        else:
            sign = 1
        
        for i in range(i, len(s)):
            if s[i].isdigit():
                total = total * 10
                total += int(s[i])
                i += 1
            else:
                break

        return max(min(total * sign, 2**31 - 1), (-2)**31)

        
solution = Solution()
answer = solution.myAtoi("-91283472332")
answer = solution.myAtoi('   -42 and this is cool')
print(answer)