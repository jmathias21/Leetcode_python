from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/palindrome-linked-list/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 55:00
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True

        slow = head
        fast = head.next
        temp = head.next
        prev = None
        head.next = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = temp
            temp = slow.next
            slow.next = prev

        is_odd = fast is None
        fast = temp
        slow = slow.next if is_odd else slow

        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
            
        return True

        
solution = Solution()
#answer = solution.isPalindrome(ListNode(1, ListNode(0, ListNode(0))))
#answer = solution.isPalindrome(ListNode(1, ListNode(2)))
answer = solution.isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1)))))))
answer = solution.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
answer = solution.isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1))))))
print(answer)