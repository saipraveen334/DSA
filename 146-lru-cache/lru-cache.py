class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.hashmap={}

        self.left=ListNode(0,0)
        self.right=ListNode(0,0)
        self.left.next=self.right
        self.right.prev=self.left
    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        return -1        

        
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        self.hashmap[key]=Node(key,value)
        self.insert(self.hashmap[key])

        if len(self.hashmap) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.hashmap[lru.key]


        
