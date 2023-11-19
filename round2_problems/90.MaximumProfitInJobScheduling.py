from typing import List
import bisect

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 13:00
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit),key=lambda x: x[0])
        start_times = [job[0] for job in jobs]
        memo = {}

        def dfs(i, sum):
            if i in memo:
                return memo[i] + sum
            
            if i >= len(start_times):
                return sum

            # skip profit
            skip_profit = dfs(i + 1, sum)

            next_index = bisect.bisect_left(start_times, jobs[i][1], i + 1)
            # pick profit
            pick_profit = dfs(next_index, sum + jobs[i][2])

            memo[i] = max(skip_profit, pick_profit)
            return memo[i]
        
        return dfs(0, 0)

        
solution = Solution()
answer = solution.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70])
print(answer)