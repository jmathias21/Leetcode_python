from collections import Counter
from typing import List

# https://leetcode.com/problems/task-scheduler/
# Tags: Greedy
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: Not timed
    #
    # Get frequencies of each letter. Calculate how many idle times there would
    # be using the largest frequency and a worst case scenario of only using those
    # letters for each task. Then look at the next frequencies and replace the idle
    # times with them to see how many ideal times we actually need
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # store the frequency of each number and sort them ascending
        frequencies = sorted(Counter(tasks).values())

        f_max = frequencies.pop()

        # If there's a max of three A's, the worst case idle time looks like the
        # following: A, idle, idle, A, idle, idle, A
        idle_time = (f_max - 1) * n
        
        while frequencies and idle_time > 0:
            # we use min here in cases where there are another set of tasks that
            # are equal in number to our max set. If we applied them, that set
            # would overflow our max set
            idle_time -= min(f_max - 1, frequencies.pop())

        idle_time = max(0, idle_time)

        return idle_time + len(tasks)

        
solution = Solution()
answer = solution.leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 2)
answer = solution.leastInterval(["A","A","A","B","B","B"], 2)
answer = solution.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)
print(answer)

# ["A", "A", "A", "B", "B", "C"]

# A  []  []  A  []  []  A
# A  [B] []  A  [B] []  A
# A  [B] [C]  A [B] [I] A