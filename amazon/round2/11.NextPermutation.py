from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O()
    # Time: started 12:04
    def nextPermutation(self, nums: List[int]) -> None:
        # iterate right to left
        # find first decreasing
        # find next highest number to the right
        # swap it with current number

        first_decreasing = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                first_decreasing = i
                break

        if first_decreasing == -1:
            nums.reverse()
            return

        reversed_nums = nums[first_decreasing + 1:]
        reversed_nums.reverse()
        nums[first_decreasing + 1:] = reversed_nums
        
        for i in range(first_decreasing + 1, len(nums)):
            if nums[i] > nums[first_decreasing]:
                nums[i], nums[first_decreasing] = nums[first_decreasing], nums[i]
                return
                


        
solution = Solution()
answer = solution.nextPermutation([1,2,3])
print(answer)