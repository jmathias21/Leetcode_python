from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 5:30
    def nextPermutation(self, nums: List[int]) -> None:
        # iterate backwards. Find first decreasing.
        # reverse numbers to the right
        # find next highest number to the right
        # swap them

        first_decreasing = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                first_decreasing = i
                break

        if first_decreasing == -1:
            nums.reverse()
            return
        
        reversed = nums[first_decreasing + 1:]
        reversed.reverse()
        nums[first_decreasing + 1:] = reversed
        
        for i in range(first_decreasing + 1, len(nums)):
            if nums[i] > nums[first_decreasing]:
                nums[i], nums[first_decreasing] = nums[first_decreasing], nums[i]
                return
            

        
solution = Solution()
answer = solution.nextPermutation([1,2,3])
print(answer)