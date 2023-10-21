from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 30:00
    def nextPermutation(self, nums: List[int]) -> None:
        if sorted(nums, reverse=True) == nums:
            nums.sort()
            return

        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                nums[i + 1:] = sorted(nums[i + 1:])

                for j in range(i + 1, len(nums)):
                    if nums[j] > nums[i]:
                        next_largest_idx = j
                        break

                temp = nums[i]
                nums[i] = nums[next_largest_idx]
                nums[next_largest_idx] = temp
                return


        
solution = Solution()
answer = solution.nextPermutation([2,3,1])
answer = solution.nextPermutation([1,1,5])
answer = solution.nextPermutation([3,2,1])
answer = solution.nextPermutation([1,2,3])
print(answer)