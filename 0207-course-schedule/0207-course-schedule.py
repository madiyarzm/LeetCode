class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #first we need to turn these lists into dictionary

        #dictioanry creation comprehension
        graph = {i: [] for i in range(numCourses)}
        
        #assigning prereq for each course (b -> a)
        for course,prereq in prerequisites:
            graph[course].append(prereq)

        #dfs 
        
        seen = set()
        cycle = set()

        def dfs(course):

            #base case
            if course in seen:
                return False
            
            if graph[course] == []:
                return True
            
            seen.add(course)

            for neigbor in graph[course]:
                if not dfs(neigbor):
                    return False
            
            seen.remove(course)
            graph[course] = []
            return True

        
        #additional measure for a case when there are not connected mini graphs
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
