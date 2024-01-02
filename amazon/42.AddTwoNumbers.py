from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(max(l1, l2))
    # Space Complexity: O()
    # Time: 
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        head = dummy

        while l1 or l2:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next

            s = val1 + val2 + carry

            if s > 9:
                s -= 10
                carry = 1
            else:
                carry = 0

            head.next = ListNode(s)
            head = head.next

        if carry:
            head.next = ListNode(1)

        return dummy.next
        
solution = Solution()
answer = solution.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
print(answer)

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.