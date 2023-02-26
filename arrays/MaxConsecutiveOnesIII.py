from typing import List

# https://leetcode.com/problems/max-consecutive-ones-iii/editorial/
# Tags: Sliding Window
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        unbrokenOnes = 0
        longestOnes = 0
        zeroesUsed = 0

        while right < n:
            if nums[right] == 1:
                unbrokenOnes += 1
                longestOnes = max(unbrokenOnes, longestOnes)
            else:
                if zeroesUsed == k:
                    if nums[left] == 0:
                        zeroesUsed -= 1
                    left += 1
                    unbrokenOnes -= 1
                    continue
                
                unbrokenOnes += 1
                longestOnes = max(unbrokenOnes, longestOnes)
                zeroesUsed += 1

            right += 1    

        return longestOnes    

solution = Solution()
answer = solution.longestOnes([0,0,0,0,1,1,1,0,0,1,1,0,1,1], 2)
print(answer)
