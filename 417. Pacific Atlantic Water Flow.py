class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # for each ocean, have a list of boarder cells adjacent to the ocean
        # run dfs on these adjancet cells and keep track of visited cells
        # new cells to visit has a height >= current cell's height
        # find the intersection of both sets

        if not heights:
            return None
        rows, cols = len(heights), len(heights[0])
        edgeP, edgeA = [], []
        va, vp = set(), set()

        for r in range(rows):
            edgeP.append((r, 0))
            edgeA.append((r, cols - 1))
        for c in range(cols):
            edgeP.append((0, c))
            edgeA.append((rows - 1, c))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in dirs:
                newR, newC = r + dr, c + dc
                if (newR in range(rows) and newC in range(cols) and
                        heights[newR][newC] >= heights[r][c] and
                        (newR, newC) not in visited):
                    dfs(newR, newC, visited)

        for (r, c) in edgeP:
            dfs(r, c, vp)
        for (r, c) in edgeA:
            dfs(r, c, va)

        return vp & va

# Time: O(M*N)
# Space: O(M*N)