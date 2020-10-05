
def bsearch(array, value):
    left = 0
    right = len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            right = mid
        else:
            left = mid + 1
    return None

if __name__ == "__main__":
    found = bsearch([1,2,3,4,5], 6)
    print(found)