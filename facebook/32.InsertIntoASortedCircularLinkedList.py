from typing import Optional

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 9:50
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            head = Node(insertVal)
            head.next = head
            return head
        
        if head.next == head:
            head.next = Node(insertVal, head)
            return head

        curr = head
        while True:
            curr_val = curr.val
            next_val = curr.next.val

            if next_val > curr_val and insertVal >= curr_val and insertVal <= next_val:
                curr.next = Node(insertVal, curr.next)
                return head

            if next_val < curr_val and (insertVal >= curr_val or insertVal <= next_val):
                curr.next = Node(insertVal, curr.next)
                return head

            curr = curr.next
            if curr == head:
                head.next = Node(insertVal, head.next)
                return head
        
solution = Solution()
n1 = Node(3)
n3 = Node(4)
n5 = Node(1)
n1.next = n3
n3.next = n5
n5.next = n1
answer = solution.insert(n1, 2)

n1 = Node(1)
n1.next = n1
answer = solution.insert(n1, 0)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n1
answer = solution.insert(n1, 3)
answer = solution.insert(n1, 7)
print(answer)