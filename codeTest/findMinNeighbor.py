def findMinNeiborInternal(arr, start, end):
    # print('find min neighor with start=%s, end=%s' % (start, end))
    if end - start <= 2:
        return end - 1
    mid = start + (end - start) // 2
    # print('try mid=%s' % mid)
    if arr[mid] > arr[mid - 1]:
        return findMinNeiborInternal(arr, start, mid)
    if arr[mid] > arr[mid + 1]:
        return findMinNeiborInternal(arr, mid, end)
    return mid

def findMinNeighbor(arr):
    length = len(arr)
    if length == 0:
        return -1
    if length == 1:
        return 0
    if arr[0] <= arr[1]:
        return 0
    if arr[length - 1] <= arr[length - 2]:
        return length - 1
    return findMinNeiborInternal(arr, 0, length)


if __name__ == "__main__":
    # execute only if run as a script
    mid = findMinNeighbor([5,4,3,4,5])
    print(mid)