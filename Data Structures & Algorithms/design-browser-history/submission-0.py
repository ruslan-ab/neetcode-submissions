class BrowserHistory:

    class HistoryEntry:
        url: str
        next: HistoryEntry
        prev: HistoryEntry

        def __init__(self, url: str):
            self.url = url
            self.next = None
            self.prev = None


    def __init__(self, homepage: str):
        self.curr = self.HistoryEntry(homepage)

    def visit(self, url: str) -> None:
        newHe = self.HistoryEntry(url)
        newHe.prev = self.curr
        self.curr.next = newHe
        self.curr = newHe

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.prev:
                self.curr = self.curr.prev
            else:
                break
        return self.curr.url

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.next:
                self.curr = self.curr.next
            else:
                break
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)