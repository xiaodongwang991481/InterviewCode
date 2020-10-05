
def spareTable(arr):
    n = len(arr)
    sparse = []
    table = []
    for i in range(n):
        table.append((i, i, arr[i]))
    sparse.append(table)
    while n > 1:
        newtable = []
        for i in range(n // 2):
            newtable.append((table[2*i][0], table[2*i + 1][1], table[2*i][2] + table[2*i + 1][2]))
        if n % 2 != 0:
            newtable.append(table[n - 1])
        table = newtable
        sparse.append(table)
        n = (n + 1) // 2
    sparse.reverse()
    return sparse

def getSum(start, end, sparse, level = 0, offset = 0):
    sparseStart, sparseEnd, sum = sparse[level][offset]
    if (start <= sparseStart and end >= sparseEnd):
        return sum
    elif (start > sparseEnd):
        return 0
    elif (end < sparseStart):
        return 0
    return getSum(start, end, sparse, level + 1, 2*offset) + getSum(start, end, sparse, level + 1, 2*offset + 1)


if __name__ == "__main__":
    # execute only if run as a script
    arr = [1,2,3,4,5,6,7,8,9]
    print(arr)
    sparse = spareTable(arr)
    print(sparse)
    for query in ((1, 4), (0, 5), (2, 6)):
        start, end = query
        result = getSum(start, end, sparse)
        print("range %s sum: %s" % (query, result))