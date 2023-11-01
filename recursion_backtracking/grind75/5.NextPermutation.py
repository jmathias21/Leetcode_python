from typing import List
import bisect

# https://leetcode.com/problems/next-permutation/
# Tags: Permutations, binary search
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: Not timed
    #
    # Find the first decreasing number, iterating right to left. Sort the numbers to the right of the first
    # decreasing number. Swap first decreasing number with the next highest number to the right
    def nextPermutation(self, nums: List[int]) -> None:
        # look for the first decreasing number, iterating right to left
        # [5,2,4,3,1], first decreasing number index = 1
        left_swap = -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i - 1] < nums[i]:
                left_swap = i - 1
                break

        # if number is only descending digits, the next permutation is the reverse of it
        if left_swap == -1:
            nums.reverse()
            return
        
        # all numbers to the right of the number we want to swap are monotonic decreasing.
        # Since we want the next permutation, we need to sort these numbers ascending
        # [5,2,1,3,4]
        subset = nums[i:]
        subset.reverse()
        nums[i:] = subset

        # find the next highest number to the right
        right_swap = i + bisect.bisect_left(nums[i:], nums[left_swap] + 1)

        # swap our left number with the next highest number to the right
        # [5,3,1,2,4], (2 and 3 are swapped)
        temp = nums[left_swap]
        nums[left_swap] = nums[right_swap]
        nums[right_swap] = temp

        
solution = Solution()
answer = solution.nextPermutation([1,2,4,9,8,7,6,5,3])
answer = solution.nextPermutation([1,2,3])
answer = solution.nextPermutation([1,5,2])
answer = solution.nextPermutation([3,2,1])
print(answer)