from typing import List, Optional

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 4:30
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node
        
        def insert_node(curr):
            new_node = Node(insertVal)
            new_node.next = curr.next
            curr.next = new_node

        # get the start node
        start = None
        curr = head
        while True:
            if curr.val > curr.next.val:
                start = curr.next
                break

            curr = curr.next
            if curr == head:
                start = head
                break
        
        # insert the node
        curr = head
        while True:
            if curr.next == start and (insertVal < curr.next.val or insertVal > curr.val):
                insert_node(curr)
                break
            elif insertVal >= curr.val and insertVal <= curr.next.val:
                insert_node(curr)
                break
            
            curr = curr.next
            if curr == head:
                break

        return head


solution = Solution()
# n1 = Node(1)
# n1.next = n1
# answer = solution.insert(n1, 2)

n1 = Node(1)
n3 = Node(3)
n5 = Node(5)
n3.next = n5
n5.next = n1
n1.next = n3
answer = solution.insert(n3, 0)

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