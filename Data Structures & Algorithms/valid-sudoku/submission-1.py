class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen= set()
            for i in range(9):
                if board[row][i]==".":
                    continue
                elif board[row][i] in seen:
                    return False
                else:
                    seen.add(board[row][i])
        
        for col in range(9):
            seen= set()
            for i in range(9):
                if board[i][col]==".":
                    continue
                elif board[i][col] in seen:
                    return False
                else:
                    seen.add(board[i][col])
        

        for box_row in range(3):
            for box_col in range(3):
                box= set()
                for r in range(3):
                    for c in range(3):
                        val= board[3*box_row+r][3*box_col+c]
                        if val=='.':
                            continue 
                        elif val in box:
                            return False
                        else:
                            box.add(val)
        return True
