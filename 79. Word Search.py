class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


# dfs on each cell, for each search,
# mark a cell as visited before making recursive calls,
# and remove cur visited cell to backtrack right before you return from dfs;
(  # base cases: we've found the whole word
    #  If the current cell (r, c) is out of bounds or
    # has a diff char than what we look for
    # or has been visited before, return False.)
    # recursively search for 4 adjacent cells
    # iteratie all cells on the board and start DFS from each cell

    ROWS, COLS = len(board), len(board[0])
path = set()


def dfs(r, c, i):
    if i == len(word):
        return True

    if (
            r < 0 or c < 0 or
            r >= ROWS or c >= COLS or
            word[i] != board[r][c] or
            (r, c) in path
    ):
        return False
    path.add((r, c))
    # recursively search for 4 adjacent cells
    res = (
            dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1)
    )
    path.remove((r, c))
    return res


for r in range(ROWS):
    for c in range(COLS):
        if dfs(r, c, 0):
            return True
return False

# time :O(m * n * 4^length of word)
# space: O(L) because of recursive calls and call stacks