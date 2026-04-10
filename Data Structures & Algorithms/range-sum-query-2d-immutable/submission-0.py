class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.new_matrix= []
        rows, cols= len(matrix), len(matrix[0])
        
        
        for i in range(rows+1):
            row=[]
            for j in range(cols+1):
                row.append(0)
            self.new_matrix.append(row)

        for i in range(1,rows+1):
            for j in range(1, cols+1):
                self.new_matrix[i][j]= matrix[i-1][j-1]+ self.new_matrix[i][j-1]+ self.new_matrix[i-1][j]- self.new_matrix[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        bottomRight = self.new_matrix[row2+1][col2+1]  # entire rectangle to bottom-right
        above       = self.new_matrix[row1][col2+1]    # rectangle above our region
        left        = self.new_matrix[row2+1][col1]    # rectangle left of our region
        topLeft     = self.new_matrix[row1][col1]      # overlap, added back
        return bottomRight - above - left + topLeft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


