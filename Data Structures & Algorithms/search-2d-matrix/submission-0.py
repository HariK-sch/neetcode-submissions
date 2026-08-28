class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        found = False

        rows = len(matrix)
        cols = len(matrix[0])

        y1 = 0
        y2 = rows - 1

        y = math.floor(y2 / 2)

        row = 0

        foundRow = False
        longestRow = math.floor(math.log2(rows))

        for i in range(longestRow + 1):
            if matrix[y][0] > target:
                y2 = y
            elif matrix[y][cols - 1] >= target:
                print("Found")
                foundRow = True
                row = y
                break
            else:
                y1 = y + 1

            y = math.floor((y2 + y1) / 2)

        print(row)

        if not foundRow:
            return False

        longestColumn = math.floor(math.log2(cols))

        search = matrix[row]
        x1 = 0
        x2 = len(search) - 1

        x = math.floor(x2 / 2)

        for i in range(longestColumn + 1):
            if search[x] < target:
                x1 = x + 1
            elif search[x] > target:
                x2 = x
            else:
                return True

            x = math.floor((x1 + x2) / 2)

        return False




        