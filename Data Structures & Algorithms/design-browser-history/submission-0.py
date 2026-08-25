class ListNode:

    def __init__(self, val = '', prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.left = ListNode()
        self.right = ListNode()


        home = ListNode(homepage)

        self.cur = home
        # left -> home -> right
        # left <- home <- right

    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url, self.cur)

        self.cur = self.cur.next # traverse



    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            steps -= 1
            self.cur = self.cur.prev
        
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            steps -= 1
            self.cur = self.cur.next
        
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)