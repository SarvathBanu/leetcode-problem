
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        pq = [(0, k)]

        while pq:
            time, node = heapq.heappop(pq)

            if time > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))

        ans = max(dist[1:])

        return ans if ans != float('inf') else -1
