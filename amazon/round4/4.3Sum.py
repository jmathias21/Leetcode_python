from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n ^ 2)
    # Space Complexity: O()
    # Time: started 10:46
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        prev = None
        for i in range(len(nums) - 1):
            if nums[i] == prev:
                continue
            prev = nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif s >= 0:
                    right -= 1
                else:
                    left += 1

        return result

        
solution = Solution()
answer = solution.threeSum([-2,0,0,2,2])
answer = solution.threeSum([-1,0,1,2,-1,-4])
print(answer)