from typing import List

# 
# Tags: 
class TicTacToe:

    def __init__(self, n: int):
        # initialize game board from n
        self.size = n
        self.column_sums = {}
        self.row_sums = {}
        self.diag_sums = {}

        self.column_sums[1] = [0 for _ in range(n)]
        self.column_sums[2] = [0 for _ in range(n)]
        self.row_sums[1] = [0 for _ in range(n)]
        self.row_sums[2] = [0 for _ in range(n)]
        self.diag_sums[1] = [0 for _ in range(2)]
        self.diag_sums[2] = [0 for _ in range(2)]

    def move(self, row: int, col: int, player: int) -> int:
        # track points
        self.column_sums[player][col] += 1
        self.row_sums[player][row] += 1
        if row == col:
            self.diag_sums[player][0] += 1
        if self.size - col - 1 == row:
            self.diag_sums[player][1] += 1

        # determine winner
        if self.column_sums[player][col] == self.size:
            return player
        elif self.row_sums[player][row] == self.size:
            return player
        elif self.diag_sums[player][0] == self.size:
            return player
        elif self.diag_sums[player][1] == self.size:
            return player
        
        return 0

        
obj = TicTacToe(3)
p1 = obj.move(0,0,1)
p1 = obj.move(0,2,2)
p1 = obj.move(2,2,1)
p1 = obj.move(1,1,2)
p1 = obj.move(2,0,1)
p1 = obj.move(1,0,2)
p1 = obj.move(2,1,1)
print(p1)