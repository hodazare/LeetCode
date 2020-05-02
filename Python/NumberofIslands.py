"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
Solution:
using DFS to traverse the nodes and set each visited node to 0.

"""

class Solution(object):
    def zeroMakers(self, i, j, grid):
        
        grid[i][j] = 0
        if i - 1 >= 0 and grid[i-1][j] == '1':
            self.zeroMakers(i-1, j, grid)
        if j - 1 >= 0 and grid[i][j-1] == '1':
            self.zeroMakers(i, j-1, grid)
        if i + 1 < len(grid) and grid[i+1][j] == '1':
            self.zeroMakers(i+1, j, grid)
        if j + 1 < len(grid[0]) and grid[i][j+1] == '1':
            self.zeroMakers(i, j+1, grid)
            
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        
        island = 0
        h = len(grid)
        v = len(grid[0])
        
        for i in range(h):
            for j in range(v):            
                if grid[i][j] == '1':
                    island += 1
                    self.zeroMakers(i, j , grid)
                    
        return island
