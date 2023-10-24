from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/sort-list/
# Tags: Linked List, Merge Sort
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: Not timed
    #
    # Perform merge sort on linked list
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        mid = self.getMid(head)

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    
    def merge(self, left, right):
        result = ListNode()
        head = result

        while left and right:
            if left.val < right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next

        head.next = left if left else right

        return result.next
    
    def getMid(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        return mid

        
solution = Solution()
answer = solution.sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))
print(answer)