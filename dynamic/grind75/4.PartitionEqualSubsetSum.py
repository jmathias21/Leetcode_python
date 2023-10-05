from typing import List

# https://leetcode.com/problems/partition-equal-subset-sum/
# Tags: 0/1 knapsack, dynamic programming
class Solution:

    # Runtime Complexity: O(m * n) where m is the sum(nums) / 2 and n is the number of array elements
    # Space Complexity: O(m)
    # Time: Not timed
    #
    # Uses a simplified version of a dynamic programming 0/1 knapsack solution. We use a hash set that
    # tracks all calculated sums, and on each iteration we add the current number to each of the sums
    # in the hash set and add those numbers to the hash set. e.g. if the current number is 3 and
    # the hash set contains [0,2], we add 0 + 3 and 2 + 3 back to the hash set, so it now contains
    # [0,2,3,5]. The hash set represents all possible sums, and we know if at least one sum is equal
    # to our target, we can return true
    def canPartitionUsingDPAndHashset(self, nums: List[int]) -> bool:
        s = sum(nums)

        # the sum cannot be an odd number
        if s % 2 != 0:
            return False
        
        target = s // 2
        dp = {0}

        for i in range(len(nums)):
            for j in list(dp):
                if j + nums[i] == target:
                    return True
                dp.add(j + nums[i])


    # Runtime Complexity: O(m * n) where m is the sum(nums) / 2 and n is the number of array elements
    # Space Complexity: O(m)
    # Time: Not timed
    #
    # Uses a simplified version of a dyanmic programming 0/1 knapsack solution. Uses a 2D array
    # to keep track of whether the current subset of numbers can sum to the current target (from
    # 0 to our actual target)
    def canPartitionUsingBottomUpDP(self, nums: List[int]) -> bool:
        s = sum(nums)

        if sum(nums) % 2 != 0:
            return False
        
        target = s // 2

        dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]
        for arr in dp:
            arr[0] = True

        for i in range(1, len(nums)):
            curr = nums[i - 1]
            for j in range(1, target + 1):
                if j > curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # dp[i - 1][j]: checks to see if the previous numbers in the set can already sum to
                    # target. If so, we know that adding more numbers won't stop a subset of them from
                    # summing to target, so we can set the current index to true
                    #
                    # dp[i - 1][j - nums[i - 1]]: in order to know if the current number can sum to our
                    # current target in combination with the previous numbers, we find the number that we
                    # need (target num - current num) from the previous iteration. If it's true, it means
                    # that our current index can be true because we found the needed number.
                    # e.g. We previously calculated that the subset (2,3) sums to 5 and stored that in our
                    # dp array. If our target is 9, and the current subset is (2,3,4), we check the previous
                    # subset in our dp array for target (9) minus current (4) = 5. Since that's set to true,
                    # we set the current index to true
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]

        return dp[len(nums) - 1][target]
            

        
solution = Solution()
answer = solution.canPartitionUsingDPAnd1DArray([2,3,1,4])
answer = solution.canPartition([1,3,4,4])
answer = solution.canPartition([1,5,11,5])
print(answer)
 
# Example for canPartitionUsingDPAnd1DArray: [2,3,1,4]
# target = sum(nums) / 2 = 5
# [0]: 0
# [0,2]: 0, 2
# [0,2,3]: 0, 2, 3, 5
# dp array contains 5, so return true

# Example for canPartitionUsingBottomUpDP: [2,3,1,4]
# target = sum(nums) / 2 = 5
#        j -->   0  1  2  3  4  5
# [2]         0| T  F  T  F  F  F
# [2,3]       1| T  F  T  T  F  T 
# [2,3,1]     2| T  T  T  T  T  T (j = 4 is true because dp[2][3] = dp[1][j - curr] = d[1][4 - 1] = True)
# [2,3,1,4]   3| T  T  T  T  T  T
# 