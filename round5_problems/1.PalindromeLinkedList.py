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
    # Time: 12:00
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        prev = None
        while fast and fast.next:
            fast = fast.next.next

            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        left = prev
        right = slow.next if fast else slow

        while left:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True


        
solution = Solution()
answer = solution.isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1))))))
answer = solution.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
print(answer)