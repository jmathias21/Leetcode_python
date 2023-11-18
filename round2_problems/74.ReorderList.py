from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Time: 21:00
    def reorderList(self, head: Optional[ListNode]) -> None:
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

        # merge two lists
        dummy = ListNode()
        curr = dummy
        while curr and prev:
            curr.next = head
            curr = curr.next
            head = head.next

            curr.next = prev
            curr = curr.next
            prev = prev.next
        curr.next = head

        return dummy.next





solution = Solution()
answer = solution.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
print(answer)