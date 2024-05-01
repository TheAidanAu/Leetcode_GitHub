class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # be careful of tuples in Python
        # extract the x and y from the tuple
        # then extra the dx an dy from the hash map
        visited = set()
        moves = {"N": (0, 1),
                 "S": (0, -1),
                 "E": (1, 0),
                 "W": (-1, 0)}
        cur = (0, 0)
        visited.add(cur)

        for dir in path:
            x, y = cur
            dx, dy = moves[dir]
            cur = x + dx, y + dy
            if cur in visited:
                return True
            visited.add(cur)
        return False
# Time: O(N)
# Space O(N) because of the set
