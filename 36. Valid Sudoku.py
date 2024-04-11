class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Traverse every cell in the board,
        # check to make sure no dups in each row, col and sub-box
        # Use sets to keep track of numbers for every row, column, and sub-box==
        cols = defaultdict(set)
        rows = defaultdict(set)
        subbox = defaultdict(set)  # key = a tuple of (r//3, c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                # Checks if the current number is already in the same row, column, or subbox
                if (
                        board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in subbox[(r // 3, c // 3)]
                ):
                    return False
                # If the number is not already present in the corresponding row, column, or subbox,
                # it adds it to the respective sets (rows, cols, and subbox) to keep track of encountered numbers
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                subbox[(r // 3, c // 3)].add(board[r][c])

        return True
# time: O(9*9) goes through every single cell
# space: O(9*9) because of the sets
