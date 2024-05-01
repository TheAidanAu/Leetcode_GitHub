class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Traverse the whole grid to keep track of the # of fresh oranges
        # and add the rotten ones to the queue.
        # Start BFS to simulate the rotting process until there're no fresh ones or if the queue is empty
        # increment time at every iternation
        q = collections.deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in dirs:
                    newX, newY = r + dx, c + dy
                    if (newX in range(ROWS) and
                            newY in range(COLS) and
                            grid[newX][newY] == 1):
                        grid[newX][newY] = 2
                        q.append((newX, newY))
                        fresh -= 1
            time += 1

        if fresh == 0:
            return time
        else:
            return -1

# Time: O(m*n)
# Space: O(m*n) because of the queue