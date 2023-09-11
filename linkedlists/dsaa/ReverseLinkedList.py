
from pickle import NONE
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/reverse-linked-list/
# Tags: Linked List
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
            


solution = Solution()
answer = solution.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))