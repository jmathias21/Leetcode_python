# https://leetcode.com/problems/reverse-bits/
# Tags: Bitwise operators, Bit manipulation, XOR, left shift, right shift, swap bits,
class Solution:

    # Runtime Complexity: O(1)
    # Space Complexity: O(1)
    # Time: 30:00
    #
    # The general solution is to get the last binary digit of n, then
    # cut off the last digit off n and add the last digit to the left most
    # position (e.g. 10000...) of our output using powers of 2 and XOR
    def reverseBits(self, n: int) -> int:
        output = 0
        i = 31

        while n > 0:
            # get the last binary digit of n: 0011 = 1
            last_digit = n & 1

            # cut off the last binary digit of n: 0011 = 0001
            n >>= 1

            # if the last digit is a 1, flip the leftmost binary output
            # and move our i pointer to the "right" by powers of 1.
            # For example: 1000 ^ pow(2, 3) = 1100
            if last_digit:
                output = output ^ pow(2, i)

            i -= 1

        return output
    
    # Runtime Complexity: O(1)
    # Space Complexity: O(1)
    # Time: Not timed
    #
    # This solution uses a divide and conquer approach to swap bits. First we
    # swap the first 16 and the last 16 bits, then we split them into 8 sections
    # and swap section 1 with section 2, section 3 with section 4, and so forth.
    # Then we split them into 16 sections and do the same thing. Then we split
    # them into 32 sections and do the same thing.
    #
    # Example swap: n = 11110000
    # (n & 11110000) >> 4 = 00001111 (gets shifted right)
    # (n & 00001111) << 4 = 00000000 (gets shifted left)
    # n = 00001111 | 00000000 = 00001111
    def reverseBitsUsingDivideAndConquer(self, n):
        n = (n >> 16) | (n << 16)
        n = ((n & 0b11111111000000001111111100000000) >> 8) | ((n & 0b00000000111111110000000011111111) << 8)
        n = ((n & 0b11110000111100001111000011110000) >> 4) | ((n & 0b00001111000011110000111100001111) << 4)
        n = ((n & 0b11001100110011001100110011001100) >> 2) | ((n & 0b00110011001100110011001100110011) << 2)
        n = ((n & 0b10101010101010101010101010101010) >> 1) | ((n & 0b01010101010101010101010101010101) << 1)
        return n

        
solution = Solution()
answer = solution.reverseBitsUsingDivideAndConquer(13)
print(answer)