from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/reverse-linked-list/
# Tags: Linked List
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 20:30
    #
    # Walk through linked list and reverse the node pointers
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        head = None

        while (curr):
            temp = curr.next
            curr.next = head
            head = curr
            curr = temp

        return head

        
solution = Solution()
answer = solution.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
print(answer)