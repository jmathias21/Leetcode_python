# https://leetcode.com/problems/number-of-1-bits/
# Tags: bit manipulation, hamming weight, Bitwise AND, Right Shift
class Solution:

    # Runtime Complexity: O(1)
    # Space Complexity: O(1)
    # Time: 45:00
    #
    # For each loop iteration, we check to see if the last bit is a 1
    # and if it is, we increase our total by 1. Then we chop off the
    # last bit and iterate again until the number goes to 0
    #
    # Note: The integer passed into this function is just a normal
    # integer. e.g. 1, 2, 3, 4, 5 etc. It is not passed as binary.
    def hammingWeight(self, n: int) -> int:
        total = 0

        while n > 0:
            # if n = 13, the binary is 1011. 1011 & 0001 = 0001,
            # which adds 1 to the total
            total += n & 1

            # chop off the last bit. So 1011 becomes 0101
            n = n >> 1

        return total            

        
solution = Solution()
answer = solution.hammingWeight(13)
print(answer)

# Example: n = 13 (binary = 1011)
# total += 1011 & 0001 = 1
# total = 1
# n = 1011 >> 1 = 0101
#
# total += 0101 & 0001 = 1
# total = 2
# n = 0101 >> 1 = 0010
#
# total += 0010 & 0001 = 0
# total = 2
# n = 0010 >> 1 = 0001
#
# total += 0001 & 0001 = 1
# total = 3
# n = 0001 >> 1 = 0000
#
# Since n = 0000, we return the total