from typing import List

# https://leetcode.com/problems/counting-bits/
# Tags: least significant bit, bitwise AND
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O()
    # Time: 8:00
    def countBitsUsingBinFunction(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n + 1):
            ans.append(bin(i)[2:].count('1'))

        return ans
    
    # Runtime Complexity: O(n)
    # Space Complexity: O()
    # Time: Not timed
    def countBitsUsingLeastSignificantBit(self, n: int):
        if n == 0:
            return [0]

        ans = [0]

        for i in range(1, n+1):
            # (i & (i - 1)) flips the least significant bit in a number to a 0.
            # Doing so will give us a previously calculated number of 1's that we
            # know has exactly one less 1 than we need.
            ans.append(ans[i & (i - 1)] + 1)
        
        return ans

        
solution = Solution()
answer = solution.countBits(2)
answer = solution.countBits2(5)
print(answer)