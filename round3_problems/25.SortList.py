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
    # Time: started 8:28
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        def mergeSort(head):
            if head.next is None:
                return head
            
            mid = getMid(head)
            
            left = mergeSort(head)
            right = mergeSort(mid)

            return merge(left, right)
        
        def merge(left, right):
            dummy = ListNode()
            head = dummy

            while left and right:
                if left.val < right.val:
                    head.next = left
                    left = left.next
                else:
                    head.next = right
                    right = right.next
                head = head.next

            head.next = left if left else right
            
            return dummy.next
        
        def getMid(node):
            slow = node
            fast = node.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            # sever list at middle
            next = slow.next
            slow.next = None

            return next
        
        sorted = mergeSort(head)
        return sorted
        
solution = Solution()
answer = solution.sortList(ListNode(8, ListNode(5, ListNode(4, ListNode(7, ListNode(1, ListNode(9, ListNode(2))))))))
answer = solution.sortList([8,5,4,7,1,9,2])
print(answer)