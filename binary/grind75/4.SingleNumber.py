from typing import List

# https://leetcode.com/problems/single-number/
# Tags: Bit manipulation, math, hash set, bitwise XOR
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # The sum of unique numbers is half of the sum of all numbers combined
    # if there was exactly two of each. But one of the numbers is missing its
    # second number, therefore (2 * sum(unique nums)) - sum(all nums)) gives us
    # the single number 
    #
    # Example: [4, 1, 2, 1, 2]
    # uniqueNumbers = [4, 1, 2]
    # ans = (2 * sum(4, 1, 2)) - sum(4, 1, 2, 1, 2)
    # ans = 14 - 10
    # ans = 4
    def singleNumberUsingHashSetAndMath(self, nums: List[int]) -> int:
        uniqueNumbers = set(nums)
        return (2 * sum(uniqueNumbers)) - sum(nums)

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: Not timed
    #
    # Uses bit manipulation to find the answer. If we XOR two of the same number,
    # it returns 0. This will leave the single number after XOR'ing all numbers
    #
    # Example: [1, 2, 1, 4, 2]
    # num = 1 [001]
    # x = 000 ^ 001 = 001
    #
    # num = 2 [010]
    # x = 001 ^ 010 = 011
    #
    # num = 1 [001]
    # x = 011 ^ 001 = 010 (Note that the 1's are now canceled, leaving x = 2)
    #
    # num = 4 [100]
    # x = 010 ^ 100 = 110
    #
    # num = 2 [010]
    # x = 110 ^ 010 = 100
    #
    # x = 100, which is 4
    def singleNumberUsingBitManipulation(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            x ^= num

        return x     

        
solution = Solution()
answer = solution.singleNumberUsingBitManipulation([1,2,1,2,4])
answer = solution.singleNumberUsingHashSetAndMath([4,1,2,1,2])
print(answer)