# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 9:00
    def reverseBits(self, n: int) -> int:
        # trim the last bit and add it to a new integer using powers of 2
        output = 0

        i = 31
        while n > 0:
            bit = n & 1
            n >>= 1

            if bit == 1:
                output = output ^ 2**i

            i -= 1

        return output

        
solution = Solution()
answer = solution.reverseBits(22)
print(answer)