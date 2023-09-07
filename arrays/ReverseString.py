from typing import List

# https://leetcode.com/problems/reverse-string/description/
# Tags: Two Pointers
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def reverseString(self, s: List[str]) -> None:
        # Set two pointers on left and right side of array
        left = 0
        right = len(s) - 1

        # loop through the array and swap pointer values in list,
        # then move pointers towards the middle of the array. If
        # the pointers converge, then we know we're finished
        while (left < right):
            # swap the values in-place
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            # move left and right pointers towards the center
            left += 1
            right -= 1

        return s
        
solution = Solution()
solution.reverseString(['h','e','l','l','o'])
solution.reverseString(['t','e','s','t'])