from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # --- 1. Check all rows ---
        # (Your code here was perfect)
        for r in range(9):
            seen = set()
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
        
        # --- 2. Check all columns ---
        for c in range(9):
            seen = set()
            for r in range(9):
                # The fix is here:
                # It should be board[r][c], not board[c][r]
                num = board[r][c] 
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)

        # --- 3. Check all 3x3 boxes ---
        # We iterate through the "starting" cell of each box
        # (0,0), (0,3), (0,6), (3,0), (3,3), etc.
        for start_row in range(0, 9, 3): # 0, 3, 6
            for start_col in range(0, 9, 3): # 0, 3, 6
                
                seen = set()
                # Now, iterate 3x3 from that starting cell
                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):
                        num = board[r][c]
                        if num == ".":
                            continue
                        if num in seen:
                            return False
                        seen.add(num)
        
        # If we get through all checks, the board is valid
        return True