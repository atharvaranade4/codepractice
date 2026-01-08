from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        a, b = [0] * 8, [0] * 8

        for i, (row, col) in enumerate(moves):
            player = a if i % 2 == 0 else b

            # row
            player[row] +=1
            #column
            player[col + 3] +=1

            # Diagonals
            if row == col:
                player[6] += 1
            if row + col == 2:
                player[7] += 1

            #check win
            if 3 in player:
                return "A" if player is a else "B"

        # after all moves
        if len(moves) == 9:
            return "Draw"
        return "Pending"