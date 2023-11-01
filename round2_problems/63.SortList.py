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
    # Time: started 2:05
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(node):
            if node is None or node.next is None:
                return node
            
            mid = getMid(node)

            left = mergeSort(node)
            right = mergeSort(mid)

            dummy = ListNode(-1)
            new_head = dummy

            while left and right:
                if left.val < right.val:
                    new_head.next = left
                    left = left.next
                else:
                    new_head.next = right
                    right = right.next
                new_head = new_head.next

            if left:
                new_head.next = left
            else:
                new_head.next = right

            return dummy.next

        def getMid(head):
            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            mid = slow.next
            slow.next = None
            return mid
        
        return mergeSort(head)

        
solution = Solution()
answer = solution.sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))
print(answer)