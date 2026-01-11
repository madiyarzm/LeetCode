from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)

        for src, dst in sorted(tickets):
            graph[src].append(dst)

        res = []

        def dfs(src):
            while graph[src]:
                dfs(graph[src].pop(0))
            res.append(src)

        dfs("JFK")
        return res[::-1]
