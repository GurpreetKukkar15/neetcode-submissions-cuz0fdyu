class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # simple brute force would be to make a list from the 2d matrix
        # by combining all the rows in one and then do binary search on that,
        # not optimal in terms of space 
        # we have to figure out the updates of the l , r , m in a way that matches
        # the format in the matrix

        # eg 1 - 00 and 40 - 23 mid point would be 0 + 2 //2 = 1 and 3 + 0 //2 = 1 so 11 i.e 11
        # we can eliminate all the indexes before 11 in the matrix and update the left to be mid + 1
        # i.e left = 00 + 01 else if it was smaller then update the right = 11 - 01

        row, col = len(matrix), len(matrix[0])

        if target > matrix[row - 1][-1] or target < matrix[0][0]:
            return False

        top = 0
        bot = row - 1
        # first we do an binary search on the matrix rowise
        while top <= bot:
            row = ( top + bot ) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                # target within range of the current row
                break
        
        # # target not in range of the whole matrix
        # if not ( top <= bot):
        #     return False
        
        # then we do binary for that row, columnwise
        row = ( top + bot) // 2
        l , r = 0, col - 1
        while l<=r:
            m = ( l + r) //2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
