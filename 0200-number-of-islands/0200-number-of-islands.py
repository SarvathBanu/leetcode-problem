class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(i, j):
            stack = [(i, j)]

            while stack:
                r, c = stack.pop()

                if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                    continue

                grid[r][c] = "0"

                stack.append((r+1, c))
                stack.append((r-1, c))
                stack.append((r, c+1))
                stack.append((r, c-1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count