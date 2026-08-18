class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0
    
    def length(self):
        return self.size
    
    def push_right(self, node):
        left_node = self.right.prev
        left_node.next = node
        node.prev = left_node

        node.next = self.right
        self.right.prev = node

        self.size += 1
    
    def pop(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        node.prev = None
        node.next = None

        self.size -= 1
    
    def pop_left(self):
        if self.length() == 0:
            return None
        node = self.left.next
        self.pop(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfu_count = 0

        self.node_map = {} # maps key -> nodes

        self.list_map = defaultdict(LinkedList) # maps freq -> ll of nodes

    def counter(self, node):
        count = node.freq
        self.list_map[count].pop(node)

        if count == self.lfu_count and self.list_map[count].length() == 0:
            self.lfu_count += 1
        
        node.freq += 1
        self.list_map[node.freq].push_right(node)

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        node = self.node_map[key]
        self.counter(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.counter(node)
            return
        
        if len(self.node_map) == self.cap:
            node = self.list_map[self.lfu_count].pop_left()
            self.node_map.pop(node.key)
        
        node = ListNode(key, value)
        self.node_map[key] = node
        self.list_map[1].push_right(node)
        self.lfu_count = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)