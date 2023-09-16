# https://leetcode.com/problems/palindrome-number/submissions/
# Tags: Math, modulus
class Solution:

    # Runtime Complexity: O(log10(n))
    # Space Complexity: O(1)
    # Time: Not timed
    def isPalindrome(self, x: int) -> bool:
        # if x has a negative sign, it can't be a palindrome.
        # if x is higher than 0 and the last digit is 0, it also
        # can't be a palindrome because an integer can't have leading
        # 0's
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_number = 0

        while (x > reversed_number):
            # get the last digit
            last_digit = x % 10

            # trim off the last digit
            x = int(x / 10)

            # add the last digit to the beginning of the reversed number
            reversed_number = (reversed_number * 10) + last_digit

        # return the reversed number if it matches the original number. In case
        # the number has an odd amount of characters, we also check the original
        # number against a version of the reversed number that strips off the last
        # digit. e.g. 122 == (int(1223 / 10) = 122)
        return x == reversed_number or x == int(reversed_number / 10)
        
        
solution = Solution()
answer = solution.isPalindrome(1221)
answer = solution.isPalindrome(0)
answer = solution.isPalindrome(123)
print(answer)

# Example: 1221
# last_digit = x % 10 = 1221 % 10 = 1
# x = x / 10 = 1221 / 10 = 122
# reversed_number = (reversed_number * 10) + last_digit = (0 * 10) + 1 = 1
#
# last_digit = x % 10 = 122 % 10 = 2
# x = x / 10 = 122 / 10 = 12
# reversed_number = (reversed_number * 10) + last_digit = (1 * 10) + 2 = 12
#
# x = 12 is not greater than reversed_number = 12, therefore we compare the two.
# since x == reversed_number, we return true