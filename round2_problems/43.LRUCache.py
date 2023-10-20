class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

# Time: started 2:33, stopped 3:03
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}


    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # update node
            node = self.map[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            # replace LRU node
            if len(self.map) == self.capacity:
                new_node = ListNode(key, value)
                self.insert(new_node)
                self.map[key] = new_node
                
                lru_node = self.head.next
                self.remove(lru_node)
                del self.map[lru_node.key]
            else:
                # Add node
                new_node = ListNode(key, value)
                self.insert(new_node)
                self.map[key] = new_node



    def insert(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
p1 = obj.get(1)
obj.put(3,3)
p2 = obj.get(2)
obj.put(4,4)
p3 = obj.get(1)
p4 = obj.get(3)
p5 = obj.get(4)

# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4