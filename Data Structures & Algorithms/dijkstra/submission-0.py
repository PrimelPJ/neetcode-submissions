class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        from typing import List, Dict
        import heapq

        # Step 1: Build the adjacency list for the directed, weighted graph
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))  # Append (destination, weight) to source's list

        # Step 2: Initialize distances from the source to all other nodes as infinity
        dist = [float('inf')] * n
        dist[src] = 0  # Distance to source is 0

        # Step 3: Create a min-heap (priority queue) to process nodes by smallest distance
        heap = [(0, src)]  # Each element is (distance_from_src, node)

        # Step 4: Dijkstra's algorithm loop
        while heap:
            current_dist, u = heapq.heappop(heap)  # Get node with smallest known distance

            # Skip processing if we already found a shorter path to this node
            if current_dist > dist[u]:
                continue

            # Check all neighbors of the current node
            for v, weight in graph[u]:
                # If a shorter path to neighbor v is found, update and push to heap
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(heap, (dist[v], v))

        # Step 5: Prepare the result as a dictionary
        # If a node is unreachable, set its distance as -1
        return {i: (dist[i] if dist[i] != float('inf') else -1) for i in range(n)}
