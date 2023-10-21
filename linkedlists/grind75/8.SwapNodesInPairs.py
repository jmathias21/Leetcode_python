from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/swap-nodes-in-pairs/description/
# Tags: Linked List
class Solution:

    # Runtime Complexity: O(N)
    # Space Complexity: O(1)
    # Time: 20:00
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:
            # nodes to swap
            first_node = head
            second_node = head.next

            # swap nodes
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # update head and previous nodes
            head = first_node.next
            prev_node = first_node

        return dummy.next
        
solution = Solution()
answer = solution.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
print(answer)