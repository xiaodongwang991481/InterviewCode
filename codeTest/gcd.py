
def gcd(a, b):
    mod = a % b
    if mod == 0:
        return b
    else:
        return gcd(b, mod)

if __name__ == "__main__":
    for query in [(1, 4), (2, 5), (3, 7), (3, 6), (4, 6), (6, 4), (6, 3)]:
        print("query %s gcd: %s" % (query, gcd(*query)))