from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/middle-of-the-linked-list/
# Tags: Linked List, Fast/Slow Pointer
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 10:30
    #
    # This solution uses something similar to Floyds Cycle, which is an algorithm
    # that to find if a linked list loops. The common denominator between that algorithm
    # and this solution is that we're using a fast/slow pointer. In this case, we just
    # check to see when we get to the algorithm with the fast pointer, and then take the
    # slow pointer, because at that point it should be in the middle.
    #
    # Extra precaution is taken to make sure we handle even/odd sets correctly. This is
    # done by checking to see if the fast pointer is null, or if its next value is null.
    # Depending on that, we know if the set if even or odd and can return the correct
    # slow pointer
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # loop through linked list using the slow/fast method
        # when fast pointer is finished, return the slow pointer

        slow = head
        fast = head.next

        while (True):
            # list is odd. Slow pointer is already in correct position:
            # [1, 2, 3, 4, 5, N]
            #        S        F
            if fast is None:
                return slow
            
            # list is even. Slow pointer needs to be adjusted because the
            # solution requires a right bias when node count is even:
            # [1, 2, 3, 4, N]
            #     S     F
            if fast.next is None:
                return slow.next

            slow = slow.next
            fast = fast.next.next
        
solution = Solution()
answer = solution.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
print(answer)