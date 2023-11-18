from collections import deque
from typing import List

class CompareKey(str):
    def __lt__(x, y):
        return x + y > y + x

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 1:11
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        largest_num = "".join(sorted(nums, key=CompareKey))
        return "0" if largest_num[0] == "0" else largest_num

        
solution = Solution()
answer = solution.largestNumber([3,30,34,5,9])
print(answer)