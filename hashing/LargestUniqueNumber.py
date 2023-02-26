
from typing import List
from collections import defaultdict

# https://leetcode.com/problems/largest-unique-number/editorial/
# Tags: Hash Map
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def largestUniqueNumber(self, nums: List[int]) -> int:
        highest = -1
        n = defaultdict(int)
        for num in nums:
            n[num] += 1

        for num, count in n.items():
            if (count == 1):
                highest = max(highest, num)

        return highest
            

solution = Solution()
answer = solution.largestUniqueNumber([5,7,3,9,4,9,8,3,1])
print(answer)

# Input: nums = [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: The maximum integer in the array is 9 but it is repeated.
# The number 8 occurs only once, so it is the answer.
