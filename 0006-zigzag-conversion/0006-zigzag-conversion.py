class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ['' for _ in range(numRows)] 
        current_row_index = 0
        going_down = True

        if numRows == 1 or numRows >= len(s):
            return s

        
        for i in range(len(s)):
            rows[current_row_index] += s[i]

            if current_row_index == numRows - 1:
                going_down = False
            
            elif current_row_index == 0:
                going_down = True

            if going_down == True:
                current_row_index += 1

            elif going_down == False:
                current_row_index -= 1
            


        
        return ''.join(rows)
        

