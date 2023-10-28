from collections import Counter, defaultdict
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 30:00
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)
        max_task = max(frequencies, key=frequencies.get)
        max_frequency = frequencies[max_task]
        del frequencies[max_task]

        idle_count = (max_frequency - 1) * n

        for frequency in frequencies.values():
            idle_count -= min(max_frequency - 1, frequency)

        idle_count = max(0, idle_count)

        return idle_count + len(tasks)

        
solution = Solution()
#answer = solution.leastInterval(["A","A","A","B","B","B"], 2)
answer = solution.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 1)
print(answer)