from collections import defaultdict
import heapq
from typing import List

# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Tags: Bellman-Ford, Djisktra's
class Solution:

    # Runtime Complexity: O((n + E) * K)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # To solve for the cheapest price from src to dst with at most k stops using the Bellman-Ford algorithm,
    # we initialize distances from src to all cities as infinity (except src itself, which is zero), then
    # relax each flight's edges up to k+1 times to find the minimum cost, ensuring we only consider paths
    # with at most k stops
    def findCheapestPriceUsingBellmanFord(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        memo = [float('inf') for _ in range(n)]
        memo[src] = 0

        for _ in range(k + 1):
            new_memo = memo.copy()

            for flight in flights:
                s, d, price = flight

                if memo[s] == float('inf'):
                    continue

                new_memo[d] = min(new_memo[d], memo[s] + price)
            memo = new_memo

        return memo[dst] if memo[dst] != float('inf') else -1
    

    # Runtime Complexity: O(N + E * K * log(E * K))
    # Space Complexity: O(N + E * K)
    # Time: Not timed
    def findCheapestPriceUsingDjikstras(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [[float('inf')] * (k + 2) for _ in range(n)]
        prices[src][0] = 0

        adj = [[] for _ in range(n)]
        for s, d, cost in flights:
            adj[s].append((d, cost))

        priority_queue = [(0, src, 0)]

        while priority_queue:
            cost, node, stops = heapq.heappop(priority_queue)

            if node == dst:
                return cost

            if stops > k:
                continue

            for neighbor, neighbor_cost in adj[node]:
                new_cost = cost + neighbor_cost
                if new_cost < prices[neighbor][stops + 1]:
                    prices[neighbor][stops + 1] = new_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor, stops + 1))

        return -1
    
    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: Not timed
    def findCheapestPriceUsingBFS(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cheapest = float('inf')
        adj = [[] for _ in range(n)]

        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))

        # sort by price
        for nodes in adj:
            nodes.sort(key=lambda x: x[1])

        memo = defaultdict(lambda: float('inf'))

        def dfs(node, stops, total):
            nonlocal cheapest
            if total >= cheapest or total >= memo[(node, stops)]:
                return

            if node == dst:
                cheapest = total
                return

            if stops > k:
                return
            
            memo[(node, stops)] = total

            for neighbor, price in adj[node]:
                dfs(neighbor, stops + 1, total + price)

        dfs(src, 0, 0)
        return cheapest if cheapest != float('inf') else -1
    
        
solution = Solution()
# answer = solution.findCheapestPriceUsingDjikstras(5, [[0,1,4],[0,2,2],[1,2,3],[2,1,1],[1,3,2],[2,3,4],[2,4,5],[1,4,3],[4,3,1]], 0, 3, 2)
# answer = solution.findCheapestPriceUsingDjikstras(4, [[0,1,100],[1,2,100],[2,0,-300],[2,3,500]], 0, 3, 3)
# answer = solution.findCheapestPriceUsingDjikstras(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
# answer = solution.findCheapestPriceUsingDjikstras(5, [[0,1,1],[0,2,5],[1,2,1],[2,3,1],[3,4,1]], 0, 4, 2)
# answer = solution.findCheapestPriceUsingDjikstras(2, [[1,0,5]], 0, 1, 1)
# answer = solution.findCheapestPriceUsingDjikstras(5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1)
answer = solution.findCheapestPriceUsingBellmanFord(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 4)
print(answer)