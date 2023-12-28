import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                current_value = board[r][c]
                if current_value == ".":
                    continue
                if (current_value in rows[r] or current_value in cols[c] or current_value in boxes[(r // 3, c // 3)]):
                    return False
                else:
                    rows[r].add(current_value)
                    cols[c].add(current_value)
                    boxes[(r // 3, c // 3)].add(current_value)
        # Valid
        return True
