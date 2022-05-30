class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class LRUCache:
  
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        #self.left = lru , self.right = mru
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
    #remove from the linkest list
    def remove(self,node):
        prev = node.prev
        nxt = node.next
        prev.next, nxt.prev = nxt, prev
    
    #insert in the linked list at mru(before mru)prev pointer
    def insert(self,node):
        prev,nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next,node.prev = nxt,prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        
        # the key already exist, update the value
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        # grather than capacity
        if len(self.cache) > self.capacity:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
            
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)