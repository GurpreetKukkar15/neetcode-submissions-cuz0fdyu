class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result= []

        for i in range(len(matrix)):

            for j in range(len(matrix[i])):
                result.append(matrix[i][j])
        
        low=0
        high= len(result)
        if result[0] > target or result[-1] < target:
            return False
        while low <= high:
            mid = low + (high-low)//2
            if result[mid]==target:
                return True
            
            if result[mid] > target:
                high= mid-1
            
            if result[mid] < target:
                low= mid+1
        
        return False
