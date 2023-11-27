from collections import defaultdict, deque
from typing import List

# https://leetcode.com/problems/bus-routes/
# Tags: BFS
class Solution:

    # Runtime Complexity: O(S) where S is the  number of stops
    # Space Complexity: O(S)
    # Time: Not timed
    #
    # Build a hash map of stops and buses that stop there. Starting at the source stop,
    # go to every stop in that route. After that, take any buses that you haven't been
    # that leave from a stop on that route. Track the number of buses you've taken
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # for each stop, store a list of buses that will stop there
        stop_bus = defaultdict(list)
        for bus in range(len(routes)):
            for stop in routes[bus]:
                stop_bus[stop].append(bus)

        buses_seen = set()
        queue = deque([(source, 0)])

        while queue:
            stop, buses_taken = queue.popleft()

            if stop == target:
                return buses_taken

            # at the current stop, try to get on all buses leaving this stop
            for bus in stop_bus[stop]:

                # do not get on a bus we've already gotten on
                if bus not in buses_seen:
                    buses_seen.add(bus)

                    # make sure we goto every stop in the current bus route before
                    # we get on a new bus
                    for next_stop in routes[bus]:
                        queue.append((next_stop, buses_taken + 1))
        return -1

        
solution = Solution()
answer = solution.numBusesToDestination([[24],[3,6,11,14,22],[1,23,24],[0,6,14],[1,3,8,11,20]], 20, 8)
answer = solution.numBusesToDestination([[1,2,7],[3,6,7]], 1, 6)
answer = solution.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12)
answer = solution.numBusesToDestination([[1,9,12,20,23,24,35,38],[10,21,24,31,32,34,37,38,43],[10,19,28,37],[8],[14,19],[11,17,23,31,41,43,44],[21,26,29,33],[5,11,33,41],[4,5,8,9,24,44]], 37, 28)
print(answer)