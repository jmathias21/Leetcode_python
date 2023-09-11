
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/middle-of-the-linked-list/editorial/
# Tags: Linked List, Fast/Slow Pointer
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow



solution = Solution()
answer = solution.middleNode(ListNode(1))
print(answer.val)

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.