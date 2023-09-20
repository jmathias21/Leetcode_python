from typing import List
import heapq

# https://leetcode.com/problems/k-closest-points-to-origin/
# Tags: heap implementation, heap, divide and conquer, euclidian distance
class Solution:

    # Runtime Complexity: O(n log k) where n are the points and k is the heap size
    # Space Complexity: O(k)
    # Time: Not timed
    #
    # This solution uses a max heap to keep track of the lowest k distances of each
    # of the points. We calculate the euclidian distance, and then we build out our heap,
    # removing the largest value when we reach the maximum size of k. At the end, we have
    # the lowest distances and can simply return them as an array in any order
    def kClosestUsingHeap(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            # calculate euclidian distance (we don't squareroot it though because
            # we don't need it for comparisons). We also take the negative value as
            # a trick so we can treat heapq as a max heap rather than a min heap
            dist = -(x*x + y*y)

            # if the length of the heap is greater than k, push our new element
            # onto the heap and pop off the highest element (i.e. the root)
            if len(heap) >= k:
                heapq.heappushpop(heap, (dist, x, y))
            # otherwise, just push the element onto the heap
            else:
                heapq.heappush(heap, (dist, x, y))

        # loop through the heap and build an array of [x,y] values from
        # what's left
        return [(x, y) for (dist, x, y) in heap]


    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: Not timed
    #
    # This solution is similar to the above, but it uses a custom heap
    # implementation
    def kClosestUsingCustomHeap(self, points: List[List[int]], k: int) -> List[List[int]]:
        # create max heapify function

        def maxHeapify(heap, size, i):
            l = (2 * i) + 1
            r = (2 * i) + 2

            largest = i

            if l < size and heap[l] > heap[i]:
                largest = l

            if r < size and heap[r] > heap[largest]:
                largest = r
            
            if largest != i:
                temp = heap[i]
                heap[i] = heap[largest]
                heap[largest] = temp
                maxHeapify(heap, size, largest)

        def heapPop(heap):
            if not heap:
                return None

            size = len(heap)

            maximum = heap[0]

            heap[0] = heap[size - 1]
            heap.pop()

            maxHeapify(heap, size - 1, 0)

            return maximum
        
        def parent(i):
            return (i - 1) // 2
        
        def heapPush(heap, val):
            # Append the new value to the heap
            heap.append(val)

            i = len(heap) - 1
            while i != 0 and heap[parent(i)] < heap[i]:
                # Swap the value with its parent
                heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
                i = parent(i)

        heap = []
        for point in points:
            # determine euclidean distance to [0,0]
            dis = (point[0] ** 2) + (point[1] ** 2)

            # add distance to current heap
            heapPush(heap, (dis, point[0], point[1]))

            # call maxHeapify if size > k
            heap_len = len(heap)
            if (heap_len > k):
                heapPop(heap)

        answer = []

        # return the top k results from heap
        while k > 0:
            _, x, y = heapPop(heap)
            answer.append([x, y])
            k -= 1

        return answer

        
solution = Solution()
#answer = solution.kClosestUsingHeap([[-5,4],[-3,2],[0,1],[-3,7],[-2,0],[-4,-6],[0,-5]], 6)
answer = solution.kClosestUsingHeap([[3,3],[5,-1],[-2,4]], 2)
#answer = solution.kClosestUsingHeap([[1,3],[-2,2]], 1)
print(answer)

# Example for kClosestUsingHeap solution:
# points = [[3,3],[5,-1],[-2,4]], k = 2
# distance of [3,3] = 18
# flip 18 to -18
# heap = []
# len(heap) < k, so push -18
# heap = [-18]
#
# distance of [5,-1] = 26
# flip 26 to -26
# heap = [-18]
# len(heap) < k, so push -26
# heap = [-26,-18] (-26 is smaller than -18, so it gets set as the root)
#
# distance of [-2,4] = 20
# flip 20 to -20
# heap = [-26,-18]
# len(heap) >= k, so push -20 and pop the highest value
# heap = [-26, -20, -18]
# heap = [-20, -18]

# The heap gets the x and y values stored with the distance as well, so it
# actually looks like [(-20, -2, 4), (-18, 3, 3)]. Therefore our answer is
# [[-2, 4], [3, 3]]