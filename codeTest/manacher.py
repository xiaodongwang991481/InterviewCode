def expendStr(arr):
    alist = ['|', '|']
    alist[1:-1] = [item for item in '|'.join(arr)]
    return alist

def manacher(arr):
    if not arr:
        return 0
    expendArr = expendStr(arr)
    length = len(expendArr)
    lps = [0] * length
    lps[1] = 1
    for i in range(2, len(expendArr)):
        lps[i] = max(0, min(lps[i-1] - 1, lps[i-2]))
        print("lps at %s: %s" % (i, lps[i]))
        while i - lps[i] > 0 and i + lps[i] + 1 < length and expendArr[i-lps[i]-1] == expendArr[i+lps[i]+1]:
            lps[i] += 1
        print("lps at %s after expension: %s" % (i, lps[i]))
    return expendArr, lps

if __name__ == "__main__":
    expendedArr, palindom = manacher("babcbabcbaccba")
    print(expendedArr)
    print(palindom)