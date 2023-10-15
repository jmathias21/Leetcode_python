from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Tags: Two Pointers
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 30:00
    #
    # "First" pointer always stays n nodes ahead of "Slow" pointer. When fast pointer reaches the end of the list
    # we know that slow pointers next node is the node we want to remove. So we remove it and return the new head
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # using a dummy handles the edge case where the node we want to remove is the head itself
        dummy = ListNode()
        dummy.next = head
        second = dummy
        first = dummy

        for i in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next

        
solution = Solution()
answer = solution.removeNthFromEnd(ListNode(1), 1)
answer = solution.removeNthFromEnd(ListNode(1, ListNode(2)), 2)
answer = solution.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
print(answer)