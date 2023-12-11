from typing import List

# https://leetcode.com/problems/3sum/
# Tags: 
class Solution:

    # Runtime Complexity: O(n ^ 2)
    # Space Complexity: O(n)
    # Time: started 12:45
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        if nums[0] > 0:
            return []

        prev = None
        for i in range(len(nums)):
            if nums[i] == prev:
                continue
            prev = nums[i]

            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left, right = left + 1, right - 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return output

        
solution = Solution()
answer = solution.threeSum([-2,0,0,2,2])
answer = solution.threeSum([-1,0,1,2,-1,-4])
print(answer)