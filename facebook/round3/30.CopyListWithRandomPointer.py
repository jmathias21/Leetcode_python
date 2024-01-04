from typing import List, Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 25:00
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_map = {}

        dummy = Node(-1)
        copy_head = dummy
        curr = head
        while curr:
            copy_head.next = Node(curr.val)
            copy_map[curr] = copy_head.next
            copy_head = copy_head.next
            curr = curr.next

        copy_head = dummy.next
        curr = head
        while curr:
            if curr.random:
                copy_head.random = copy_map[curr.random]
            copy_head = copy_head.next
            curr = curr.next

        return dummy.next

        
solution = Solution()
n7 = Node(7)
n13 = Node(13)
n11 = Node(11)
n10 = Node(10)
n1 = Node(1)

n7.next = n13
n13.next = n11
n13.random = n7
n11.next = n10
n11.random = n1
n10.next = n1
n10.random = n11
n1.random = n7

answer = solution.copyRandomList(n7)
print(answer)