from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 1:43
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if num - 1 not in s:
                count = 0
                while num in s:
                    num += 1
                    count += 1
                longest = max(longest, count)

        return longest

        
solution = Solution()
answer = solution.longestConsecutive([100,4,200,1,3,2])
print(answer)