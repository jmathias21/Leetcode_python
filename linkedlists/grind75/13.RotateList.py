from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/rotate-list/
# Tags: Split linked list
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 26:00
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        # get length of list
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1
        tail = curr

        k = k % length

        if k == 0:
            return head

        # split the list k away from the end
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next
        right_head = curr.next
        curr.next = None

        # tack right side onto left side
        tail.next = head
        return right_head

        
solution = Solution()
answer = solution.rotateRight(ListNode(1, ListNode(2)), 1)
answer = solution.rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 12)
print(answer)