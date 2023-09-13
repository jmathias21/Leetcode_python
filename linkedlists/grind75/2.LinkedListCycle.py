from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
# https://leetcode.com/problems/linked-list-cycle/
# Tags: Floyds Cycle, Hashset, Linked List
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 9:30
    #
    # Uses a set to track which nodes have been visited.
    # If we revisit the same node, return True
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head is None):
            return False

        seen = set()

        while (head.next):
            if (head in seen):
                return True

            seen.add(head)
            head = head.next

        return False
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 10:30
    #
    # Uses Floyds Cycle Finding Algorithm to create a fast runner
    # and a slow runner. If the fast runner loops over the slow runner,
    # we know that the nodes repeat
    def hasCycleLeastMemory(self, head: Optional[ListNode]) -> bool:
        if (head is None):
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            
            slow = slow.next
            fast = fast.next.next

        return True
        


        
solution = Solution()
l4 = ListNode(4)
l0 = ListNode(0)
l2 = ListNode(2)
head = ListNode(3)
head.next = l2
l2.next = l0
l0.next = l4
l4.next = l2
answer = solution.hasCycle2(head)
print(answer)