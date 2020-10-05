def sqrt(x: int) -> int:
    start = 0
    end = x + 1
    while start  < end:
        mid = (start + end) // 2
        squared = mid * mid
        if squared > x:
            end = mid
        else:
            start = mid + 1
        print('start=%s, end=%s' % (start, end))
    return end - 1

if __name__ == "__main__":
    print(sqrt(4))
    print(sqrt(1))