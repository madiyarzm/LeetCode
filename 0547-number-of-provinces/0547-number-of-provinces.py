class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        

        #built lists as value for hashmap
        graph = {i: [] for i in range(len(isConnected))}

        #assigning connections to each city in hashmap
        for city in range(len(isConnected)):
            for connection in range(len(isConnected[0])):
                    if city == connection or not isConnected[city][connection]:
                        continue
                    
                    graph[city].append(connection) 

        
        visited = set()

        #dfs 
        def dfs(node):

            #if we didnt explore this city, then go for it
            if node not in visited:
                visited.add(node)

                #explore its connection's connections
                for nei in graph.get(node, 0):
                    dfs(nei)
        
        counter = 0

        #loop through all provinces -> each index is certain city 
        for connections in range(len(isConnected)):

            if connections not in visited:
                dfs(connections)
                counter += 1
        
        return counter