from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 30:00
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        s = sum(nums)

        if s % 2 != 0:
            return False
        
        target = s // 2

        sums = set()
        sums.add(0)
        for num in nums:
            new_sums = sums.copy()
            for s in sums:
                new_sums.add(num + s)
            sums = new_sums

        return target in sums

        
        
solution = Solution()
answer = solution.canPartition([1,5,11,5])
#answer = solution.canPartition([1,2,3,4,5])
print(answer)

# DP - 0/1 Knapsack. Hash set keeps track of sums. For every num, we loop through hash set sums, add the current number to each sum, then add it back to the hash set