import sys

def main(array, expect):
    start = 0
    end = 0
    size = len(array)
    sum = 0
    while (start < size):
        while (end < size and sum < expect):
            sum += array[end]
            end += 1
        if (sum == expect):
            print(f'find sum={expect} with index ({start}, {end})')
            return
        sum -= array[start]
        start += 1
    else:
        print(f'not found sum={expect}')



if __name__ == "__main__":
    # execute only if run as a script
    main([1,2,3, 5], 7)