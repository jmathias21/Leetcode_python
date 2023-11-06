from typing import List

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

# https://leetcode.com/problems/largest-number/
# Tags: Comparison method
class Solution:

    # Runtime Complexity: O(n logn)
    # Space Complexity: O(n)
    # Time: Not timed
    def largestNumber(self, nums: List[int]) -> str:
        nums = [(str(num)) for num in nums]
        largest_num = "".join(sorted(nums, key=LargerNumKey))
        return "0" if largest_num[0] == "0" else largest_num

        
solution = Solution()
answer = solution.largestNumber([3,30,34,5,9])
print(answer)