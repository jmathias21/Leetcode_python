from typing import List

from sortedcontainers import SortedDict

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 10:20
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        for num in s:
            if num - 1 not in s:
                curr_length = 1
                while num + curr_length in s:
                    curr_length += 1
                longest = max(longest, curr_length)

        return longest

        
solution = Solution()
answer = solution.longestConsecutive([100,4,200,1,3,2])
answer = solution.longestConsecutive([1,2,0,1])
answer = solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
print(answer)