import heapq

class MaxItem(object):
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


def buildHeap(arr):
    return heapq.heapify(arr)

def getMedian(arr):
    minHeap = []
    maxHeap = []
    for item in arr:
        if not maxHeap:
            heapq.heappush(maxHeap, MaxItem(item))
            print("maxHeap after item %s: %s" % (item, maxHeap))
        elif len(maxHeap) == len(minHeap):
            topMin = heapq.heappop(minHeap)
            minValue = min(item, topMin)
            maxValue = max(item, topMin)
            heapq.heappush(maxHeap, MaxItem(minValue))
            heapq.heappush(minHeap, maxValue)
            print("maxHeap after item %s: %s" % (item, maxHeap))
            print("minHeap after item %s: %s" % (item, minHeap))
        else:
            topMax = heapq.heappop(maxHeap).value
            minValue = min(item, topMax)
            maxValue = max(item, topMax)
            heapq.heappush(maxHeap, MaxItem(minValue))
            heapq.heappush(minHeap, maxValue)
            print("maxHeap after item %s: %s" % (item, maxHeap))
            print("minHeap after item %s: %s" % (item, minHeap))
    if len(maxHeap) == len(minHeap):
        topMax = heapq.heappop(maxHeap).value
        topMin = heapq.heappop(minHeap)
        return (topMax + topMin) / 2
    else:
        return heapq.heappop(maxHeap).value


if __name__ == "__main__":
    median = getMedian([1,2,3,4,5,6,7,8,9])
    print(median)