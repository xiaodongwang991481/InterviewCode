import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

def mergeByY(left, right, merged):
    leftIndex = 0
    rightIndex = 0
    leftLength = len(left)
    rightLength = len(right)
    while leftIndex < leftIndex and rightIndex < rightLength:
        if left[leftIndex].y <= right[rightIndex].y:
            merged.append(left[leftIndex])
            leftIndex += 1
        else:
            merged.append(right[rightIndex])
            rightIndex += 1
    while leftIndex < leftLength:
        merged.append(left[leftIndex])
        leftIndex += 1
    while rightIndex < rightLength:
        merged.append(right[rightIndex])
        rightIndex += 1


def findClosestInternal(sortedPairsByX, sortedPairsByY, minAll):
    length = len(sortedPairsByX)
    if length > 1:
        mid = length // 2
        sortedPairsByYL = []
        sortedPairsByYR = []
        minL = findClosestInternal(sortedPairsByX[:mid], sortedPairsByYL, minAll)
        minR = findClosestInternal(sortedPairsByX[mid:], sortedPairsByYR, minAll)
        mergeByY(sortedPairsByYL, sortedPairsByYR, sortedPairsByY)
        minLR = min(minL, minR)
        midX = sortedPairsByX[mid].x
        filteredSortedPairsByY = [item for item in sortedPairsByY if abs(item.x - midX) < minLR]
        filteredLength = len(filteredSortedPairsByY)
        for i in range(filteredLength):
            j = i + 1
            while j < filteredLength and filteredSortedPairsByY[j].y - filteredSortedPairsByY[i].y < minLR:
                foundDistance = filteredSortedPairsByY[i].distance(filteredSortedPairsByY[j])
                if foundDistance < minLR:
                    minLR = foundDistance
                j += 1
        return minLR
    else:
        sortedPairsByY.extend(sortedPairsByX)
        return minAll

def findClosest(pairs):
    length = len(pairs)
    if length < 2:
        raise Exception("no clostest pairs in %s" % pairs)
    sortedPairs = sorted(pairs, key=lambda item: item.x)
    minAll = sortedPairs[0].distance(sortedPairs[1])
    return findClosestInternal(sortedPairs, [], minAll)


if __name__ == "__main__":
    minAll = findClosest([
        Point(2, 3), Point(12, 30),
        Point(40, 50), Point(5, 1),
        Point(12, 10), Point(3, 4)
    ])
    print("find closest distance: %s" % minAll)