from typing import List

# https://leetcode.com/problems/rotate-array/
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    #
    # To rotate the array by k, we slice the left side of the
    # pivot point and store it in a separate array. Then we
    # piece the left side and right side together onto the
    # original array.
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)

        # we take the mod of k because if the list is
        # length 10 and k = 3, then k = 13 should return
        # the same result
        k = k % len(nums)

        # get the left side of the array up to the pivot point
        left = nums[:length - k]

        # paste the right side of the array onto the left side.
        # We use the original array as the source because this 
        # hasn't been overwritten yet
        nums[:k] = nums[length - k: length]

        # paste the left side of the array onto the right side
        nums[k:length] = left

        return nums

solution = Solution()
solution.rotate([1, 2, 3, 4, 5, 6, 7], 3)