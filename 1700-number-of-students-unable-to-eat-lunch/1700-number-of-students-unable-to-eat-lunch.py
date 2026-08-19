class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        

        while sandwiches and sandwiches[0] in students:

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            
            else:
                left = students.pop(0)
                students.append(left)
            
        
        return len(sandwiches)
        
