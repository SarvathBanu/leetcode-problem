
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        MOD = 10**9 + 7

        graph = [[] for _ in range(n)]

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float('inf')] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]

        while pq:
            time, node = heapq.heappop(pq)

            if time > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]

                    heapq.heappush(pq, (new_time, neighbor))

                elif new_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]
