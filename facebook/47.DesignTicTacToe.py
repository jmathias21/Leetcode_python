from typing import List

# https://leetcode.com/problems/design-tic-tac-toe/
# Tags: 
# Time: 35:00
class TicTacToe:

    def __init__(self, n: int):
        # initialize game board from n
        self.size = n
        self.column_sums = [0 for _ in range(n)]
        self.row_sums = [0 for _ in range(n)]
        self.r_diag_sums = [0 for _ in range(n + n - 1)]
        self.l_diag_sums = [0 for _ in range(n + n - 1)]


    def move(self, row: int, col: int, player: int) -> int:
        s = 1 if player == 1 else 1000

        self.column_sums[col] += s
        self.row_sums[row] += s
        self.r_diag_sums[row + col] += s
        self.l_diag_sums[row + (self.size - (col + 1))] += s

        if self.column_sums[col] == self.size * 1000:
            return 2
        if self.row_sums[row] == self.size * 1000:
            return 2
        if self.r_diag_sums[row + col] == self.size * 1000:
            return 2
        if self.l_diag_sums[row + (self.size - (col + 1))] == self.size * 1000:
            return 2
        
        if self.column_sums[col] == self.size:
            return 1
        if self.row_sums[row] == self.size:
            return 1
        if self.r_diag_sums[row + col] == self.size:
            return 1
        if self.l_diag_sums[row + (self.size - (col + 1))] == self.size:
            return 1
        
        return 0


obj = TicTacToe(3)
p1 = obj.move(0,0,1)
p1 = obj.move(0,2,2)
p1 = obj.move(2,2,1)
p1 = obj.move(1,1,2)
p1 = obj.move(2,0,1)
p1 = obj.move(1,0,2)
p1 = obj.move(2,1,1)