class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iternative BFS: for each cell, run bfs on UNVISITED island cells,
        # increment count and marking each adjacent cell as visited in a set
        # so that they're conunted as one island.

        # (We use a deque (q) to keep track of cells to visit.
        # In BFS, we explore adjacent cells from the current cell
        # If an adjacent cell is within the grid boundaries, contains "1",
        # and is not visited, we add it to the queue (q) and mark it as visited.)

        # (We traverse the grid using nested loops for each cell.
        # Each time we start BFS in an unvisited "1" cell,
        # it means we have found a new island. We increment the islands count.)
        if not grid:
            return 0

        islands = 0
        rows, cols = len(grid), len(grid[0])
        path = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            path.add((r, c))

            while q:
                x, y = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dx, dy in directions:
                    newX, newY = x + dx, y + dy
                    if (newX in range(rows) and
                            newY in range(cols) and
                            grid[newX][newY] == "1" and
                            (newX, newY) not in path):
                        q.append((newX, newY))
                        path.add((newX, newY))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in path:
                    bfs(r, c)
                    islands += 1

        return islands

# Time: O(m*n)
# Space: O(m*n) for the visited set and the queue
