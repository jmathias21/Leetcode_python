from collections import defaultdict
from typing import List



class Solution:

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        memo = {}
        total_cost = 0
        shortest_paths = {}

        for char in set(original + changed):
            memo[char] = float('inf')

        # Precompute shortest paths for each unique character in the source
        for source_val in set(source):
            new_memo = memo.copy()
            new_memo[source_val] = 0

            for _ in range(len(original)):
                for i in range(len(original)):
                    src, dest = original[i], changed[i]
                    weight = cost[i]

                    if new_memo[src] == float('inf'):
                        continue

                    new_memo[dest] = min(new_memo[dest], new_memo[src] + weight)

            shortest_paths[source_val] = new_memo

        # Calculate total transformation cost using the precomputed shortest paths
        for s, t in zip(source, target):
            if s != t:
                cost = shortest_paths[s][t]
                if cost == float('inf'):
                    return -1
                total_cost += cost

        return total_cost if total_cost != float('inf') else -1

        

        
solution = Solution()
answer = solution.minimumCost(source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2])
answer = solution.minimumCost(source = "abcd", target = "acbe",
                              original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20])
print(answer)

# Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"],
# cost = [2,5,5,1,2,20]
# Output: 28
# Explanation: To convert the string "abcd" to string "acbe":
# - Change value at index 1 from 'b' to 'c' at a cost of 5.
# - Change value at index 2 from 'c' to 'e' at a cost of 1.
# - Change value at index 2 from 'e' to 'b' at a cost of 2.
# - Change value at index 3 from 'd' to 'e' at a cost of 20.
# The total cost incurred is 5 + 1 + 2 + 20 = 28.
# It can be shown that this is the minimum possible cost.