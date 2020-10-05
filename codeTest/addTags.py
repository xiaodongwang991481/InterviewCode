
def processTags(input, positionAndTags, currentPosition, index, indexSize, outputs):
    if index == indexSize:
        return currentPosition, index
    start, end, tag = positionAndTags[index]
    outputs.append(input[currentPosition:start])
    currentPosistion = start
    outputs.append('<%s>' % tag)
    endIndex = index + 1
    while endIndex < indexSize:
        if positionAndTags[endIndex][0] > end:
            break
        endIndex += 1
    while index < endIndex:
        print(input, positionAndTags, currentPosition, index, endIndex, outputs)
        currentPosition, index = processTags(
            input, positionAndTags, currentPosition, index + 1, endIndex, outputs
        )
    outputs.append(input[currentPosistion:end])
    outputs.append('</%s>' % tag)
    return end, endIndex

def addTags(input, tags):
    positionAndTags = [(start, end, tag) for tag, indexes in tags.items() for start, end in indexes]
    positionAndTags.sort()
    outputs = []
    currentPosition = 0
    currentIndex = 0
    length = len(positionAndTags)
    while currentIndex < length:
        currentPosition, currentIndex = processTags(
            input, positionAndTags, currentPosition, currentIndex, length, outputs
        )
    outputs.append(input[currentPosition:])
    return ''.join(outputs)



if __name__ == "__main__":
    # execute only if run as a script
    translated = addTags('ABCDE', {'b': [(0, 2)], 'i': [(1, 3)], 'u': [(3, 5)]})
    print(translated)