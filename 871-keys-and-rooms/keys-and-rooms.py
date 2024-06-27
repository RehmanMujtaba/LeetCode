from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = [False] * len(rooms)
        visited[0] = True

        queue = deque([])
        queue.append(0)

        while queue:
            v = queue.pop()

            for room in rooms[v]:
                if visited[room] == False:
                    queue.append(room)
                    visited[room] = True
        
        for room in visited:
            if room == False:
                return False

        return True
