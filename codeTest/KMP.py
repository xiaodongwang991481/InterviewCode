def buildLPS(pat):
    length = len(pat)
    lps = [0] * length
    lp = 0
    i = 1
    while i < length:
        if pat[i] == pat[lp]:
            lp += 1
            lps[i] = lp
            i += 1
        else:
            if lp != 0:
                lp = lps[lp - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def search(text, pat):
    lps = buildLPS(pat)
    print('%s lps: %s' % (pat, lps))
    found = []
    ti = 0
    pi = 0
    tl = len(text)
    pl = len(pat)
    for ti in range(tl):
        print("current position: ti=%s pi=%s" % (ti, pi))
        if pat[pi] == text[ti]:
            pi += 1
            if pi == pl:
                pi -= 1
                found.append((ti - pi, ti+1))
                pi = lps[pi]
        else:
            while pi != 0 and pat[pi] != text[ti]:
                pi = lps[pi - 1]
        print("position after: ti=%s pi=%s" % (ti, pi))
    return found


if __name__ == "__main__":
    found = search("ABABDABACDABABCABAB", "ABABCABAB")
    print(found)