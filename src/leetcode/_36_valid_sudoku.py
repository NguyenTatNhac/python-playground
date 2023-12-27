class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row / column
        for i in range(9):
            col_set = set()
            row_set = set()
            for j in range(9):
                curr_row_val = board[i][j]
                if curr_row_val != '.':
                    if curr_row_val in row_set:
                        return False
                    else:
                        row_set.add(curr_row_val)
                
                curr_col_val = board[j][i]
                if curr_col_val != '.':
                    if curr_col_val in col_set:
                        return False
                    else:
                        col_set.add(curr_col_val)

        # check each sub-box
        box_starting_points = [
            (0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)
        ]
        for i in range(len(box_starting_points)): # 9 boxes
            box_set = set()
            start_row, start_col = box_starting_points[i][0], box_starting_points[i][1]
            for j in range(3):
                for k in range(3):
                    curr_val = board[start_row + j][start_col + k]
                    if curr_val != '.':
                        if curr_val in box_set:
                            return False
                        else:
                            box_set.add(curr_val)
        # Valid
        return True
