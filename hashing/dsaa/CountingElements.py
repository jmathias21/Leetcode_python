from typing import List

# https://leetcode.com/problems/counting-elements/editorial/
# Tags: Hash Set
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def countElements(self, arr: List[int]) -> int:
        total = 0
        n = set(arr)
        for i in range(len(arr)):
            if arr[i] + 1 in n:
                total += 1
        return total


solution = Solution()
answer = solution.countElements([1,3,2,3,5,0])
print(answer)

# Input: arr = [1,1,2,3,5]
# Output: 3
# Explanation: 1, 1, and 2 are counted cause 2 and 3 are in arr.
# 3 not counted because 4 is not in array