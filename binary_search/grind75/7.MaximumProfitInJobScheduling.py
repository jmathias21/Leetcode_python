from typing import List
import bisect

# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# Tags: Top-down dynamic programming, bottom-up dynamic programming
class Solution:

    # Runtime Complexity: O(n logn)
    # Space Complexity: O(n)
    # Time: Not timed
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[0])
        start_times = [start_time for start_time, _, _ in jobs]

        memo = {}
        def backtrack(profit, i):
            if i >= len(jobs):
                return profit
            
            if i in memo:
                return memo[i] + profit

            skip_profit = backtrack(profit, i + 1)

            next_index = bisect.bisect_left(start_times, jobs[i][1], i + 1)
            pick_profit = backtrack(profit + jobs[i][2], next_index)

            memo[i] = max(skip_profit, pick_profit)
            return memo[i]

        return backtrack(0, 0)
    
    
    # Runtime Complexity: O(n logn)
    # Space Complexity: O(n)
    # Time: Not timed
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        dp = [0] * (len(jobs) + 1)
        start_times = [start_time for start_time, _, _ in jobs]

        for i in range(len(jobs) - 1, -1, -1):
            next_index = bisect.bisect_left(start_times, jobs[i][1], i + 1)
            dp[i] = max(dp[i + 1], dp[next_index] + jobs[i][2])

        return dp[0]
        
solution = Solution()
answer = solution.jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60])
print(answer)