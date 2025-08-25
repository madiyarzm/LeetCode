class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        answer = [[0] * (i + 1) for i in range(numRows)]

        answer[0] = [1]

        if numRows == 1:
            return [answer[0]]
        
        
        answer[1] = [1,1]

        for i in range(2, numRows):

            answer[i][0] = 1 
            answer[i][i] = 1

            for j in range(1, i):
                answer[i][j] = answer[i - 1][j - 1] + answer[i - 1][j]
        
        return answer