import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        for point in points:
            distance = math.sqrt((point[0]) ** 2 + (point[1]) ** 2)
            distances.append(distance)

        heap = []
        for pair in list(zip(distances, points)):
            heapq.heappush(heap, pair)

        res = []
        while k > 0:
            pair = heapq.heappop(heap)
            point = pair[1]
            res.append(point)   
            k -= 1

        return res


