
def printMatrix(matrix, m, n):
    for i in range(m):
        print(matrix[i])


def verifyAssignment(matrix, m, n, i, j):
    foundXSet = set()
    # print("verify row %s" % i)
    for offset in range(n):
        value = matrix[i][offset]
        if value != 0:
            if value not in foundXSet:
                foundXSet.add(value)
            else:
                # print("found existing %s in %s in row %s" % (value, foundXSet, i))
                return False
    foundYSet = set()
    # print("verify column %s" % j)
    for offset in range(m):
        value = matrix[offset][j]
        if value != 0:
            if value not in foundYSet:
                foundYSet.add(value)
            else:
                # print("found existing %s in %s in column %s" % (value, foundYSet, j))
                return False
    startX = i // 3 * 3
    startY = j // 3 * 3
    foundSet = set()
    # print("verify row [%s:%s] column [%s:%s]" % (startX, startX + 3, startY, startY + 3))
    for offsetX in range(startX, startX + 3):
        for offsetY in range(startY, startY + 3):
            value = matrix[offsetX][offsetY]
            if value != 0:
                if value not in foundSet:
                    foundSet.add(value)
                else:
                    # print("found existing %s in %s in 3x3 sub matrix (%s, %s)" % (value, foundSet, startX, startY))
                    return False
    # print("verified in position (%s, %s)" % (i, j))
    return True


def trySudokuInternal(matrix, m, n, pairs):
    # print("current matrix:")
    # printMatrix(matrix, m, n)
    # print("remain paris: %s" % pairs)
    if not pairs:
        return True
    i, j = pairs.pop()
    # print("try asssign value in (%s, %s)" % (i, j))
    for value in range(1, 10):
        # print("try assign value %s to position (%s, %s)" % (value, i, j))
        matrix[i][j] = value
        result = verifyAssignment(matrix, m, n, i, j)
        if result:
            nextResult = trySudokuInternal(matrix, m, n, pairs)
            if nextResult:
                return True
    # print("failed assign value in (%s, %s)" % (i, j))
    matrix[i][j] = 0
    pairs.append((i, j))
    # print("recover matrix back")
    # printMatrix(matrix, m, n)
    # print("failed to try pair (%s, %s)" % (i, j))
    return False

def trySodoku(matrix, m, n):
    pairs = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                pairs.append((i, j))
    solved = trySudokuInternal(matrix, m, n, pairs)
    if solved:
        print("solved")
        printMatrix(matrix, m, n)
    else:
        print("no solved")

if __name__ == "__main__":
    trySodoku(
        [
            [3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]
        ], 9, 9
    )