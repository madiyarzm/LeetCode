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

        def dfs(course):

            #base case, during exploration of course's prereqs I found out course itself
            if course in seen:
                return False
            
            #seeing whether this courses prereqs are fully cleared, if its -> go higher level
            if graph[course] == []:
                return True
            
            #start marking the current course we r going to dive 
            seen.add(course)

            #for each prereq of the course
            for neigbor in graph[course]:

                #if course's prereq itself has a cycle, then end this course exploration.
                if not dfs(neigbor):
                    return False
            
            #if all was clear, then remove this course from exploration
            seen.remove(course)

            #and clear all of its prereqs
            graph[course] = []
            return True

        
        #additional measure for a case when there are not connected mini graphs
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True

