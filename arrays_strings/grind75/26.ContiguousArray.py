from typing import List

# https://leetcode.com/problems/contiguous-array/
# Tags: Hash map, binary array
class Solution:

    # Runtime Complexity: O(N)
    # Space Complexity: O(N)
    # Time: Not timed
    #
    # Use hash map to store the current 0/1 count and corresponding index. At each index, if a
    # hash map item already exists for that count, we can calculate the max length at the index
    # by subtracting the current index from the indx stored in the hash map
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        map = {0: -1}
        count = 0

        for i in range(len(nums)):
            count = count - 1 if nums[i] == 0 else count + 1

            if count in map:
                max_length = max(max_length, i - map[count])
            else:
                map[count] = i

        return max_length

        
solution = Solution()
answer = solution.findMaxLength([0,1,0,0,1,1,0])
answer = solution.findMaxLength([0,1,0,0,1,1,0])
print(answer)