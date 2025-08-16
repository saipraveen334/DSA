class MyCalendarTwo:

    def __init__(self):
        self.overlapping = []
        self.nonoverlapping= []
        

    def book(self, startTime: int, endTime: int) -> bool:

        for s , e in self.overlapping:
            if startTime < e and endTime > s:
                return False
        
        for s , e in self.nonoverlapping:
            if startTime < e and endTime > s:
                self.overlapping.append((max(startTime , s) , min(endTime , e)))
        self.nonoverlapping.append((startTime , endTime))

        return True





        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)