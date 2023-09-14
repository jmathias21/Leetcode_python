from typing import List

# https://leetcode.com/problems/majority-element/
# Tags: sort
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 22:30
    #
    # Since the majority element will take up over half the list,
    # we can sort the list and take the middle value, because the 
    # middle value will always be part of the majority number
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)

        mid = int((l - 1) / 2)

        return nums[mid]


        
solution = Solution()
answer = solution.majorityElement([12,52,12,70,12,61,12,12,50,72,82,12,11,25,28,43,40,12,12,53,12,12,98,12,12,92,81,2,12,15,40,12,12,9,12,31,12,12,12,12,77,12,12,50,12,12,12,93,41,92,12,12,12,12,12,12,12,12,12,37,48,14,12,70,82,12,80,12,12,12,12,56,30,12,8,12,50,12,20,12,21,97,12,42,12,10,12,38,73,15,9,11,79,12,12,28,51,12,15,12])
answer = solution.majorityElement([2,3,3])
answer = solution.majorityElement([2,2,4,3,1,1,2,2,2])
print(answer)