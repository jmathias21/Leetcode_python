from collections import defaultdict
import math
from typing import List

from sortedcontainers import SortedDict

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 1:53
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)

        for task in tasks:
            d[task] += 1

        task_counts = sorted(d.values(), reverse=True)
        task_max = task_counts[0]

        idles = (task_max - 1) * n

        for i in range(1, len(task_counts)):
            idles -= min(task_max - 1, task_counts[i])

        idles = max(0, idles)

        return idles + len(tasks)


        
solution = Solution()
answer = solution.leastInterval(["A","A","A","B","B","B"], 2)
answer = solution.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)
print(answer)