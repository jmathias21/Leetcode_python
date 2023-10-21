from typing import List

# https://leetcode.com/problems/longest-consecutive-sequence/
# Tags: Hash set
class Solution:

    # Runtime Complexity: O(N)
    # Space Complexity: O(N)
    # Time: Not timed
    #
    # Store each number in a set. Find numbers that have no number before it and then
    # check how many consecutive increasing numbers are already in the set, then move onto the
    # next number and check again. Store the longest streak
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
        
        
solution = Solution()
answer = solution.longestConsecutive([100,4,200,3,2,1,201])
answer = solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
answer = solution.longestConsecutive([100,4,200,1,3,2,201,202,203,204])
print(answer)