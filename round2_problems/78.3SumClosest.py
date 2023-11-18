from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n^2)
    # Space Complexity: O(1)
    # Time: Not timed
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        length = len(nums)

        nums.sort()

        for i in range(len(nums) - 2):
            left = i + 1
            right = length - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < abs(closest - target):
                    closest = s
                if s < target:
                    left += 1
                else:
                    right -= 1

        return closest


        
solution = Solution()
answer = solution.threeSumClosest([-6,-3,-1,2,3,5], 2)
print(answer)