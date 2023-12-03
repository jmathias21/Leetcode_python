from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# https://leetcode.com/problems/copy-list-with-random-pointer/
# Tags: Linked List, Hash Map
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 20:00
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {}

        new_head = Node(-1)
        new_curr = new_head
        curr = head
        while curr:
            new_curr.next = Node(curr.val)
            map[curr] = new_curr.next

            new_curr = new_curr.next
            curr = curr.next

        curr = head
        while curr:
            if curr.random:
                map[curr].random = map[curr.random]
            curr = curr.next

        return new_head.next
    
        
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