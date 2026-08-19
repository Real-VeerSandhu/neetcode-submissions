class StockSpanner:
    # invairant -> stack is decreasing from left to right, right=top

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            old_price_top, old_span = self.stack.pop()
            res += old_span
        
        self.stack.append((price, res))
        return res

"""
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1

no stack so just do

stack = [100]

---

stockSpanner.next(80); // return 1

stack = [100, 80] < top

today_price = 101

--


[(7, 1), (2, 1), (1, 1)]

-> (2, )

stockSpanner.next(60); // return 1
stockSpanner.next(70); // return 2
stockSpanner.next(60); // return 1
stockSpanner.next(75); // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85); // return 6

"""

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)