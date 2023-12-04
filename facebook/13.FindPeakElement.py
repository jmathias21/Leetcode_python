from typing import List

# https://leetcode.com/problems/find-peak-element/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 11:00
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('-inf')]

        def search(left, right):
            if left == right:
                return left

            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                return search(mid + 1, right)
            return search(left, mid)
            
        return search(1, len(nums) - 2) - 1

        
solution = Solution()
answer = solution.findPeakElement([1,2,1,3,5,6,4])
print(answer)