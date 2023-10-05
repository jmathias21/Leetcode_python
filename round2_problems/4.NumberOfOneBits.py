# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 6:00
    def hammingWeight(self, n: int) -> int:
        total = 0

        while n > 0:
            # Check to see if last bit is a 1
            if n & 1:
                # if it is, add to total
                total += 1
            # chop off the last bit
            n >>= 1

        return total

        
solution = Solution()
answer = solution.hammingWeight(13)
print(answer)