
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = [[] for _ in range(n)]

        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        prob = [0.0] * n
        prob[start_node] = 1.0

        pq = [(-1.0, start_node)]

        while pq:
            p, node = heapq.heappop(pq)
            p = -p

            if node == end_node:
                return p

            if p < prob[node]:
                continue

            for neighbor, edge_prob in graph[node]:
                new_prob = p * edge_prob

                if new_prob > prob[neighbor]:
                    prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))

        return 0.0
