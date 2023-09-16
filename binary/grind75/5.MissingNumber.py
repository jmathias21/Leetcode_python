from typing import List

# https://leetcode.com/problems/missing-number/
# Tags: Summation, XOR, bitwise manipulation
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 15:00
    #
    # Sum all of the expected numbers together as well as the actual numbers.
    # When we subtract the expected from the actual total, we get the missing
    # number
    def missingNumberUsingSummation(self, nums: List[int]) -> int:
        expected = 0
        actual = 0
        l = len(nums)
        for i in range(0, l):
            expected += i
            actual += nums[i]

        expected += l

        return expected - actual
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: Not timed
    #
    # 1. We start with a number, which is the length of the list.
    # 2. For every position (index) and number in the list, we XOR them with our starting number.
    # 3. Due to the properties of XOR, any number and its matching position will cancel each other out.
    # 4. After we've gone through the list, the result will be the only number that didn't
    #    have a match (i.e., the missing number).
    #
    # In simple terms: We mix all the positions and numbers together using XOR. Any number
    # that has its matching position in the list will disappear, leaving behind the missing number.
    def missingNumberUsingXor(self, nums: List[int]) -> int:
        missing_number = len(nums)
        for i in range(0, len(nums)):
            missing_number ^= i ^ nums[i]

        return missing_number


        
solution = Solution()
answer = solution.missingNumberUsingXor([0, 1, 3, 4, 5])
print(answer)