from typing import List

# https://leetcode.com/problems/contains-duplicate/
# Tags: Hash Set
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 2:45
    #
    # Uses a hashset to keep track of whether each number has already
    # been seen
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for x in nums:
            if x in s:
                return True
            
            s.add(x)

        return False
        
solution = Solution()
answer = solution.containsDuplicate([1,2,3,4,1,5])
print(answer)