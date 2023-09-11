
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/editorial/
# Tags: Linked List, 
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
        

solution = Solution()
answer = solution.deleteDuplicates2(ListNode(1, ListNode(1, ListNode(1, ListNode(3, ListNode(3))))))
print(answer.val)

# Input: head = [1,1,2]
# Output: [1,2]