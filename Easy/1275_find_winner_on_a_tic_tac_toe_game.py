"""
related topic: array, matrix, simulation, hash table
time complexity: O(n), n = len(moves)
space complexity: O(1)

先依照 moves 擺出棋盤，接著檢查勝負及步數得出結果。

"""


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [["", "", ""], ["", "", ""], ["", "", ""]]

        for index in range(len(moves)):
            board[moves[index][0]][moves[index][1]] = "A" if index % 2 == 0 else "B"

        for i in range(3):
            if (
                (board[i][0] == board[i][1] and board[i][1] == board[i][2])
                or (board[0][i] == board[1][i] and board[1][i] == board[2][i])
            ) and board[i][i] != "":
                return board[i][i]

        if (
            (board[0][0] == board[1][1] and board[1][1] == board[2][2])
            or (board[2][0] == board[1][1] and board[1][1] == board[0][2])
        ) and board[1][1] != "":
            return board[1][1]

        if len(moves) < 9:
            return "Pending"

        return "Draw"
