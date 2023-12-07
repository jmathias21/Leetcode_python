from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# https://leetcode.com/problems/copy-list-with-random-pointer/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 10:59
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':


        
solution = Solution()
answer = solution.copyRandomList()
print(answer)