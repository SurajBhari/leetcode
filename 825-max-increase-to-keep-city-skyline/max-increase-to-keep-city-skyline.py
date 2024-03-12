class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        su = 0 
        matrix = len(grid)
        for n in range(matrix):
            for m in range(len(grid[n])):
                n1 = []
                n2 = []
                n1.extend([grid[n][i] for i in range(matrix)])
                n2.extend([grid[i][m] for i in range(matrix)])
                maximum = min([max(n1), max(n2)])
                su += maximum - grid[n][m]
        return su
                
        