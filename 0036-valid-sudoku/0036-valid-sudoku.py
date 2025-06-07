class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        box_index = 0
        
        box_set = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                
                if board[i][j] != '.':
                    if board[i][j] in rows[i]:
                        return False
                    
                    else:
                        rows[i].add(board[i][j])
                
                if board[j][i] != '.':
                    if board[j][i] in columns[i]:
                        return False
                    
                    else:
                        columns[i].add(board[j][i])
        
        for i in range(9):
            for j in range(9):
                
                box_index = (i // 3) * 3 + j // 3
                
                if board[i][j] != '.':
                    if board[i][j] in box_set[box_index]:
                        return False
                    
                    else:
                        box_set[box_index].add(board[i][j])
        
        return True