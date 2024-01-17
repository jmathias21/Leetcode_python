from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minimum = min(nums)
        maximum = max(nums)
        counts = [0] * (maximum - minimum + 1)

        for num in nums:
            counts[num - minimum] += 1

        for i in range(len(counts) - 1, -1, -1):
            k -= counts[i]

            if k <= 0:
                return i + minimum

        
solution = Solution()
answer = solution.findKthLargest([3,2,1,5,6,4], 2)
print(answer)