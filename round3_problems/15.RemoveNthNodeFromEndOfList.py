from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 11:00
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        dummy = ListNode(-1)
        dummy.next = head
        
        first = dummy
        offset = dummy

        while n > 0:
            offset = offset.next
            n -= 1

        while offset and offset.next:
            first = first.next
            offset = offset.next

        first.next = first.next.next
        return dummy.next

        

        
solution = Solution()
answer = solution.removeNthFromEnd(ListNode(1, ListNode(2)), 2)
answer = solution.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
print(answer)