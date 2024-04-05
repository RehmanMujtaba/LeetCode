import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        sol = []

        for point in points:
            dist = pow(point[0], 2) + pow(point[1], 2)
            x = point[0]
            y = point[1]
            if len(heap) < k:
                heappush(heap, [-1 * dist, x, y])
            elif heap[0][0] < -1 * dist:
                heappop(heap)
                heappush(heap, [-1 * dist, x, y])

        for points in heap:
            sol.append([points[1], points[2]])

        return sol