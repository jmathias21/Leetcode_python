from typing import List

# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
# Tags: prefix count
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    def getMaxLen(self, nums: List[int]) -> int:
        length = len(nums)
        pos = [0] * length
        neg = [0] * length
        pos[0] = 1 if nums[0] > 0 else 0
        neg[0] = 1 if nums[0] < 0 else 0

        max_length = pos[0]
        for i in range(1, length):
            if nums[i] > 0:
                pos[i] = pos[i - 1] + 1
                neg[i] = neg[i - 1] + 1 if neg[i - 1] > 0 else 0
            elif nums[i] < 0:
                pos[i] = neg[i - 1] + 1 if neg[i - 1] > 0 else 0
                neg[i] = pos[i - 1] + 1
            max_length = max(max_length, pos[i])

        return max_length
    
solution = Solution()
answer = solution.getMaxLen([0,1,-2,-3,-4])
answer = solution.getMaxLen2([1,3,2,0,-1,3,-2,4])
print(answer)