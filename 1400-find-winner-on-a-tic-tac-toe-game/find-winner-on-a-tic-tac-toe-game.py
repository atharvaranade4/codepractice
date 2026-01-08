from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        a, b = [0] * 8, [0] * 8

        for idx, (row, col) in enumerate(moves):
            player = a if idx % 2 == 0 else b

            # Rows and columns
            player[row] += 1
            player[col + 3] += 1

            # Diagonals
            if row == col:
                player[6] += 1
            if row + col == 2:
                player[7] += 1

            # Check win after each move
            if 3 in player:
                return "A" if player is a else "B"

        # After all moves
        if len(moves) == 9:
            return "Draw"
        return "Pending"
