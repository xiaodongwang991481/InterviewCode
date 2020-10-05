import bisect

def buildFrequencyMap(arr):
    frequencyMap = {}
    for i in range(len(arr)):
        frequencyMap.setdefault(arr[i], []).append(i)
    return frequencyMap

def queryFrequency(start, end, value, frequencyMap):
    if value not in frequencyMap:
        return 0
    valueRange = frequencyMap[value]
    print("value %s range %s" % (value, valueRange))
    lowerBound = bisect.bisect_left(valueRange, start)
    upperBound = bisect.bisect_right(valueRange, end)
    return upperBound - lowerBound

if __name__ == "__main__":
    arr = [1,2,3,2,1,4,3,2,1,5,3,2,1]
    print(arr)
    frequencyMap = buildFrequencyMap(arr)
    print(frequencyMap)
    for query in [(1,4, 1), (0, 5, 2), (2, 8, 3)]:
        print("start %s, end %s value %s" % query)
        frequency = queryFrequency(*query, frequencyMap)
        print("frequency: %s" % frequency)