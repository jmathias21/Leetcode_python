from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Tags: Reverse Linked list
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 35:00
    #
    # Get length of the list. Determine the iterations needed from length of list // k. On each iteration,
    # reverse k nodes. Then repeat on the next set of nodes.
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        iterations = length // k

        dummy = ListNode()
        dummy.next = head
        curr = head
        end_node = dummy
        for _ in range(iterations):
            i = 0
            prev = end_node
            end_node = curr
            orig_prev = prev
            while i < k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                i += 1
            end_node.next = curr
            if orig_prev:
                orig_prev.next = prev

        return dummy.next

        
solution = Solution()
answer = solution.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3)
print(answer)