from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/palindrome-linked-list/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 40:00
    #
    # This solution loops through the list once to get the length,
    # then loops through it again to reverse the pointers for the first
    # half so it looks like this: N <- 1 <- 2   2 -> 1 -> N. Then we set
    # left and right pointers, traverse each halved list, and compare there
    # values to verify they are the same. If so, the list is a palindrome
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True

        curr = head
        prev = None
        list_length = 0

        # get list length
        while curr is not None:
            list_length += 1
            curr = curr.next

        curr = head

        # reverse first half of list
        for i in range(0, int(list_length / 2) - 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp                

        left_head = curr
        right_head = curr.next if list_length % 2 == 0 else curr.next.next
        left_head.next = prev

        # compare first half and second half
        while left_head is not None:
            if left_head.val != right_head.val:
                return False
            left_head = left_head.next
            right_head = right_head.next

        return True

        
solution = Solution()
answer = solution.isPalindrome(ListNode(1))
answer = solution.isPalindrome(ListNode(1, ListNode(2, ListNode(1))))
answer = solution.isPalindrome(ListNode(1, ListNode(1)))
answer = solution.isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1))))))
answer = solution.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
print(answer)