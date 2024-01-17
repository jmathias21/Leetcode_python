from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Runtime Complexity: O(n log k)
    # Space Complexity: O()
    # Time: 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        heap = []
        # O(n)
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))

        curr = dummy
        
        while heap:
            _, i, head = heapq.heappop(heap)

            curr.next = head
            curr = curr.next

            if head.next:
                heapq.heappush(heap, (head.next.val, i, head.next))
                head = head.next

        return dummy.next
    
solution = Solution()
answer = solution.mergeKLists([ListNode(1, ListNode(4, ListNode(5))),ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])
print(answer)