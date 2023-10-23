from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/add-two-numbers/
# Tags: Linked List
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 19:00
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        node = head

        while l1 or l2 or carry == 1:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            s = l1_val + l2_val + carry

            if s >= 10:
                carry = 1
                s -= 10
            else:
                carry = 0

            node.next = ListNode(s)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next

        
solution = Solution()
answer = solution.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
answer = solution.addTwoNumbers(ListNode(4, ListNode(3)), ListNode(5, ListNode(6, ListNode(4))))
print(answer)