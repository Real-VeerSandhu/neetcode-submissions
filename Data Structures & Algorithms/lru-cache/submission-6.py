class ListNode:
    def __init__(self, key = 0, value = 0, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
    
    def _add_to_right(self, node: ListNode) -> None:
        old_mru = self.right.prev
        
        old_mru.next = node
        node.prev = old_mru

        self.right.prev = node
        node.next = self.right
    
    def _disconnect(self, node: ListNode) -> None:

        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

        node.next = None
        node.prev = None


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._disconnect(node)
        self._add_to_right(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._disconnect(self.cache[key])
            del self.cache[key]
        
        self.cache[key] = ListNode(key, value)
        self._add_to_right(self.cache[key])

        if len(self.cache) > self.cap:
            node_to_delete = self.left.next
            
            self._disconnect(node_to_delete)
            del self.cache[node_to_delete.key]
