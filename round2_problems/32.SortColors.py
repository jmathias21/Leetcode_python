from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: started 8:16
    def sortColors(self, nums: List[int]) -> None:
        length = len(nums)
        left = 0
        right = length - 1

        i = 0
        while i <= right:
            if nums[i] == 2:
                temp = nums[right]
                nums[right] = nums[i]
                nums[i] = temp
                right -= 1
            elif nums[i] == 0:
                temp = nums[left]
                nums[left] = nums[i]
                nums[i] = temp
                left += 1
                i += 1
            else:
                i += 1
            

        
solution = Solution()
answer = solution.sortColors([2,0,2,1,1,0])
answer = solution.sortColors([2,1,2])
#answer = solution.sortColors([2,0,2,1,1,0])
print(answer)