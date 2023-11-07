from typing import List

# https://leetcode.com/problems/3sum-closest/
# Tags: Three pointers
class Solution:

    # Runtime Complexity: O(n ^ 2)
    # Space Complexity: O(1)
    # Time: Not timed
    #
    # Sort the array. Use three pointers: Iterate from left to right, and on each iteration assign
    # a left and right pointer that iterate inwards. Calculate the sum on each sub-iteration and
    # based on the sum determine which pointer we need to move next. Capture the closest sum to the
    # target
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        nums.sort()

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    return sum
                if abs(target - sum) < abs(target - closest):
                    closest = sum

        return closest

        
solution = Solution()
answer = solution.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2)
answer = solution.threeSumClosest([0,0,0], 1)
answer = solution.threeSumClosest([-1,2,1,-4], 1)
print(answer)