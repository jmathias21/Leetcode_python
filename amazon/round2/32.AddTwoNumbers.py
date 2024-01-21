from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 9:57
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        carry = 0

        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            s = num1 + num2 + carry
            carry = 0

            if s > 9:
                carry = 1
                s -= 10

            curr.next = ListNode(s)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            curr.next = ListNode(1)

        return head.next

        
solution = Solution()
answer = solution.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
print(answer)