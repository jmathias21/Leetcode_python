from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/reorder-list/
# Tags: middle of the linked list, reverse linked list, merge two sorted lists
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: Not timed
    #
    # Split the lists at the middle (right biased). Then reverse the right linked list, and merge
    # the right linked list back into the left linked list
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split lists at middle (right biased)
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right_head = slow.next
        slow.next = None

        # reverse right list
        curr = right_head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        right_head = prev

        # merge two lists
        while right_head:
            prev_next = head.next
            head.next = right_head
            right_prev_next = right_head.next
            right_head.next = prev_next

            head = prev_next
            right_head = right_prev_next


solution = Solution()
answer = solution.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
print(answer)