from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/merge-two-sorted-lists/
# Tags: linked list
class Solution:

    # Runtime Complexity: O(n + m)
    # Space Complexity: O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a pointer variable and a head variable that are both pointing
        # at a disconnected node
        curr = head = ListNode()
        
        while (list1 and list2):
            if list1.val <= list2.val:
                # move the pointer's next value to the head of list1
                # because that is the next node we want in our combined
                # list
                curr.next = list1

                # move the pointer itself forward
                curr = list1

                # move the list1 head up because we added the current node
                # to our combined list
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next

        # This logic accounts for when one list is longer than the other list
        if (list1 and not list2):
            curr.next = list1
        elif (list2 and not list1):
            curr.next = list2

        return head.next

        
solution = Solution()
answer = solution.mergeTwoLists(ListNode(5), ListNode(1, ListNode(2, ListNode(4))))
print(answer)
answer = solution.mergeTwoLists(ListNode(2, ListNode(3, ListNode(4))), ListNode(2, ListNode(4, ListNode(4))))
print(answer)
answer = solution.mergeTwoLists(ListNode(1, ListNode(3, ListNode(5, ListNode(5)))), ListNode(2, ListNode(4, ListNode(4))))
print(answer)

# C = current
#
#      L1
# H    5 -> N
# C    1 -> 2 -> 4 -> N
#      L2
#
#      L1
# H    5 -> N
# |
#  ->  1 -> 2 -> 4 -> N
#      L2
#      C
#
#      L1
# H    5 -> N
# |
#  ->  1 -> 2 -> 4 -> N
#           L2
#           C
#
#      L1
# H    5 -> N
# |
#  ->  1 -> 2 -> 4 -> N
#                L2
#                C
#
#      C
#      L1
# H    5 -> N
# |
#  ->  1 -> 2 -> 4 -> N
#                     L2
#                
# [1, 2, 4, 5]