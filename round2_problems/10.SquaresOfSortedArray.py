from typing import List
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 12:00
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left = 0
        right = l - 1
        output = [0] * l

        for i in range(l - 1, -1, -1):
            if abs(nums[right]) > abs(nums[left]):
                output[i] = nums[right] ** 2
                right -= 1
            else:
                output[i] = nums[left] ** 2
                left += 1

        return output

        
solution = Solution()
answer = solution.sortedSquares([-4,-1,0,3,10])
answer = solution.sortedSquares([-4,-3,-2,-1])
print(answer)