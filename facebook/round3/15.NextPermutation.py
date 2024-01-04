from typing import List
import bisect

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O()
    # Time: started 3:15
    def nextPermutation(self, nums: List[int]) -> None:
        # Iterate right to left, find first decreasing
        # sorted nums to the right
        # find next highest number to the right and swap (binary search)
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

        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                return


        
solution = Solution()
# answer = solution.nextPermutation([3,2,1])
answer = solution.nextPermutation([1,3,2])
print(answer)