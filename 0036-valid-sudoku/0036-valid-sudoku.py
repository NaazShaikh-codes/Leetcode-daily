class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # for row
        for i in range(9):
            present = set()
            for j in range(9):
                if board[i][j] in present:
                    return False
                if board[i][j] == ".":
                    continue
                present.add(board[i][j])

        # for column
        for j in range(9):
            present = set()
            for i in range(9):
                if board[i][j] in present:
                    return False
                if board[i][j] == ".":
                    continue
                present.add(board[i][j])

        # 3 x 3
        for row in range(0,9,3):
            for col in range(0,9,3):
                present = set()

                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in present:
                            return False
                        present.add(board[i][j])
        return True