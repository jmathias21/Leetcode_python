from typing import List

# https://leetcode.com/problems/rotate-array/
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    #
    # This solution mods the rotation number against the list length
    # because if k = 7 and len(nums) = 7, then the list is rotated all
    # the way back to normal, and nothing changes.
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        # 1 2 3 4 | 5 6 7  k = 3
        # 1 2 3 4
        left = nums[:n - k]

        # 1 2 3 | 4 5 6 7
        # 5 6 7   4 5 6 7
        nums[:k] = nums[n - k:]

        # 5 6 7 | 4 5 6 7
        # 5 6 7   1 2 3 4
        nums[k:] = left

        print(nums)


solution = Solution()
solution.rotate([1, 2, 3, 4, 5, 6, 7], 3)