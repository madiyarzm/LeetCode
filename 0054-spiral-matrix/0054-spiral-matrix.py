class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        going_right = True
        going_down = False
        going_left = False
        going_up = False

        index = 0
        i = 0
        j = 0

        output = []
        top = 0
        bottom = len(matrix) - 1 
        right_side = len(matrix[0]) - 1
        left_side = 0

        while index < len(matrix) * len(matrix[0]):
                output.append(matrix[i][j])
                index += 1

                if going_right:
                    if j < right_side:
                        j += 1
                    else:
                        going_right = False
                        going_down = True
                        top += 1
                        i += 1

                elif going_down:
                    if i < bottom:
                        i += 1
                    else:
                        going_down = False
                        going_left = True
                        right_side -= 1
                        j -= 1

                elif going_left:
                    if j > left_side:
                        j -= 1
                    else:
                        going_left = False
                        going_up = True
                        bottom -= 1
                        i -= 1

                elif going_up:
                    if i > top:
                        i -= 1
                    else:
                        going_up = False
                        going_right = True
                        left_side += 1
                        j += 1

        return output
