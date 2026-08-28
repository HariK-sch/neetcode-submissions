class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        grids = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if (board[i][j]) == ".":
                    continue

                num = int(board[i][j])

                if num in rows[i]:
                    return False
                rows[i].add(num)

                if num in cols[j]:
                    return False
                cols[j].add(num)

                grid = i // 3 + (3 * (j // 3))

                if num in grids[grid]:
                    return False
                grids[grid].add(num)
        
        return True





        