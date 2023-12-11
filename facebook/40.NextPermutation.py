from typing import List

# https://leetcode.com/problems/next-permutation/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 2:15
    def nextPermutation(self, nums: List[int]) -> None:
        left_swap = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                left_swap = i
                break

        if left_swap == -1:
            return nums.reverse()
        
        reversed = nums[left_swap + 1:]
        reversed.reverse()
        nums[left_swap + 1:] = reversed
        
        for i, num in enumerate(reversed):
            if num > nums[left_swap]:
                temp = nums[left_swap]
                nums[left_swap] = nums[i + left_swap + 1]
                nums[i + left_swap + 1] = temp
                break
        


        
solution = Solution()
answer = solution.nextPermutation([1,3,2])
answer = solution.nextPermutation([5,2,4,3,1])
print(answer)