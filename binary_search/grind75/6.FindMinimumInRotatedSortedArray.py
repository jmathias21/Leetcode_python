from typing import List

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Tags: Binary search
class Solution:

    # Runtime Complexity: O(logn)
    # Space Complexity: O(1)
    # Time: 14:00
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # if not rotated, return minimum immediately
        if nums[left] < nums[right]:
            return nums[left]
        
        def search(left, right):
            mid = (left + right) // 2

            if nums[left] > nums[right]:
                if nums[mid] > nums[left]:
                    return search(mid + 1, right)
                else:
                    return search(left + 1, mid)
            else:
                return nums[left]
            
        return search(left, right)

        
solution = Solution()
answer = solution.findMin([4,5,1,2,3])
answer = solution.findMin([4,5,6,7,0,1,2])
print(answer)