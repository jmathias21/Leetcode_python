from typing import List

# https://leetcode.com/problems/plates-between-candles/
# Tags: Prefix Sum
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 23:00
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix_sum = [0] * len(s)
        prev_map = [None] * len(s)
        next_map = [None] * len(s)

        curr_sum = 0
        prev = None
        for i, char in enumerate(s):
            if char == '*':
                curr_sum += 1
            else:
                prev = i
            prev_map[i] = prev    
            prefix_sum[i] = curr_sum

        next = None
        for i in range(len(s) - 1, -1, -1):
            if s[i] != '*':
                next = i
            next_map[i] = next

        output = []
        for start, end in queries:
            if prev_map[end] == None or next_map[start] == None:
                output.append(0)
            else:
                output.append(max(0, prefix_sum[prev_map[end]] - prefix_sum[next_map[start]]))

        return output

        
solution = Solution()
answer = solution.platesBetweenCandles("||*", [[2,2]])
answer = solution.platesBetweenCandles("**|**|***|", [[2,5],[5,9]])
print(answer)
answer = solution.platesBetweenCandles("***|**|*****|**||**|*", [[1,17],[4,5],[14,17],[5,11],[15,16]])
print(answer)


# Input: s = "**|**|***|", queries = [[2,5],[5,9]]
# Output: [2,3]
# Explanation:
# - queries[0] has two plates between candles.
# - queries[1] has three plates between candles.