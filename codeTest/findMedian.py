def median(array1, array2):
    prev = 0
    current = 0
    count1 = len(array1)
    count2 = len(array2)
    count = count1 + count2
    medianNumber = count // 2
    array1Offset = 0
    array2Offset = 0
    offset = 0
    while (offset <= medianNumber and array1Offset < count1 and array2Offset < count2):
        prev = current
        if (array1[array1Offset] < array2[array2Offset]):
            current = array1[array1Offset]
            array1Offset += 1
        else:
            current = array2[array2Offset]
            array2Offset += 1
        offset += 1
    while (offset <= medianNumber and array1Offset < count1):
        prev = current
        current = array1[array1Offset]
        array1Offset += 1
        offset += 1
    while (offset <= medianNumber and array2Offset < count2):
        prev = current
        current = array2[array2Offset]
        array2Offset += 1
        offset += 1
    if (count % 2 == 0):
        return (prev + current) / 2
    else:
        return current

def median2(array1, array2):



if __name__ == "__main__":
    found = median([1,3,5,7,9], [2,4,6,8])
    print(found)