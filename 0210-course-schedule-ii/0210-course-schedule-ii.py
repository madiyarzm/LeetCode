class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        visited = set()
        done = set()
        order = []

        def dfs(course):

            if course in visited:
                return False
            
            if course in done:
                return True
            
            visited.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            done.add(course)
            visited.remove(course)
            order.append(course)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
            
        return order


