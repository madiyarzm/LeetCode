#node class for doubly-linked list
class Node():
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #map key to Node

        #set up leftmost and rightmost, & connect them
        self.leftmost, self.rightmost = Node(0, 0), Node(0, 0)
        self.leftmost.next, self.rightmost.prev = self.rightmost, self.leftmost

    #removes
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    #inserts
    def insert(self, node):
        prev, nxt = self.rightmost.prev, self.rightmost
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        #whenever we get something, it becomes -> MRU
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            #remove from linked list, and delete LRU from cache
            lru = self.leftmost.next
            self.remove(lru)
            
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)