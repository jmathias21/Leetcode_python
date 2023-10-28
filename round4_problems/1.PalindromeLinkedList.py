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
    # Time: Not timed
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True

        curr = head
        length = 0

        while curr:
            curr = curr.next
            length += 1

        curr = head
        prev = None
        for _ in range((length // 2) - 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        left_head = curr
        right_head = curr.next if length % 2 == 0 else curr.next.next
        left_head.next = prev

        for _ in range((length // 2)):
            if left_head.val != right_head.val:
                return False
            left_head = left_head.next
            right_head = right_head.next

        return True


        

        

        
solution = Solution()
answer = solution.isPalindrome(ListNode(1, ListNode(2)))
answer = solution.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
answer = solution.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
print(answer)