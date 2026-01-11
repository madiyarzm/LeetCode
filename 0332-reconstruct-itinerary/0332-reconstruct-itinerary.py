from collections import defaultdict, deque

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(deque)

        for src, dst in sorted(tickets):
            graph[src].append(dst)

        res = []

        def dfs(src):
            while graph[src]:
                dfs(graph[src].popleft())
            res.append(src)

        dfs("JFK")
        return res[::-1]
