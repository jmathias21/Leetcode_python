class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 12:24
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True

        length = 0
        curr = head
        prev = None

        # get length of list
        while curr:
            length += 1
            curr = curr.next

        curr = head

        for i in range((length // 2) - 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        left_head = curr
        right_head = curr.next if length % 2 == 0 else curr.next.next
        left_head.next = prev

        while left_head is not None:
            if left_head.val != right_head.val:
                return False
            
            left_head = left_head.next
            right_head = right_head.next

        return True


        
solution = Solution()
#answer = solution.isPalindrome(ListNode(1, ListNode(0)))
#answer = solution.isPalindrome(ListNode(1, ListNode(0, ListNode(1))))
#answer = solution.isPalindrome(ListNode(1, ListNode(0, ListNode(0))))
answer = solution.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
#answer = solution.isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1))))))
print(answer)