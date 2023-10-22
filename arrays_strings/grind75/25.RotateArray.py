from typing import List

# https://leetcode.com/problems/rotate-array/
# Tags: Modulus operator, reverse list in-place
class Solution:

    # Runtime Complexity: O(N)
    # Space Complexity: O(1)
    # Time: 7:00
    #
    # We get k modulus the length of numbers to account for k values that loop. Then we
    # reverse the array in-place, then reverse the first k numbers and then reverse the
    # rest of the numbers to the right
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(start, end):
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1
        
        length = len(nums)
        k = k % length

        reverse(0, length - 1)
        reverse(0, k - 1)
        reverse(k, length - 1)


        
solution = Solution()
answer = solution.rotate([1,2,3,4,5,6,7], 10)
print(answer)