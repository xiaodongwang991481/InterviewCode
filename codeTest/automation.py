import collections

def buildDFA(pat):
    length = len(pat)
    tf = []
    for i in range(length + 1):
        tf.append({})
    lps = 0
    allChars = set(pat)
    for char in allChars:
        tf[0][char] = 0
    tf[0][pat[0]] = 1
    for i in range(1, length):
        for char in allChars:
            tf[i][char] = tf[lps][char]
        tf[i][pat[i]] = i + 1
        lps = tf[lps][pat[i]]
    for char in allChars:
        tf[length][char] = tf[lps][char]
    print("tf %s" % tf)
    return tf

def search(text, pat):
    tf = buildDFA(pat)
    j = 0
    patLen = len(pat)
    for i in range(len(text)):
        j = tf[j][text[i]]
        if j == patLen:
            print("found %s in index %s" % (pat, i - patLen + 1))


if __name__ == "__main__":
    search("ACACACAGACACAGACAGA", "ACACAGA")