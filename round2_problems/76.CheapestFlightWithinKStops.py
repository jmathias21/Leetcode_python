from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 11:17
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        weights = [float('inf') for _ in range(n)]
        weights[src] = 0

        for _ in range(k + 1):
            new_weights = weights.copy()

            for flight in flights:
                frm, to, price = flight

                if weights[frm] == float('inf'):
                    continue

                new_weights[to] = min(new_weights[to], weights[frm] + price)

            weights = new_weights
        
        return weights[dst] if weights[dst] != float('inf') else -1

        
solution = Solution()
answer = solution.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
print(answer)