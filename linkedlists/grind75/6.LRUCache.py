from typing import List

class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

# https://leetcode.com/problems/lru-cache/
# Tags: Doubly linked list, Least recently used (LRU)
# Time: Not timed
#
# Uses a double linked list to maintain the order of each key so that we always know what the
# LRU is. When we get a key, we move it to the back of the list. When we modify a key, we move it
# to the back of the list. If the list is at capacity, we find the LRU node (front of the list),
# remove it and add our new node at the end of the list
#
# Space Compexity: O(n) where n is the capacity
class LRUCache:

    # Time Complexity: O(1)
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        

    # Time Complexity: O(1)
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        self.remove(self.map[key])
        node = ListNode(key, self.map[key].val)
        self.map[key] = node
        self.add(node)
        return node.val

    # Time Complexity: O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
    
        node = ListNode(key, value)
        self.map[key] = node
        self.add(node)

        if len(self.map) > self.capacity:
            del_key = self.head.next.key
            self.remove(self.head.next)
            del self.map[del_key]


    def add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


obj = LRUCache(2)
obj.put('1',1)
obj.put('2',2)
obj.get('1')
obj.put('3',3)
obj.get('2')
obj.put('4',4)
obj.get('1')
obj.get('3')
obj.get('4')

obj = LRUCache(4)
obj.put('A',5)
obj.put('B',6)
obj.put('C',7)
obj.put('D',8)
obj.put('A',9)
obj.put('E',10)
obj.put('F',11)

# Example: Capacity 3
# Put ['A', 1]
# Put ['B', 2]
# Put ['C', 3]

# Current doubly linked list:
# H -> A -> B -> C -> T

# Get ['B'] (re-order B to the end of the list)
    # Remove B:   H -> A -> C -> T
    # Add B:      H -> A -> C -> B -> T
    # Return 2

# Put ['E', 4] (at max capacity. Replace LRU)
    # Remove A:   H -> C -> B -> T
    # Add E:      H -> C -> B -> E -> T

# Put ['B', 4] (key already exists. Replace and re-order to end of list)
    # B already exists
    # Remove B:   H -> C -> E -> T
    # Add B:      H -> C -> E -> B -> T