from typing import List

# Tags: 
class Solution:

    # Runtime Complexity: O(n ^ 2)
    # Space Complexity: O(n)
    # Time: 21:00
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        length = len(nums)
        nums.sort()
        prev = nums[0] - 1

        # three pointers
        for i in range(len(nums)):    
            if nums[i] == prev:
                continue

            left_prev = nums[i] - 1
            left = i + 1
            right = length - 1

            while left < right:
                if nums[left] == left_prev:
                    left += 1
                    continue

                s = nums[i] + nums[left] + nums[right]

                if s < 0:
                    left_prev = nums[left]
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    left_prev = nums[left]
                    left += 1

            prev = nums[i]

        return answer

        
solution = Solution()
answer = solution.threeSum([-1,0,1,2,-1,-4])
#answer = solution.threeSum([3,0,-2,-1,1,2])
# answer = solution.threeSum([0,0,0])
# answer = solution.threeSum([0,1,1])
# answer = solution.threeSum([-1,0,1,2,-1,-4])
print(answer)