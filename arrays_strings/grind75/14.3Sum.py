from typing import List

# https://leetcode.com/problems/3sum/
# Tags: 
class Solution:

    # Runtime Complexity: O(n^2)
    # Space Complexity: O(n)
    # Time: Not timed
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        num_length = len(nums)

        for i in range(num_length):
            if nums[i] > 0:
                break

            # make sure we skip duplicate values of nums[i]
            if i == 0 or nums[i] != nums[i - 1]:
                self.twoSum(nums, i, answer)

        return answer
            
    
    def twoSum(self, nums: List[int], i: int, res: List[List[int]]) -> List[int]:
        left = i + 1
        right = len(nums) - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1


        
solution = Solution()
answer = solution.threeSum([-4,-3,-2,-1,0,1,2,3,4])
answer = solution.threeSum([-1,0,1,2,-1,-4])
print(answer)