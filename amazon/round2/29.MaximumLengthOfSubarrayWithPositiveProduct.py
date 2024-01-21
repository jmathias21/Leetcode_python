from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 
    def getMaxLen(self, nums: List[int]) -> int:
        pos_len = 1 if nums[0] > 0 else 0
        neg_len = 1 if nums[0] < 0 else 0
        max_length = pos_len

        for i in range(1, len(nums)):
            if nums[i] < 0:
                temp = pos_len
                pos_len = neg_len + 1 if neg_len > 0 else 0
                neg_len = temp + 1
            elif nums[i] > 0:
                pos_len += 1
                neg_len += 1 if neg_len > 0 else 0
            else:
                pos_len = 0
                neg_len = 0
            max_length = max(max_length, pos_len)
        
        return max_length
                
        
solution = Solution()
answer = solution.getMaxLen([-16,0,-5,2,2,-13,11,8])
print(answer)