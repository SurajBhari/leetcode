class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        su = 0 
        matrix = len(grid)
        for n in range(matrix):
            for m in range(len(grid[n])):
                n1 = []
                n2 = []
                for i in range(matrix):
                    n1.append(grid[n][i])
                    n2.append(grid[i][m])
                su += min([max(n1), max(n2)]) - grid[n][m]
        return su
                
        