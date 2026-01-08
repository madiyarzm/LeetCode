class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = {i: [] for i in range(n)}

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(graph, s, d):

            visited = {s}
            stack = [s]

            while stack:
                current = stack.pop()

                if current == d:
                    return True
                
                for nei in graph[current]:
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)

            return False
        
        return dfs(graph, source, destination)