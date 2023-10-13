from typing import List

# https://leetcode.com/problems/gas-station/
# Tags:
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 28:00
    #
    # Keep track of cumulative gain (gas - cost). If the gain goes negative, we know that the answer
    # must be at least one index in front of us, so we set it and reset our gain. If the gain never
    # goes negative, we have our answer
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_gain = 0
        total_gain = 0
        answer = 0

        for i in range(len(gas)):
            curr_gain += gas[i] - cost[i]
            total_gain += gas[i] - cost[i]

            # If we meet a "valley", start over from the next station
            # with 0 initial gas.
            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1

        return answer if total_gain >= 0 else -1

        
solution = Solution()
answer = solution.canCompleteCircuit([6,2,3,1,5,2], [0,4,5,5,0,4])
answer = solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
print(answer)