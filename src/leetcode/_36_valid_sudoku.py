import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                curr_val = board[r][c]
                if curr_val == ".":
                    continue
                if ((str(curr_val) + "r" + str(r)) in seen or
                    (str(curr_val) + "c" + str(c)) in seen or
                    (str(curr_val) + "b" + str(r//3) + str(c//3)) in seen):
                    return False
                seen.add(str(curr_val) + "r" + str(r))
                seen.add(str(curr_val) + "c" + str(c))
                seen.add(str(curr_val) + "b" + str(r//3) + str(c//3))
        # Valid
        return True
