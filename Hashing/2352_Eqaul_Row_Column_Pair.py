# Given a 0-indexed n x n integer matrix grid, return the number of 
# pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the 
# same elements in the same order (i.e., an equal array).



from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        column = defaultdict(int)
        count = 0
        n = len(grid)
        
        for row in grid:
            rows[tuple(row)] +=1

        for col in range(len(grid[0])):
            curr_col = []
            for row in range(len(grid)):
                curr_col.append(grid[row][col])
            column[tuple(curr_col)] +=1

        for key, value in rows.items():
            if key in column:
                count += rows[key] * column[key]
        return count

        
# Hardest aspect was looping through the columns


