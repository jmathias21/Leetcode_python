from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/odd-even-linked-list/
# Tags: Linked List
class Solution:

    # Runtime Complexity: O(N)
    # Space Complexity: O(1)
    # Time: 15:00
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None

        odd, even = head, head.next
        even_head = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head


        
solution = Solution()
answer = solution.oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))))
answer = solution.oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
print(answer)