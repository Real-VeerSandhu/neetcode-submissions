class StringIterator:

    def __init__(self, compressedString: str):
        self.res = compressedString
        self.ch = ''
        self.num = 0
        self.iterator = 0

    def next(self) -> str:
        if not self.hasNext():
            return ''
        
        if self.num == 0:
            self.ch = self.res[self.iterator] # grabs char
            self.iterator += 1 # puts pointer on new freq number
            while self.iterator < len(self.res) and self.res[self.iterator].isdigit():
                self.num = self.num * 10 + int(self.res[self.iterator])
                self.iterator += 1
        
        self.num -= 1
        return self.ch

    def hasNext(self) -> bool:
        return self.iterator != len(self.res) or self.num != 0
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
