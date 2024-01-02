from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 11:45
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        prev = None

        for i in range(len(nums)):
            if nums[i] == prev:
                continue
            prev = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1

        return result
                

        
solution = Solution()
# answer = solution.threeSum([0,0,0,0])
answer = solution.threeSum([-1,0,1,2,-1,-4])
print(answer)