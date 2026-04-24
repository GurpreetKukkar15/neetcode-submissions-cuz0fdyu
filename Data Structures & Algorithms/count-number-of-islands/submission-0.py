from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check for an empty grid
        if not grid or not grid[0]:
            return 0
        
        # visited set now stores (row, col) tuples
        visited = set()
        count = 0
        ROWS, COLS = len(grid), len(grid[0]) # Get dimensions once
        
        for r in range(ROWS):
            for c in range(COLS):
                # Only start DFS if it's land ('1') AND it hasn't been visited
                if grid[r][c] == "1" and (r, c) not in visited:
                    # Found a new island, explore it and increment the count
                    self.explore_island(r, c, grid, visited, ROWS, COLS) 
                    count += 1
                    
        return count
        
    # Renamed helper function to be a proper class method (takes 'self')
    # Added ROWS and COLS for cleaner boundary checking
    def explore_island(self, r: int, c: int, grid: List[List[str]], visited: set, ROWS: int, COLS: int):
        
        # 1. Base Case: Check boundaries and if already visited
        if (r < 0 or r >= ROWS or 
            c < 0 or c >= COLS or 
            (r, c) in visited or 
            grid[r][c] == "0"):
            return

        # 2. Mark the current cell as visited
        visited.add((r, c))

        # 3. Recursively explore all four neighbors (North, East, South, West)
        # Note: All recursive calls now correctly use 'self.'
        self.explore_island(r + 1, c, grid, visited, ROWS, COLS)
        self.explore_island(r, c + 1, grid, visited, ROWS, COLS)
        self.explore_island(r, c - 1, grid, visited, ROWS, COLS)
        self.explore_island(r - 1, c, grid, visited, ROWS, COLS)