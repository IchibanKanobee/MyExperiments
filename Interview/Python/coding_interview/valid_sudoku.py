class Solution:
    def isValidSudoku(self, board):

        def checkRow(board):
            for i in range(9):
                l = [0] * 9
                for j in range(9):
                    if board[i][j] != ".":
                        if l[int(board[i][j]) - 1] == 1:
                            return 0
                        else:
                            l[int(board[i][j]) - 1] = 1
            return 1

        def checkColumn(board):
            for i in range(9):
                l = [0] * 9
                for j in range(9):
                    if board[j][i] != ".":
                        if l[int(board[j][i]) - 1] == 1:
                            return 0
                        else:
                            l[int(board[j][i]) - 1] = 1
            return 1

        def checkBox(board):
            # c = 0
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    l = [0] * 9
                    for x in range(i, i + 3):
                        for y in range(j, j + 3):
                            if board[x][y] != ".":
                                if l[int(board[x][y]) - 1] == 1:
                                    return 0
                                else:
                                    l[int(board[x][y]) - 1] = 1
            return 1

        return checkRow(board) and checkColumn(board) and checkBox(board)


board = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


s = Solution()
print (s.isValidSudoku((board)))