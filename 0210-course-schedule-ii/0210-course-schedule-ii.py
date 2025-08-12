class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        #we need one more set to track explored courses
        visited = set()
        done = set()
        order = []

        def dfs(course):

            if course in visited:
                return False
            
            #compared to Course I, we cant clear prereqs, so we check whether its done
            if course in done:
                return True
            
            visited.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):

                    #here False its just indicator to return empty list later
                    return False
            
            #if prereqs had no cycles, then add this course as done
            done.add(course)

            #remove it, to not detect cycle accidentally
            visited.remove(course)

            #and create topological order, since now we are in the lowest level
            order.append(course)

            return True
        

        for crs in range(numCourses):

            #if there is False indicator
            if not dfs(crs):
                return []
        
        #if not give the order itself
        return order


