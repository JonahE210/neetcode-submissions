import heapq
class MedianFinder:

    def __init__(self):
        self.small = [] #max heap to get the biggest of the small numbers (closer to the middle of the array)
        self.big = [] #min heap, converse logic
        
    def addNum(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.big, num)

        if len(self.small) > len(self.big) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.big, value)

        elif len(self.big) > len(self.small) + 1:
            value = heapq.heappop(self.big)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return float(-self.small[0])

        if len(self.big) > len(self.small):
            return float(self.big[0])

        return (-self.small[0] + self.big[0]) / 2